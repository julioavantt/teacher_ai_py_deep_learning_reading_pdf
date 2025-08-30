from sentence_transformers import SentenceTransformer

def generar_embeddings(fragmentos):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(fragmentos)
    return embeddings, model