# Vector Database

## Demo code to use

```python
import vector_database.embedding as emb
    
image_embedding = emb.ImageEmbedding()
image_embedding.imageVectorDatabaseBuild('Your Picture Folder')
image_embedding.imageQuery()
```