import sys
sys.path.append('../vector_database')
import vector_database.embedding as emb
import os


if __name__ == '__main__':
    
    base_path = os.path.dirname(__file__)
    
 
    image_embedding = emb.ImageEmbedding(model_name_list=['resnet50'])
    image_embedding.imageVectorDatabaseBuild('D:/Pictures/PIC/2023')
    # image_embedding.imageVectorDatabaseLoad(os.path.join(base_path, 'image_vector_database.json'))
    image_embedding.imageQuery()