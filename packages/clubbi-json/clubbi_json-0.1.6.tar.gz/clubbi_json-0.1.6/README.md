![Clubbi-logo](https://user-images.githubusercontent.com/32624827/160703813-03249a14-9f4f-46a4-a7c1-f46686e97459.png)

# clubbi_json
Este repositório tem como finalidade facilitar a serialização e desserialização de JSON, oferecendo suporte ao tratamento de dados personalizado e integração com bibliotecas JSON.

## Requisitos

- [Python 3.9](https://www.python.org/downloads/release/python-390/)
- [pipenv](https://pipenv.pypa.io/en/latest/)


## Funcionalidades
### DUMPS - Serializa objetos Python em formato JSON.
`dumps`(data, /, pretty=False, sort_keys=False, non_str_keys=True, default=_serialize_default) -> str:

#### Parâmetros:
- `data`: Objeto a ser serializado.
- `pretty` (opcional): Se True, a saída JSON será formatada com indentação.
- `sort_keys` (opcional): Se True, as chaves do JSON serão ordenadas.
- `non_str_keys` (opcional): Se True, as chaves não-strings são permitidas no JSON.
- `default` (opcional): Função de serialização personalizada para tipos não nativos.

Retorno:
str: JSON serializado.

### LOADS - Desserializa objetos JSON em objetos Python.
`loads`(data: str) -> Union[str, dict, list, int, float]:

#### Parâmetros:
- `data`: JSON a ser desserializado.

Retorno:
Union[str, dict, list, int, float]: Objeto Python desserializado.

```python
# Desserialização
from clubbi-json import dumps, loads

data = {'name': 'John', 'age': 30, 'is_active': False}
json_string = dumps(data, pretty=True)
data_deserialized = loads(json_string)

# Serialização 
from my_json_module import dumps, loads

data = {'name': 'John', 'age': 30, 'is_active': False}
json_string = dumps(data, pretty=True)
```