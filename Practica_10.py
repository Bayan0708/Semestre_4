import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import linregress

# Definir los datos
x = input("Ingresa tu lista de variables independientes, si estás en Excel utiliza la función transponer y pégala aquí: ")
lista_de_numerosx = [float(numero) for numero in x.split('\t')]

y = input("Ingresa tu lista de variables dependientes, si estás en Excel utiliza la función transponer y pégala aquí: ")
lista_de_numerosy = [float(numero) for numero in y.split('\t')]

errores = input("Ingresa tu lista de barras de error, si estás en Excel utiliza la función transponer y pégala aquí: ")
lista_de_errores = [float(error) for error in errores.split('\t')]

datos = {'x': lista_de_numerosx, 'y': lista_de_numerosy, 'error': lista_de_errores}

# Definir los colores
color_puntos = 'black'
color_linea = 'red'

# Crear un DataFrame de Pandas con los datos
df = pd.DataFrame(datos)

# Graficar los datos con un gráfico de dispersión
plt.scatter(df['x'], df['y'], color=color_puntos)

# Calcular la línea de regresión lineal
slope, intercept, r_value, p_value, std_err = linregress(df['x'], df['y'])
lineal = slope * df['x'] + intercept

# Calcular el valor R^2
r_squared = r_value**2

# Agregar las líneas de regresión al gráfico
plt.plot(df['x'], lineal, color=color_linea, label=f'Ajuste lineal (R^2 = {r_squared:.3f})')

# Agregar etiquetas y un título al gráfico (en negritas)
plt.xlabel('x', fontweight='bold')
plt.ylabel('y', fontweight='bold')
plt.title('Gráfico de ajustes lineal y logarítmico\nR^2 debajo de la ecuación lineal', fontweight='bold')

# Agregar una leyenda al gráfico
plt.legend()

# Agregar una cuadrícula al gráfico
plt.grid(True)

# Graficar los datos con barras de error (con formato de T en las esquinas)
plt.errorbar(df['x'], df['y'], yerr=df['error'], fmt='o', color=color_puntos, capsize=5, elinewidth=1, markeredgewidth=1)

# Agregar el texto de las ecuaciones de los ajustes y el valor R^2 debajo de la ecuación lineal
plt.text(max(df['x']) + 0.1, max(df['y']) - 2, f'Ecuación del ajuste lineal:\n y = {round(slope, 2)}x + {round(intercept, 2)}\nR^2 = {r_squared:.3f}', fontsize=10)

# Mostrar el gráfico
plt.show()