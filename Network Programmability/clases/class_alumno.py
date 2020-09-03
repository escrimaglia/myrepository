class Alumnos:
def __init__(self,id,nombre,notas):
    self.id = id
    self.nombre = nombre
    self.notas = notas

def promedio(self):
    suma = 0
    for nota in self.notas:
        suma = suma + nota
    return suma / len(self.notas)
