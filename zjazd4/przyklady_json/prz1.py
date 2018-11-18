import json

meble = ["krzesło, szafa, komoda, stół"]
print(type(meble))

meble_as_json = json.dumps(meble)
print(type(meble_as_json))


odczytanie_z_jsona_meble = json.loads(meble_as_json)
print(type(odczytanie_z_jsona_meble))
print(odczytanie_z_jsona_meble)

with open("meble.json", 'w')  as f:
    json.dump(meble, f)

with open("meble.json")  as f:
    meble = json.load(f)
    meble.append("taboret")
    print(meble)

with open("meble.json", 'w')  as f:
    json.dump(meble, f)