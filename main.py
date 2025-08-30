# main.py
from data_loader import cargar_fragmentos
from embeddings_generator import generar_embeddings
from similarity_search import buscar_fragmentos

# 1. Cargar PDFs
fragmentos, metadatos = cargar_fragmentos("./pdfs/")
print(f"Se cargaron {len(fragmentos)} fragmentos de {len(set(metadatos))} PDFs.")

# 2. Generar embeddings
embeddings, model = generar_embeddings(fragmentos)

# 3. Interfaz básica
while True:
    pregunta = input("Pregunta (o 'salir'): ")
    if pregunta.lower() == 'salir':
        break
    resultados = buscar_fragmentos(pregunta, fragmentos, metadatos, embeddings, model)
    
    for r in resultados:
        print(f"PDF: {r['pdf']} | Similitud: {r['similitud']:.2f}")
        print(f"{r['fragmento']}\n{'-'*50}")