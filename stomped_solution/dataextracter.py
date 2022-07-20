import json
import base64
jsonFile = open('ordered.json', 'r')
values = json.load(jsonFile)
encoded_values=""
for i in values:
	encoded_values += (i['_source']["layers"]["icmp"]["data"]['data.data'])
print(base64.b64decode(bytes.fromhex(encoded_values).decode("ascii")))
jsonFile.close()
