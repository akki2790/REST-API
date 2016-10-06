#parsing a JSON file

#{
#   'pets':{
#           'name': 'Tony',
#           'species': 'Dog'
#           }
#}


import json
from pprint import pprint

f=open('pets.json', 'r')
pets=json.loads(f.read())
f.close()
pprint pets

