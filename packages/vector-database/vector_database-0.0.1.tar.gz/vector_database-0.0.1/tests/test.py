import sys
sys.path.append('../vector_database')
import vector_database.embedding as emb
import os


if __name__ == '__main__':
    
    base_path = os.path.dirname(__file__)
    
 
    image_embedding = emb.ImageEmbedding()
    # image_embedding.imageVectorDatabaseBuild('D:/Pictures/PIC/2023/2023-07-26')
    image_embedding.imageVectorDatabaseLoad('./image_vector_database.json')
    image_embedding.imageQuery()