import json

ar = []

with open('forbidden_words.txt', encoding='utf-8') as r:
    for i in r:
        n = i.lower().split('\n')[0]
        if n != '':
            ar.append(n)

with open('forbidden_words.json', 'w', encoding='utf-8') as e:
    #writing data in json file
    json.dump(ar, e)
