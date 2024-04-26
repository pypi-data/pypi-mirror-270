import numpy as np
from torchvision import models
from torchvision.io import read_image
import os
import pandas as pd
from rich.progress import track
import tkinter as tk
from tkinter import filedialog
from sklearn.cluster import KMeans
import cv2
import matplotlib.pyplot as plt

class ImageEmbedding:
    
    def __init__(self, model_name_list: list = ['resnet50', 'SwinTransfomer', 'VisionTransfomer']):
        self.model_name_list = model_name_list
        self.database_size = 0
        self.modelSelection()
    
    def modelSelection(self) -> models:
        
        model_list = []
        preprocess_list = []
        
        for model in self.model_name_list:
            if model == 'resnet50':
                
                weights = models.ResNet50_Weights.DEFAULT
                model = models.resnet50(weights=weights)
                preprocess = weights.transforms()
                model_list.append(model)
                preprocess_list.append(preprocess)
                
            elif model == 'SwinTransfomer':
                
                weights = models.Swin_V2_B_Weights.DEFAULT
                model = models.swin_v2_b(weights=weights)
                preprocess = weights.transforms()
                model_list.append(model)
                preprocess_list.append(preprocess)
                
            elif model == 'VisionTransfomer':
                
                weights = models.ViT_B_16_Weights.DEFAULT
                model = models.vit_b_16(weights=weights)
                preprocess = weights.transforms()
                model_list.append(model)
                preprocess_list.append(preprocess)
                
        
        self.model_list = model_list          
        self.preprocess_list = preprocess_list
                    
            

    def imageEmbedding(self, imagePath: str) -> np.ndarray:
        
        embed_vector = np.array([])
        
        for index, model in enumerate(self.model_list):
            
            image = read_image(imagePath)
            image = self.preprocess_list[index](image)
            image = image.unsqueeze(0)
            
            vector = model(image)
            embed_vector = np.concatenate((embed_vector, vector.detach().numpy().flatten()))
            
        return embed_vector / np.linalg.norm(embed_vector)
    
    
    def imageVectorDatabaseBuild(self, image_folder_path, save_base_path='.', save_database_name='image_vector_database.json', save_cluster_name='cluster_info.json' ,cluster_num=10):
    
        database_size = 0
        
        for root, dirs, files in track(os.walk(image_folder_path), description='Checking Vector Database Size...'):
            for file in files:
                
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.JPG'):
                    
                    database_size += 1
        
        self.database_size = database_size 
        print(f'Database Size: {database_size}')
                    
        database = pd.DataFrame(columns=['image_path', 'embedding_vector'], index=range(database_size))
        
        index = 0
        
        for root, dirs, files in track(os.walk(image_folder_path), description='Building Vector Database...'):
            for file in files:
                
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.JPG'):
                    
                    image_path = os.path.join(root, file)
                    embed_vector = self.imageEmbedding(image_path)
                    
                    database.loc[index, 'image_path'] = image_path
                    database.loc[index, 'embedding_vector'] = embed_vector
                    index += 1
        
        database.to_json(os.path.join(save_base_path, save_database_name))
        self.database_path = os.path.join(save_base_path, save_database_name)
        self.database = database
        self.clusterDatabase(save_base_path, save_cluster_name, cluster_num)
        
    def clusterDatabase(self, save_base_path='.', save_cluster_name='cluster_info.json' ,cluster_num=10):
        
        kmeans = KMeans(n_clusters=cluster_num)
        kmeans.fit(list(self.database['embedding_vector']))
        
        cluster_centers = kmeans.cluster_centers_
        cluster_labels = kmeans.labels_
        cluster_index = [_ for _ in range(cluster_num)]
        for i in range(cluster_num):
            cluster_index[i] = np.where(cluster_labels == i)
        
        cluster = pd.DataFrame(columns=['cluster_center', 'cluster_index'])
        cluster['cluster_center'] = cluster_centers.tolist()
        cluster['cluster_index'] = cluster_index
        cluster.to_json(os.path.join(save_base_path, save_cluster_name))
        
        self.cluster = cluster
    
    def imageVectorDatabaseLoad(self, database_path, cluster_path=None):
        
        database = pd.read_json(database_path)
        self.database = database
        self.database_size = len(database)
        self.database_path = database_path
        
        if cluster_path is not None:
            cluster = pd.read_json(cluster_path)
            self.cluster = cluster
            
        else:
            save_path = database_path.split('/')
            save_path.pop()
            save_path = '/'.join(save_path)
            self.clusterDatabase(save_path, 'cluster_info.json', 10)
      
    
    def imageQuery(self):
        
        if self.database_size == 0:
            print('Database is empty. Please build the database first.')
            return
        
        
        root = tk.Tk()
        root.withdraw()
        
        file_path = filedialog.askopenfilename(
            title='Select Image',
            filetypes=[('Image Files', ['*.png', '*.jpg', '*.jpeg', '*.JPG'])]
        )
        
        root.destroy()
        
        smallest_distance = -1

        
        query_vector = self.imageEmbedding(file_path)
        
        for index, center in enumerate(self.cluster['cluster_center']):
            
            distance = np.linalg.norm(query_vector - np.array(center))
            
            if smallest_distance == -1:
                smallest_distance = distance
                smallest_index = index
            elif distance < smallest_distance:
                smallest_distance = distance
                smallest_index = index
                
        cluster_index = self.cluster.loc[smallest_index, 'cluster_index']
        smallest_distance= -1
        
        for index in cluster_index[0]:
            distance = np.linalg.norm(query_vector - self.database.loc[index, 'embedding_vector'])
            
            if smallest_distance == -1:
                smallest_distance = distance
                smallest_index = index
            elif distance < smallest_distance:
                smallest_distance = distance
                smallest_index = index
        
        image = cv2.imread(self.database.loc[smallest_index, 'image_path'])
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        plt.imshow(image)
        plt.show()
        
    