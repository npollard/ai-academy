import pandas as pd
from pandas.api.types import CategoricalDtype
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

def transform_data(df, has_politics):
    df = one_hot(df)
    if has_politics:
        df = one_hot_politics(df)
    else:
        df = df.drop('pres', axis=1)
        df = df.drop('gov', axis=1)
    return df

def train_test(df):
    x = df.drop(df.iloc[:,2:6], axis=1)
    y = df.iloc[:, 2:6]
    x_train, x_test, y_train, y_test = train_test_split(x, y) #, random_state=42)
    return (x_train, x_test, y_train, y_test)

def one_hot(df):
    cat_headers = ['state', 'subject']
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
    cat_headers = ['state', 'pres', 'gov', 'grade', 'subject']
    for header in cat_headers:
        df[header] = df[header].astype('category')

    return df

def linear_regression(df, has_politics):
    df = transform_data(df, has_politics)
    x_train, x_test, y_train, y_test = train_test(df)
    reg = LinearRegression().fit(x_train, y_train)
    print("*"*50)
    print(f'LinearRegression WITH{"" if has_politics else "OUT"} POLITICS')
    print('Training score', reg.score(x_train,y_train))
    print('Testing score:', reg.score(x_test,y_test))

def neural_network(df, has_politics):
    df = transform_data(df, has_politics)
    x_train, x_test, y_train, y_test = train_test(df)
    mlp = MLPRegressor(max_iter=9000).fit(x_train, y_train)
    predictions = mlp.predict(x_test)
    print("*"*50)
    print(f'MLPRegressor WITH{"" if has_politics else "OUT"} POLITICS')
    print(mlp.score(x_test, y_test))

df = pd.read_csv('data/all_alds_one_row.csv')
linear_regression(df, True)
linear_regression(df, False)
neural_network(df, True)
neural_network(df, False)
