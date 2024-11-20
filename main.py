import pypdfium2 as pdfium
from pathlib import Path
from PIL import Image
import img2pdf
import os
import shutil

carpeta_pdf = Path("pdfs")
carpeta_comprimidos = Path("comprimidos")
imagenes = []
imagenes_comprimidas = []
escala = 2
calidad = 40

"""
Extraer paginas como imagenes
"""
def extrarPaginas(nombre_pdf, nombre_pdf_sin_extension):
    pdf = pdfium.PdfDocument(f"{carpeta_pdf}/{nombre_pdf}")
    cantidad_paginas = len(pdf)
    for indice_pagina in range(cantidad_paginas):
        numero_pagina = indice_pagina+1
        nombre_imagen = f"{nombre_pdf_sin_extension}_{numero_pagina}.jpg"
        imagenes.append(nombre_imagen)
        print(f"Extrayendo página {numero_pagina} de {cantidad_paginas}")
        pagina = pdf.get_page(indice_pagina)
        imagen_para_pil = pagina.render(scale=escala).to_pil()
        imagen_para_pil.save(nombre_imagen)

#FIN DE LA FUNCION EXTAER PAGINAS


"""
Comprimir imágenes.
Entre menor calidad, menos peso del PDF resultante
"""
def comprimirImagenes():
    for nombre_imagen in imagenes:
        print(f"Comprimiendo {nombre_imagen}...")
        nombre_imagen_sin_extension = Path(nombre_imagen).stem
        nombre_imagen_salida = nombre_imagen_sin_extension + \
            "_comprimida" + nombre_imagen[nombre_imagen.rfind("."):]
        imagen = Image.open(nombre_imagen)
        imagen.save(nombre_imagen_salida, optimize=True, quality=calidad)
        imagenes_comprimidas.append(nombre_imagen_salida)

#FIN DE LA FUNCION COMPRIMIR IMAGENES

"""
Escribir imágenes en un nuevo PDF
"""
def crearPDFComprimido(nombre_pdf_comprimido):
    print("Creando PDF comprimido...")
    with open(nombre_pdf_comprimido, "wb") as documento:
        documento.write(img2pdf.convert(imagenes_comprimidas))

#FIN DE LA FUNCION CREAR PDF COMPRIMIDO

"""
Mover comprimidos a carpeta de comprimidos
"""
def moverPDFComprimido(nombre_pdf_comprimido):
    print(f"Moviendo PDF Comprimido..., {nombre_pdf_comprimido}")
    shutil.move(nombre_pdf_comprimido, f"{carpeta_comprimidos}/{nombre_pdf_comprimido}")

#FIN DE LA FUNCION MOVER PDF COMPRIMIDO

"""
Eliminar imágenes temporales
"""
def eliminarImagenes():
    print("Eliminando Imagenes...")
    for imagen in imagenes + imagenes_comprimidas:
        os.remove(imagen)

#FIN DE LA FUNCION ELIMINAR IMAGENES

for archivo in carpeta_pdf.iterdir():
    if archivo.is_file():
        print(f"{archivo.name}")
        nombre_pdf = archivo.name
        nombre_pdf_sin_extension = Path(nombre_pdf).stem
        nombre_pdf_comprimido = f"{nombre_pdf_sin_extension}.pdf"
        extrarPaginas(nombre_pdf, nombre_pdf_sin_extension)
        comprimirImagenes()
        crearPDFComprimido(nombre_pdf_comprimido)
        moverPDFComprimido(nombre_pdf_comprimido)
        eliminarImagenes()
