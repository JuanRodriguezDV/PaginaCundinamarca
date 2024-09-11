import pandas as pd
import matplotlib.pyplot as plt
from pyscript import document
from pyodide.http import open_url


def mostrar(event):
    nombre_archivo = document.querySelector("#nombre").value
    url = open_url(nombre_archivo)
    df = pd.read_csv(url, sep=";")
    total_produccion = df["Produccion"].sum()
    promedio_clima = round(df["Clima"].mean(), 2)
    clima_min = df["Clima"].min()
    clima_max = df["Clima"].max()
    # print(f" El total de la produccion es: {total_produccion}")
    # print(f"El promedio del clima es: {promedio_clima}")
    # print(f"El clima minimo es: {clima_min}")
    # print(f"El clima maximo es: {clima_max}")

    cantidad = 0
    cantidad2 = 0
    cantidad3 = 0
    cantidad4 = 0
    cantidad5 = 0
    for i in df["Especie"]:
        match i:
            case "Hierba":
                cantidad += 1
            case "Arboles nativos":
                cantidad2 += 1
            case "Arbol invasor":
                cantidad3 += 1
            case "Frailejon":
                cantidad4 += 1
            case "Orquidea":
                cantidad5 += 1
    # print(f"La cantidad de hierbas es: {cantidad}")
    # print(f"La cantidad de arboles nativos es: {cantidad2}")
    # print(f"La cantidad de arboles invasores es: {cantidad3}")
    # print(f"La cantidad de frailejones es: {cantidad4}")
    # print(f"La cantidad de orquideas es: {cantidad5}")

    # Graficando los datos
    document.querySelector("#Total").innerText = "El total de la produccion es: " + str(
        total_produccion
    )
    document.querySelector("#PromClima").innerText = (
        "El promedio del clima es:  " + str(promedio_clima)
    )
    document.querySelector("#ClimMin").innerText = "El clima minimo es: " + str(
        clima_min
    )
    document.querySelector("#ClimMax").innerText = "El clima maximo es: " + str(
        clima_max
    )
    document.querySelector("#THierbas").innerText = "La cantidad de hierbas es: " + str(
        cantidad
    )
    document.querySelector("#TANativos").innerText = (
        "La cantidad de arboles nativos es: " + str(cantidad2)
    )
    document.querySelector("#TAInvasores").innerText = (
        "La cantidad de arboles invasores es: " + str(cantidad3)
    )
    document.querySelector("#TFrailejones").innerText = (
        "La cantidad de frailejones es " + str(cantidad4)
    )
    document.querySelector("#TOrquideas").innerText = (
        "La cantidad de orquideas es: " + str(cantidad5)
    )

    plt.figure(figsize=(5, 3))
    df.plot(x="Especie", y="Produccion", kind="bar")
    contenido = document.querySelector("#Contenido")
    plt.title("Expecie Vs Produccion")
    contenido.value = plt.show()

    plt.figure(figsize=(5, 3))
    df.plot(x="Planta", y="Clima", kind="area")
    grafico = document.querySelector("#Grafico")
    plt.title("PLantas Vs Clima")
    grafico = plt.show()
