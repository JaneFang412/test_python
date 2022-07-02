# from openpyxl import Workbook
# import json
import yaml

print(yaml.load("""
- Hesperiidae
- Papilionidae
- Apatelodidae
- Epipleidae
""", Loader=yaml.CLoader))

print(yaml.load("""
a:1
""", Loader=yaml.FullLoader))

print(yaml.load(open("demo.yml"), Loader=yaml.FullLoader))

print(yaml.dump({'a': [1, 2]}))

with open("demo2.yml", "w") as f:
    yaml.dump(data={'a': [1,2]}, stream=f)