from tkinter import *
import requests


def mostrar_respuesta(clima):
    nombre_ciudad = clima ['name']
    desc = clima["weather"][0]["descripcion"]
    temp = clima["main"]["temp"]
    
    ciudad["text"] = nombre_ciudad
    temperatura["text"] = temp
    descripcion["text"] = desc

def clima_JSON(ciudad):
    API_key="64ad54f12f6e2d035472caaedc5bb930"
    URL = "https://api.openweathermap.org/data/2.5/weather"
    parametros = {"APPID" : API_key, "q" : ciudad, "units": "metric"}
    response = requests.get(URL, params = parametros)
    clima = response.json()
    
    mostrar_respuesta(clima)
    print(clima['name'])
    print(clima['wather"][0]["description'])
    print(clima['main"]["temp'])

ventana= Tk()
ventana.geometry("350x550")


texto_ciudad = Entry(ventana, font =("Courier", 20, "normal"), justify ="center")
texto_ciudad.pack(padx = 30, pady =30)

obtener_clima= Button(ventana, text= "Obtener Clima", font =("Courrier", 20, "normal"), command =lambda: clima_JSON(texto_ciudad.get))
obtener_clima.pack()

ciudad = Label(font = ("Courier", 20, "normal"))
ciudad.pack(padx=20, pady=20)

temperatura = Label(font = ("Courier", 50, "normal"))
temperatura.pack(padx=10, pady=10)

descripcion = Label(font = ("Courier", 20, "normal"))
descripcion.pack(padx=10, pady=10)







ventana.mainloop()