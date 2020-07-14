from tkinter import *
import requests


def clima(ciudad):
    API_key="64ad54f12f6e2d035472caaedc5bb930"
    URL = "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={your api key}"
    parametros = {"APPID" : API_key, "q": ciudad, "units": "metric"}
    response = requests.get(URL, params=parametros)
    print(response.json())
    
ventana= Tk()
ventana.geometry("350x550")


texto_ciudad = Entry(ventana, font =("Courier", 20, "normal"), justify ="center")
texto_ciudad.pack(padx = 30, pady =30)

obtener_clima= Button(ventana, text= "Obtener Clima", font =("Courrier", 20, "normal"), command =lambda: clima())
obtener_clima.pack()

mostrar_clima = Label(text = "weather", font =("Courier", 20, "normal"))
mostrar_clima.pack(padx=30, pady=30)









ventana.mainloop()