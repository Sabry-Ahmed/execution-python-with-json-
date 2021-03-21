import json

with open('s.json') as json_file:
    data = json.load(json_file)
    print('Name: ' + data['name'])
    print('Age dans JSON: ' + str(data['age']))
    print('La ville donnée: ' + data['ville'])
    print(data['notes'])
    notes = data["notes"]
    moy = 0
    for element in notes: 
        note = element['note']
        print(note)
        moy = moy + note
    print("moyenne = {:.2f}".format(moy/len(notes)))