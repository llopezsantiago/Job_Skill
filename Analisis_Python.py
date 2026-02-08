import pandas as pd
import numpy as np

# Creamos unos datos de prueba
data = {
    'Lenguaje': ['Python', 'R'],
    'Estado': ['Configurado', 'Configurado'],
    'Nivel': [10, 10]
}

df = pd.DataFrame(data)
print("¡Felicidades! Tu entorno de Ciencia de Datos está listo:")
print(df)