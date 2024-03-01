import matplotlib.pyplot as plt
import pandas as pd


def graph_across_grades(df, state, subjects, grades, standard_setting_years):
    df = df[df['state'] == state]
    df = df.sort_values(by=['year', 'subject', 'grade'], ascending=True)
    print(df)
    fig, axs = plt.subplots(len(subjects), len(grades))
    for ids, subject in enumerate(subjects):
        for idg, grade in enumerate(grades):
            graphify(df, state, subject, grade, standard_setting_years, axs[ids, idg])
    plt.show()

def graphify(df, state, subject, grade, standard_setting_years, ax):
    df = df[df['subject'] == subject]
    df = df[df['grade'] == grade]

    ax.set_title(f'{state} {subject} GRADE {grade}')
    ax.set_ylabel('Percentage of students')
    ax.plot(df['year'], df['bb'], color='purple', label='Below Basic')
    ax.plot(df['year'], df['ba'], color='red', label='At or above Basic')
    ax.plot(df['year'], df['pr'], color='orange', label='At or above Proficient')
    ax.plot(df['year'], df['ad'], color='yellow', label='At Advanced')
    for year in standard_setting_years:
        ax.axvline(x=year, label='Standard setting')

    ax.legend()

df = pd.read_csv('data/all_alds_one_row.csv')
#graph_across_grades(df, 'NY', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2013, 2018])
# CC:
#graph_across_grades(df, 'AR', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'CA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'CO', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'CT', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'DE', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'DC', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
graph_across_grades(df, 'GA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'HI', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
graph_across_grades(df, 'ID', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'IL', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'IA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'KS', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'KY', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'LA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'ME', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'MD', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'MA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'MI', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
graph_across_grades(df, 'MS', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'MT', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'NV', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'NH', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'NM', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'NY', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
graph_across_grades(df, 'ND', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'OH', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'OR', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'PA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'RI', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
graph_across_grades(df, 'SD', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'VT', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'WA', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'WV', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'WI', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
#graph_across_grades(df, 'WY', ['MATHEMATICS', 'READING', 'SCIENCE'], [4,8], [2010, 2015])
