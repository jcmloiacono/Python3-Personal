import json

productos = {"Mouse": 29.9, "Teclado": 119.9, "Audifonos": 35.9, "Monitor":290 }

print ("contenido de la variable :", productos )

print()

productos_json = json.dumps(productos)
print ("contenido de la variable Json :", productos_json )