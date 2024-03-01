from collections import defaultdict
import csv
import json
import requests

nested_dict = lambda: defaultdict(nested_dict)

states = [
    'AL',
    'AK',
    'AZ',
    'AR',
    'CA',
    'CO',
    'CT',
    'DE',
    'DC',
    'FL',
    'GA',
    'HI',
    'ID',
    'IL',
    'IN',
    'IA',
    'KS',
    'KY',
    'LA',
    'ME',
    'MD',
    'MA',
    'MI',
    'MN',
    'MS',
    'MO',
    'MT',
    'NE',
    'NV',
    'NH',
    'NJ',
    'NM',
    'NY',
    'NC',
    'ND',
    'OH',
    'OK',
    'OR',
    'PA',
    'RI',
    'SC',
    'SD',
    'TN',
    'TX',
    'UT',
    'VT',
    'VA',
    'WA',
    'WV',
    'WI',
    'WY'
]

errors = nested_dict()
def get_all_states_alds():
    for state in states:
    #for state in ['AK']:
        print(f'STATE: {state}')
        fetch_alds(state)

def fetch_alds(state):
    impact = nested_dict()
    grades = [4, 8]
    subjects = [('MATHEMATICS', 'MRPCM'), ('READING', 'RRPCM'), ('SCIENCE', 'SRPUV')]
    alds = ['BB', 'BA', 'PR', 'AD']
    for grade in grades:
        print(f'** GRADE {grade}')
        for subject in subjects:
            print(f'**** {subject[0]}')
            for ald in alds:
                print(f'****** {ald}')
                naep_url = 'https://www.nationsreportcard.gov/Dataservice/GetAdhocData.aspx?type=data&variable=TOTAL'
                naep_url += f'&subject={subject[0]}&grade={grade}&subscale={subject[1]}&jurisdiction={state}&stattype=ALD:{ald}'
                #print(naep_url)
                response = requests.get(naep_url)
                #print(response)
                if response.status_code != 200:
                    print("************** ERR!")
                    if not errors[response.status_code]:
                        errors[response.status_code] = []
                    errors[response.status_code].append(naep_url)
                else:
                    try:
                        result = response.json()["result"]
                    except ValueError:
                        if not errors["JSON EXCEPTION"]:
                            errors["JSON EXCEPTION"] = []
                        errors["JSON EXCEPTION"].append(naep_url)
                    for r in result:
                        #al = f'{state} {r["year"]}: GRADE {grade} {subject[0]} {ald}'
                        #print(al)
                        if r["errorFlag"]:
                            err = f'ERROR: {r["errorFlag"]},{"" if r["isStatDisplayable"] else " NOT"} DISPLAYABLE, VALUE = {r["value"]}'
                            #print(err)
                            errKey = f'{r["errorFlag"]} ({"" if r["isStatDisplayable"] else "NOT "}DISPLAYABLE)'
                            if not errors[errKey][state]:
                                errors[errKey][state] = []
                            errors[errKey][state].append(f'{r["year"]} GRADE {r["grade"]} {subject[0]} = {r["value"]}')
                        #else:
                            #print(r["value"])
                        impact[r["year"]][grade][subject[0]][ald] = r["value"]
    with open(f'data/alds/{state}.json', 'w', encoding='utf-8') as f:
        json.dump(impact, f, ensure_ascii=False, indent=4)

get_all_states_alds()
print(f'\n\n{json.dumps(errors, indent=2)}')
