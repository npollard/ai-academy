import json

states = []
with open(f'data/alds/errs.json', 'r', encoding='utf-8') as f:
    errs = json.loads(f.read())
    for err in errs:
        for state in errs[err]:
            states.append(state)

states = set(states)
for state in states:
    with open(f'data/alds/{state}.json', 'r', encoding='utf-8') as f2:
        alds = json.loads(f2.read())
        for year in alds:
            for grade in alds[year]:
                for subject in alds[year][grade]:
                    for ald in alds[year][grade][subject]:
                        if alds[year][grade][subject][ald] == 999:
                            print(f'{state} {year} {grade} {subject} {ald}')
                            alds[year][grade][subject][ald] = 0
    with open(f'data/alds/{state}.json', 'w', encoding='utf-8') as f:
        json.dump(alds, f, ensure_ascii=False, indent=4)

