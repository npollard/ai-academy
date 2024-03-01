import pandas as pd
from pandas.api.types import CategoricalDtype
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def transform_data(df, has_politics, has_states, has_years, has_years_since):
    df = one_hot(df, has_states)
    if has_politics:
        df = one_hot_politics(df)
    else:
        df = df.drop('pres', axis=1)
        df = df.drop('gov', axis=1)
    if not has_years:
        df = df.drop('year', axis=1)
    if not has_years_since:
        df = df.drop('years_since_ald_set', axis=1)

    return df

def train_test(df):
    x = df.drop('value', axis=1)
    y = df['value']

    x_train, x_test, y_train, y_test = train_test_split(x, y) #, random_state=42)
    return (x_train, x_test, y_train, y_test)

def one_hot(df, has_states):
    cat_headers = ['subject', 'ald']
    if has_states:
        cat_headers.append('state')
    else:
        df = df.drop('state', axis=1)
    for header in cat_headers:
        dummies = pd.get_dummies(df[header])
        df = df.drop(header, axis=1)
        df = df.join(dummies)

    return df

def one_hot_politics(df):
    pres_dummies = pd.get_dummies(df['pres'])
    gov_dummies = pd.get_dummies(df['gov'])
    df = df.drop('pres', axis=1)
    df = df.drop('gov', axis=1)
    df = df.join(pres_dummies, rsuffix='_pres')
    df = df.join(gov_dummies, rsuffix='_gov')

    return df


def categorize(df):
    ald_cat = CategoricalDtype(categories=['BB', 'BA', 'PR', 'AD'], ordered=True)
    df['ald'] = df['ald'].astype(ald_cat)
    
    cat_headers = ['state', 'pres', 'gov', 'grade', 'subject']
    for header in cat_headers:
        df[header] = df[header].astype('category')

    return df

def ml_combinations(df, algorithm):
    machine_learn(df, algorithm, False, True, True, False)
    machine_learn(df, algorithm, True, True, True, False)
    machine_learn(df, algorithm, False, True, True, True)
    machine_learn(df, algorithm, True, True, True, True)

    machine_learn(df, algorithm, False, False, True, False)
    machine_learn(df, algorithm, True, False, True, False)
    machine_learn(df, algorithm, False, False, True, True)
    machine_learn(df, algorithm, True, False, True, True)

    machine_learn(df, algorithm, False, True, False, False)
    machine_learn(df, algorithm, True, True, False, False)
    machine_learn(df, algorithm, False, True, False, True)
    machine_learn(df, algorithm, True, True, False, True)

    machine_learn(df, algorithm, False, False, False, False)
    machine_learn(df, algorithm, True, False, False, False)
    machine_learn(df, algorithm, False, False, False, True)
    machine_learn(df, algorithm, True, False, False, True)

    #machine_learn(df, algorithm, False, True, False, False)
    #machine_learn(df, algorithm, True, True, False, False)
    #machine_learn(df, algorithm, False, True, False, True)
    #machine_learn(df, algorithm, True, True, False, True)


def machine_learn(df, algorithm, has_politics, has_states, has_years, has_years_since):
    df = transform_data(df, has_politics, has_states, has_years, has_years_since)

    iterations = 10
    test_sum = 0
    for i in range(iterations):
        x_train, x_test, y_train, y_test = train_test(df)
        model = algorithm.fit(x_train, y_train)
        predictions = model.predict(x_test)
        test_sum += model.score(x_test, y_test)
    print_results(test_sum/iterations, algorithm, has_politics, has_states, has_years, has_years_since)

def print_results(score, algorithm, has_politics, has_states, has_years, has_years_since):
    print("-"*60)
    print(f'{algorithm}')
    print(f'{"" if has_politics else "!"}POLITICS | {"" if has_states else "!"}STATES | {"" if has_years else "!"}YEARS | {"" if has_years_since else "!"}YEARS SINCE STANDARD SETTING')
    print(score)

df = pd.read_csv('data/cc_state_data.csv')
#ml_combinations(df, LinearRegression())
ml_combinations(df, MLPRegressor(hidden_layer_sizes=(30,30,30), max_iter=1000))
