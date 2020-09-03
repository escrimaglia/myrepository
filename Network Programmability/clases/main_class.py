from class_domicilio import Domicilio

if __name__ == "__main__":
    obj_dom = Domicilio("123","Ed",[6,6,6],"Alto Villasol, Torre Catedral, Piso 3, Depto D, CP 5000, Cordoba")
    cp = obj_dom.get_cp()
    promedio = obj_dom.promedio()

    print (f"Alumno: {obj_dom.nombre}, ID: {obj_dom.id}, Domicilio: {obj_dom.domicilio}")
    print (f"Promedio: {promedio}")
    print (f"Código Postal: {cp}")
