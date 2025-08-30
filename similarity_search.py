from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def buscar_fragmentos(pregunta, fragmentos, metadatos, embeddings, model, top_k=3):
    pregunta_vec = model.encode([pregunta])
    similitudes = cosine_similarity(pregunta_vec, embeddings)[0]
    
    indices = np.argsort(similitudes)[-top_k:][::-1]
    
    resultados = []
    for idx in indices:
        resultados.append({
            "fragmento": fragmentos[idx],
            "pdf": metadatos[idx],
            "similitud": similitudes[idx]
        })
    return resultados