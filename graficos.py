import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Sebastian\Desktop\prueba_tecnica\fifa_data\kl.csv", encoding='latin1')

print(df.head())
print(df.columns.tolist())

plt.figure(figsize=(5,4))
sns.histplot(df['Age'], bins=30, kde=True, color='blue')
plt.title('Distribución de Edades de Jugadores')
plt.xlabel('Edad')
plt.ylabel('Frecuencia')
plt.show()

plt.figure(figsize=(10,4))
sns.boxplot(x='Age', y='Overall', data=df, palette='Set3')
plt.title('Boxplot Compracion del Overall y la Edad de los Jugadores')
plt.xlabel('Edad')
plt.ylabel('Puntaje')
plt.show()

plt.figure(figsize=(5,4))
sns.barplot(x='Age', y='Overall', data=df)
plt.title('Barra de Puntajes de los Jugadores')
plt.xlabel('Edad')
plt.ylabel('Puntaje')
plt.show()