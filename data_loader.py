import pdfplumber
import os

def cargar_fragmentos(carpeta="./pdfs/"):
    fragmentos = []
    metadatos = []
    
    for archivo in os.listdir(carpeta):
        if archivo.endswith(".pdf"):
            ruta = os.path.join(carpeta, archivo)
            with pdfplumber.open(ruta) as pdf:
                for pagina in pdf.pages:
                    texto = pagina.extract_text() or ""
                    for parrafo in texto.split("\n"):
                        parrafo = parrafo.strip()
                        if parrafo:
                            fragmentos.append(parrafo)
                            metadatos.append(archivo)
    return fragmentos, metadatos
