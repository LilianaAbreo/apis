import requests
import json

#Requerimiento 1

def repuesta_api(type, url, data = {}):
    return json.loads(requests.request(type, url=url, data=data).text)

url = "https://reqres.in/api/users"

#Pedir datos
users_data = repuesta_api('GET', url)['data']  #data es la clave del diccionario
print(users_data)

#Requerimiento 2 Creando datos con POST

dato_enviar = {
  "name": "Ignacio",
  "job": "Profesor"
}
#Crear y enviar datos para la api
created_users = repuesta_api('POST', url,data= dato_enviar)
print("Creando datos con POST")
print(created_users)

#Requerimiento 3 Actualizando datos con PUT
#dato para actualizar el api
url_actualizar = "https://reqres.in/api/users/2"

dato_actualizar= {
    "name": "morpheus",
    "residence": "zion"
} 
#Crear y enviar dato para actualizar o editar
update_users= repuesta_api('PUT', url_actualizar,data= dato_actualizar)
print("Actualizando datos con PUT")
print(update_users)

#Requerimiento 4

def eliminar_dato_api(url, id):
    url_eliminar = url + f'/id'
    print(url_eliminar)
    return requests.request('DELETE', url_eliminar)
#para sacar los id
id_usuario = [indice_id['id'] for indice_id in users_data if indice_id['first_name']== 'Tracey']
print(id_usuario)

invocando_para_eliminar = eliminar_dato_api(url,id_usuario)
print(invocando_para_eliminar)



   