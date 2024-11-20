import hmac
import hashlib
import json
from pathlib import Path

from urllib.parse import unquote

# @API_SECRET, clave secreta suministrada mediante correo electronico enviado a cada entidad
API_SECRET = '0m76b@nx6=8h_=n)p3p-!pnl0+((jcuqh245ed=whwl)kq!jc0'

api_key_bytes= bytes(API_SECRET, 'utf-8')
data_api = []
data_docs_api = []
carpeta_signatureJson = Path("signaturesJSON")
carpeta_dataJson = Path("fileJSON")


# *************************************************************************************
# @data, en esta variable va el cuerpo del mensaje enviado en la peticion,
# este valor se debe modificar dependiendo el servicio que se desea consumir.
# los servicios que requieren esta modificacion son de tipo PUT y POST
# *************************************************************
# VALORES DE DATA PARA ENVIAR ARCHIVOS MTO 3
"""
"codigo_queja":"1426202410281345341860",
"type":"pdf"
"""
#**************************************************************
# VALORES DE DATA PARA ENVIAR CASO ACTUALIZADO
"""
   "codigo_queja":"1426202410281345341860",
   "estado_cod":4,
   "documentacion_rta_final":"true",
   "anexo_queja":"true",
   "fecha_cierre":"2024-10-29T11:09:00",
   "fecha_actualizacion":"2024-10-29T11:09:00",
   "canal_cod":14,
   "producto_cod":127,
   "macro_motivo_cod":108,
   "marcacion":None,
   "aceptacion_queja":None,
   "desistimiento_queja":2,
   "queja_expres":2,
   "a_favor_de":3,
   "producto_digital":2,
   "rectificacion_queja":None,
   "prorroga_queja":None,
   "admision":9,
   "sexo":1,
   "lgbtiq":2,
   "condicion_especial":98,
   "tutela":2,
   "ente_control":99
   """
# *************************************************************************************
jsonData = [
  {
   "codigo_queja": "1426202410070844300737",
   "sexo": 2,
   "lgbtiq": 2,
   "condicion_especial": 98,
   "canal_cod": 5,
   "producto_cod": 124,
   "macro_motivo_cod": 916,
   "estado_cod": 4,
   "fecha_actualizacion": "2024-10-28T13:08:00",
   "producto_digital": 2,
   "a_favor_de": 3,
   "aceptacion_queja": None,
   "rectificacion_queja": None,
   "desistimiento_queja": 2,
   "prorroga_queja": None,
   "admision": 9,
   "documentacion_rta_final": "true",
   "anexo_queja": "true",
   "fecha_cierre": "2024-10-28T13:08:00",
   "tutela": 2,
   "ente_control": 99,
   "marcacion": 7,
   "queja_expres": 2
 },
 {
   "codigo_queja": "1426202410081250130737",
   "sexo": 10,
   "lgbtiq": 2,
   "condicion_especial": 98,
   "canal_cod": 5,
   "producto_cod": 124,
   "macro_motivo_cod": 916,
   "estado_cod": 4,
   "fecha_actualizacion": "2024-10-24T08:02:00",
   "producto_digital": 2,
   "a_favor_de": 3,
   "aceptacion_queja": None,
   "rectificacion_queja": None,
   "desistimiento_queja": 2,
   "prorroga_queja": None,
   "admision": 9,
   "documentacion_rta_final": "true",
   "anexo_queja": "true",
   "fecha_cierre": "2024-10-24T08:02:00",
   "tutela": 2,
   "ente_control": 99,
   "marcacion": None,
   "queja_expres": 2
 },
 {
   "codigo_queja": "1426202410081746230737",
   "sexo": 10,
   "lgbtiq": 2,
   "condicion_especial": 98,
   "canal_cod": 5,
   "producto_cod": 124,
   "macro_motivo_cod": 916,
   "estado_cod": 4,
   "fecha_actualizacion": "2024-10-24T15:48:00",
   "producto_digital": 2,
   "a_favor_de": 1,
   "aceptacion_queja": None,
   "rectificacion_queja": None,
   "desistimiento_queja": 2,
   "prorroga_queja": None,
   "admision": 9,
   "documentacion_rta_final": "true",
   "anexo_queja": "true",
   "fecha_cierre": "2024-10-24T15:48:00",
   "tutela": 2,
   "ente_control": 99,
   "marcacion": None,
   "queja_expres": 2
 },
 {
   "codigo_queja": "1426202410090835030737",
   "sexo": 10,
   "lgbtiq": 2,
   "condicion_especial": 98,
   "canal_cod": 5,
   "producto_cod": 124,
   "macro_motivo_cod": 916,
   "estado_cod": 4,
   "fecha_actualizacion": "2024-10-24T11:40:00",
   "producto_digital": 2,
   "a_favor_de": 3,
   "aceptacion_queja": None,
   "rectificacion_queja": None,
   "desistimiento_queja": 2,
   "prorroga_queja": None,
   "admision": 9,
   "documentacion_rta_final": "true",
   "anexo_queja": "true",
   "fecha_cierre": "2024-10-24T11:40:00",
   "tutela": 2,
   "ente_control": 99,
   "marcacion": None,
   "queja_expres": 2
 },
 {
   "codigo_queja": "1426202410101122180737",
   "sexo": 10,
   "lgbtiq": 2,
   "condicion_especial": 98,
   "canal_cod": 5,
   "producto_cod": 124,
   "macro_motivo_cod": 916,
   "estado_cod": 4,
   "fecha_actualizacion": "2024-10-24T08:29:00",
   "producto_digital": 2,
   "a_favor_de": 3,
   "aceptacion_queja": None,
   "rectificacion_queja": None,
   "desistimiento_queja": 2,
   "prorroga_queja": None,
   "admision": 9,
   "documentacion_rta_final": "true",
   "anexo_queja": "true",
   "fecha_cierre": "2024-10-24T08:29:00",
   "tutela": 2,
   "ente_control": 99,
   "marcacion": None,
   "queja_expres": 2
 },
 {
   "codigo_queja": "1426202410101135370737",
   "sexo": 10,
   "lgbtiq": 2,
   "condicion_especial": 98,
   "canal_cod": 5,
   "producto_cod": 124,
   "macro_motivo_cod": 916,
   "estado_cod": 4,
   "fecha_actualizacion": "2024-10-24T11:34:00",
   "producto_digital": 2,
   "a_favor_de": 3,
   "aceptacion_queja": None,
   "rectificacion_queja": None,
   "desistimiento_queja": 2,
   "prorroga_queja": None,
   "admision": 9,
   "documentacion_rta_final": "true",
   "anexo_queja": "true",
   "fecha_cierre": "2024-10-24T11:34:00",
   "tutela": 2,
   "ente_control": 99,
   "marcacion": None,
   "queja_expres": 2
 }
 ]

