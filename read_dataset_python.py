import pandas as pd
import matplotlib.pyplot as plt

# SE IMPORTA EL ARICHO DE EXCEL A TRABJAR
df = pd.read_excel(
    r"C:\Users\aeaco\Desktop\Machine Learning Curso basico de Machine Learning y Python\Simple_Dashboard_Excel_BikeBuyers\Excel Project Dataset.xlsx", sheet_name='bike_buyers')


# se elimina duplicados
df_noD = df.drop_duplicates()

# Se cambian las columnas Marital Status and Gender to a full name intead of a letters to give more infomration


df1 = df_noD["Marital Status"] = df_noD["Marital Status"].replace(
    "S", "Single")


df2 = df_noD["Marital Status"] = df_noD["Marital Status"].replace(
    "M", "Married")

df3 = df_noD["Gender"] = df_noD["Gender"].replace(
    "F", "Female")


df4 = df_noD["Gender"] = df_noD["Gender"].replace(
    "M", "Masculine")

# Se da formato moneda a la columna de Income

df_noD["Income"] = df_noD["Income"].apply(lambda x: f"${x/1000:.1f}k")


# Se agrega una columna nueva (vacia) para agrupar las edades por rangos.

df_noD["Age_Range"] = None

# Se aplica la logica para parametrizar edades se setea directamente en df_noD para evitar eliminar las columnas restantes.
pd.DataFrame(df_noD, columns=["Age", "Age_Range"])
df_noD.loc[df.Age <= 35, "Age_Range"] = "Adulthood (Young)"
df_noD.loc[df.Age >= 36, "Age_Range"] = "Middle Age"
df_noD.loc[df.Age >= 56, "Age_Range"] = "Older Adulthood"

# Se trabaja sobre df_noD porque es el archivo que no tiene duplicados y sobre ese se sobre-esecriben los datos necesarios.

print(df_noD)

# El dataset limpio se pasa a Excel para visualizacion.

df_noD.to_excel(
    r"C:\Users\aeaco\Desktop\Machine Learning Curso basico de Machine Learning y Python\Simple_Dashboard_Excel_BikeBuyers\New_Clean_data.xlsx")


# Se genera una grafica para probar el dataset.

x_values = df_noD["Gender"]
y_values = df_noD["Purchased Bike"]
plt.bar(x_values, y_values)
plt.show()
plt.close('all')

#Prueba de git 
