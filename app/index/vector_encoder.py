from sentence_transformers import SentenceTransformer

#Load the model
model = SentenceTransformer('sentence-transformers/multi-qa-MiniLM-L6-cos-v1')

#Encode query and documents
# doc_emb = model.encode(docs)

# print(doc_emb)