data = {
    "codigo_queja":"1426202410070844300737",
    "type":"pdf"
}

# ***********************************************************************************
# se debe modificar la variable @path de acuerdo al servicio que se desea consumir,
# los servicios que requieren esta modificacion son de tipo GET o DELETE
# ***********************************************************************************
path = '' # inicialización requerida para consumir el servicio <<get Queja>>


def generate_keys(data):
  data_str = json.dumps(data, ensure_ascii=False)
  print('data_str: ', data_str)
  signature = hmac.new(api_key_bytes,msg=data_str.encode('utf-8'),digestmod=hashlib.sha256).hexdigest().upper()
  signature_path = hmac.new(api_key_bytes,msg=unquote(path).encode('utf-8'),digestmod=hashlib.sha256).hexdigest().upper()
  # se utiliza para peticiones POST y PUT
  print(f'Data - {signature}')
  data_api.append({
      "id": data["codigo_queja"],
      "signature": signature,
      "data": data
  })

  # se utiliza para peticiones GET y DELETE
  print(f'URL - {signature_path}')
    
def generate_fileSigns(nameFoder, nameFileResults, content):
  with open(f"{nameFoder}/{nameFileResults}", "w") as archivo:
      json.dump(content, archivo, indent=4)

#for queja in jsonData:
 #   generate_keys(queja)

#generate_fileSigns()

def get_content_file(name_file_json):
  with open(f"{carpeta_dataJson}/{name_file_json}", "r") as archivo:
    return json.load(archivo)

def generate_dataDocs_json(name_file_json):
  content = get_content_file(name_file_json)
  for queja in content:
    data_docs_api.append(
      {
        "codigo_queja": queja["codigo_queja"],
        "type":"pdf"
      }
    )
  generate_fileSigns(carpeta_dataJson, "dataDocs.json", data_docs_api)


def run_files_JSON(name_file_json):
  content = get_content_file(name_file_json)
  for queja in content:
    generate_keys(queja)


generate_dataDocs_json("data.json")
run_files_JSON("data.json")
generate_fileSigns(carpeta_signatureJson, "signaturesCases.json", data_api)

data_api = []
run_files_JSON("dataDocs.json")
generate_fileSigns(carpeta_signatureJson, "signaturesDocs.json", data_api)