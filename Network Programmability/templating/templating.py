#Uso de Template Jinja2 para generar configuracion Catalyst3500 - NEP@L
#Ed Scrimaglia

from jinja2 import Environment, FileSystemLoader
import yaml

def loadDatos():
	with open("modelo.yaml") as f:
		modelo = yaml.load(f, Loader=yaml.FullLoader)
	return modelo

def mapTemplate(_datos) :
	dir_templates = FileSystemLoader('./')
	env = Environment(loader=dir_templates)
	template = env.get_template('script.j2')
	switch_conf = template.render(devices=_datos)
	return switch_conf

def write_file(_configuracion,_file_name):
	with open(_file_name,"w") as file:
		file.write(_configuracion)

if __name__ == "__main__":
	datos = loadDatos()
	configuracion = mapTemplate(datos)
	file_name = "template.cfg"
	write_file(configuracion, file_name)

