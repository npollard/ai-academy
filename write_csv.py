from collections import defaultdict
import csv
import json

nested_dict = lambda: defaultdict(nested_dict)

cc_states = [
    'AR',
    'CA',
    'CO',
    'CT',
    'DE',
    'GA',
    'HI',
    'ID',
    'IL',
    'IA',
    'KS',
    'KY',
    'LA',
    'ME',
    'MD',
    'MA',
    'MI',
    'MS',
    'MT',
    'NV',
    'NH',
    'NM',
    'NY',
    'ND',
    'OH',
    'OR',
    'PA',
    'RI',
    'SD',
    'VT',
    'WA',
    'WV',
    'WI',
    'WY'
]

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

states_long = [
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Dist. of Col.',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming',
]

party_map = {
    'Democratic': 'D',
    'Republican': 'R'
}

def get_pres():
    politics = nested_dict()
    with open(f'data/politics/input/presidents.csv', encoding='utf-8-sig') as presidents_file:
        reader = csv.reader(presidents_file)
        header = next(reader)
        for line in reader:
            elec_year = int(line[0].split(' ')[0])
            if elec_year < 1988:
                continue
            state = states[states_long.index(line[1])]
            party = party_map[line[15]]
            for year in range(elec_year, elec_year + 4):
                print(f'{year} {state} {party}')
                politics[state][int(year)]["PRES"] = party
    return politics

def get_govs(politics):
    for state in states:
        with open(f'data/politics/govs/{state}.json', 'r') as govs_file:
            govs = json.loads(govs_file.read())
            for year in govs:
                politics[state][int(year)]["GOV"] = govs[year]
    return politics

def get_politics():
    politics = get_pres()
    return get_govs(politics)

def get_years_since_ald_set(year):
    if (year < 2015):
        return year - 2010
    else:
        return year - 2015

def write_csv(politics):
    with open('data/cc_state_data.csv', 'w') as output_csv:
        output_csv.write('state,year,years_since_ald_set,pres,gov,grade,subject,ald,value\n')
        for state in cc_states:
            print(state)
            with open(f'data/alds/{state}.json', 'r') as alds_file:
                alds = json.loads(alds_file.read())
                for year in alds:
                    if int(year) < 2010:
                        continue
                    years_since_ald_set = get_years_since_ald_set(int(year))
                    pres = politics[state][int(year)]["PRES"] if politics[state][int(year)]["PRES"] else '?'
                    gov = politics[state][int(year)]["GOV"] if politics[state][int(year)]["GOV"] else '?'
                    print(f'PRES: {pres}, GOV: {gov}')
                    for grade in alds[year]:
                        for subject in ['MATHEMATICS', 'READING']:
                            for ald in alds[year][grade][subject]:
                                value = alds[year][grade][subject][ald]
                                output_csv.write(f'{state},{year},{years_since_ald_set},{pres},{gov},{grade},{subject},{ald},{value}\n')

politics = get_politics()
write_csv(politics)
