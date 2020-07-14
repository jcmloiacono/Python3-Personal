def incrementar(p):
    p.edad += 1
    return p


personas = [
    persona("Juan", 35),
    persona("Marta", 16),
    persona("Manuel", 78),
    persona("Eduardo", 12)
]

personas = map(lambda p: persona(p.nombre, p.edad+1), personas)

for persona in personas:
    print(persona)