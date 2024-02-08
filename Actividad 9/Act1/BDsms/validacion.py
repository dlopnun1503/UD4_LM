import json
from jsonschema import validate

# Definir el esquema
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "libreria":{
        "libro":{
            "autores":{
                "autor":{
                "apellido1":{
                "type":"string"
            }, "apellido2":{
                "type":"string"
            }, "nombre":{
                "type":"string"
            }, "genero":{
                "type":"string"
            }
        }
            }, "titulo":{
        "type":"string"
    }, "CodigoLibro":{
        "type":"string"
}, "editorial":{
    "type":"string"
}, "edicion":{
    "type":"string"
}, "FechaPublicacion":{
    "dia":{
        "type":"integer"
    }, "mes":{
           "type":"integer"
    }, "anio":{
        "type":"integer"
    }
}, "ISBN":{
    "type":"string"
}, "numPaginas":{
    "type":"integer"
},"required":["apellido1", "apellido2", "nombre", "genero", "titulo", "CodigoLibro", "editorial", "edicion", "dia", "mes", "anio", "ISBN", "numPaginas"]

}
}
}


# Archivo JSON a validar
archivo_json = '''
{
    "libreria": {
      "libro": [
        {
          "autores": {
            "autor": {
              "apellido1": "Cervantes",
              "apellido2": "Saavedra",
              "nombre": "Miguel",
              "genero": "Hombre"
            }
          },
          "titulo": "El ingenioso hidalgo Don Quijote De La Mancha",
          "CodigoLibro": 1,
          "editorial": "Catedra",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": 16,
            "mes": "Enero",
            "anio": 1605
          },
          "ISBN": 9788408061052,
          "numPaginas": 1560
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Rojas",
              "apellido2": "",
              "nombre": "Fernando",
              "genero": "Hombre"
            }
          },
          "titulo": "La Celestina",
          "CodigoLibro": 2,
          "editorial": "La Mar De Fácil",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1499
          },
          "ISBN": 9781589771260,
          "numPaginas": 244
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Hurtado",
              "apellido2": "Mendoza",
              "nombre": "Diego",
              "genero": "Hombre"
            }
          },
          "titulo": "El Lazarillo De Tormes",
          "CodigoLibro": 3,
          "editorial": "Juventud",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1554
          },
          "ISBN": 9788497406826,
          "numPaginas": 128
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Lope de Vega",
              "apellido2": "Carpio",
              "nombre": "Félix",
              "genero": "Hombre"
            }
          },
          "titulo": "Fuenteovejuna",
          "CodigoLibro": 4,
          "editorial": "Austral",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1619
          },
          "ISBN": 9780828870412,
          "numPaginas": 94
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Alas",
              "apellido2": "",
              "nombre": "Leopoldo",
              "genero": "Hombre"
            }
          },
          "titulo": "La Regenta",
          "CodigoLibro": 5,
          "editorial": "Austral",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1884
          },
          "ISBN": 9788423916672,
          "numPaginas": 944
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Zorrilla",
              "apellido2": "",
              "nombre": "Jose",
              "genero": "Hombre"
            }
          },
          "titulo": "Don Juan Tenorio",
          "CodigoLibro": 6,
          "editorial": "Catedra",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": 28,
            "mes": "Marzo",
            "anio": 1844
          },
          "ISBN": 9788469848517,
          "numPaginas": 184
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Pardo",
              "apellido2": "Bazán",
              "nombre": "Emilia",
              "genero": "Mujer"
            }
          },
          "titulo": "Los Pazos de Ulloa",
          "CodigoLibro": 7,
          "editorial": "La Mar De Fácil",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1886
          },
          "ISBN": 9788419772176,
          "numPaginas": 472
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Calderón",
              "apellido2": "De la Barca",
              "nombre": "Pedro",
              "genero": "Hombre"
            }
          },
          "titulo": "La vida es un sueño",
          "CodigoLibro": 8,
          "editorial": "Catedra",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": "Desconocido",
            "mes": "Desconocido",
            "anio": 1635
          },
          "ISBN": 9788420725895,
          "numPaginas": 178
        },
        {
          "autores": {
            "autor": {
              "apellido1": "Valle-Inclán",
              "apellido2": "",
              "nombre": "Ramón María",
              "genero": "Hombre"
            }
          },
          "titulo": "Luces de Bohemia",
          "CodigoLibro": 9,
          "editorial": "Austral",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": 23,
            "mes": "Octubre",
            "anio": 1923
          },
          "ISBN": 9788423938735,
          "numPaginas": 295
        },
        {
          "autores": {
            "autor": {
              "apellido1": "García",
              "apellido2": "Lorca",
              "nombre": "Federico",
              "genero": "Hombre"
            }
          },
          "titulo": "La Casa de Bernarda Alba",
          "CodigoLibro": 10,
          "editorial": "Catedra",
          "edicion": "Original",
          "FechaPublicacion": {
            "dia": 8,
            "mes": "Marzo",
            "anio": 1945
          },
          "ISBN": 9788469833070,
          "numPaginas": 152
        }
      ]
    }
  }
'''

# Cargar el archivo JSON
datos_json = json.loads(archivo_json)

# Validar contra el esquema
validate(instance=datos_json, schema=schema)

#Este script de Python utiliza la biblioteca jsonschema para cargar el esquema y los datos JSON, 
#y luego realiza la validación. Si el archivo JSON cumple con el esquema, no se producirá ninguna excepción. 
#En caso contrario, se lanzará una excepción indicando la razón de la invalidación.