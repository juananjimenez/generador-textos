import pandas as pd
import random

# Función para combinar textos y titulares H2
def combinar_textos(dataset, num_textos_combinar=3):
    # Convertir la columna 'h2' a una lista
    h2_lista = dataset['Ladillo'].tolist()

    # Seleccionar aleatoriamente num_textos_combinar textos del dataset
    textos_seleccionados = random.sample(h2_lista, num_textos_combinar)

    # Crear el artículo combinado
    articulo_combinado = ""
    for h2 in textos_seleccionados:
        # Obtener el contenido correspondiente al H2
        contenido = dataset.loc[dataset['Ladillo'] == h2, 'Texto'].values[0]
        articulo_combinado += f"## {h2}\n{contenido}\n\n"

    return articulo_combinado

# Subir el dataset (asegúrate de tener un archivo CSV con columnas 'h2' y 'contenido')
ruta_dataset = "articulos.csv"
dataset = pd.read_csv(ruta_dataset)

# Crear un artículo combinando 3 textos
articulo_combinado = combinar_textos(dataset, num_textos_combinar=3)

# Guardar en un archivo de texto
with open("articulo_combinado.txt", "w", encoding="utf-8") as file:
    file.write(articulo_combinado)

# Imprimir el artículo combinado
print("Artículo Combinado:")
print(articulo_combinado)