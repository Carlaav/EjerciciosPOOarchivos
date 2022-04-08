import pandas as pd


def examenes_y_asistencia(file):
    data = pd.read_csv(file, sep=";")
    print(data.info)
    data = data.sort_values(by=["Apellidos"])
    data = data.reset_index(drop=True)
    data = data.fillna(0)
    lista = []
    for i in range(len(data)):
        diccionario = {}
        diccionario["Apellidos"] = data["Apellidos"][i]
        diccionario["Nombre"] = data["Nombre"][i]
        diccionario["Parcial1"] = str(data["Parcial1"][i]).replace(",", ".")
        diccionario["Parcial2"] = str(data["Parcial2"][i]).replace(",", ".")
        diccionario["Ordinario1"] = str(data["Ordinario1"][i]).replace(",", ".")
        diccionario["Ordinario2"] = str(data["Ordinario2"][i]).replace(",", ".")
        diccionario["Practicas"] = str(data["Practicas"][i]).replace(",", ".")
        diccionario["Asistencia"] = str(data["Asistencia"][i]).replace(",", ".")
        lista.append(diccionario)
    return lista

def calcular_media(lista):
    media = 0
    for i in range(len(lista)):
        lista[i]["NotaMedia"] = float(lista[i]["Parcial1"]) * 0.3 + float(lista[i]["Parcial2"]) * 0.3 + float(lista[i]["Practicas"]) * 0.4
        media += lista[i]["NotaMedia"]

    return lista

def suspensos_y_aprobados(lista):
    aprobado = []
    suspenso = []
    for i in range(len(lista)):
        if float(lista[i]["Asistencia"].replace("%", "")) >= 75 and float(lista[i]["Parcial1"]) >= 4 and float(lista[i]["Parcial2"]) >= 4 and float(lista[i]["Practicas"]) >= 4 and float(lista[i]["NotaMedia"]) >= 5:
            nombre = lista[i]["Nombre"] + " " + lista[i]["Apellidos"]
            suspenso.append(nombre)
        else:
            nombre = lista[i]["Nombre"] + " " + lista[i]["Apellidos"]
            suspenso.append(nombre)
    return aprobado, suspenso

a = calcular_media(examenes_y_asistencia("EjerciciosPOOarchivos\calificaciones (1).csv"))
aprobados, suspensos = suspensos_y_aprobados(a)
print(aprobados)
print(suspensos)
