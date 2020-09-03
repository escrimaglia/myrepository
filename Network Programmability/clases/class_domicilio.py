from class_alumnos import Alumnos

class Domicilio(Alumnos):
    def __init__(self,id,nombre,notas,domicilio):
        super().__init__(id,nombre,notas)
        self.domicilio = domicilio

    def get_cp(self):
        domiclio_split = self.domicilio.split(",")
        for ele in domiclio_split:
            if "cp" in ele.lower():
                return ele
