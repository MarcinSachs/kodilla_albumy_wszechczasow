import pandas as pd


def get_album_data():
    '''Pobiera dane o najlepiej sprzedających się albumach wszech czasów z oficjalnej strony UK Charts'''
    data = pd.read_html(
        'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551', header=0)
    df = pd.DataFrame(data[0])
    df.drop(columns=['POS'], inplace=True)
    return df


def rename_columns_to_polish(df):
    '''Zamienia nazwy kolumn na język polski'''
    df.rename(columns={'TITLE': 'TYTUŁ', 'ARTIST': 'ARTYSTA',
                       'YEAR': 'ROK', 'HIGH POSN': 'MAX POZ'}, inplace=True)
    return df


def get_unique_artists_count(df):
    '''Zwraca liczbę unikalnych artystów w DataFrame'''
    return df['ARTYSTA'].nunique()


def get_top_artists(df):
    '''Zwraca top artystów z największą liczbą albumów na liście'''
    top_artists = df['ARTYSTA'].value_counts().head()
    return top_artists


def rename_columns_to_capitalized(df):
    '''Zamienia nazwy kolumn na kapitalizowane'''
    df.rename(columns=lambda x: x.capitalize(), inplace=True)
    return df


df = get_album_data()

# 1. zamiana nazw kolumn na język polski
df = rename_columns_to_polish(df)

# 2. Ilu pojedynczych artystów znajduje się na liście?
print(f'Liczba unikalnych artystów: {get_unique_artists_count(df)}')
# output: Liczba unikalnych artystów: 47

# 3. Które zespoły pojawiają się najczęściej na liście?
print(
    f'Zespoły, które pojawiają się najczęściej na liście: {get_top_artists(df)}')
# output: Zespoły, które pojawiają się najczęściej na liście:
# TAKE THAT          3
# COLDPLAY           3
# QUEEN              2
# ADELE              2
# MICHAEL JACKSON    2

# 4. zamiana nazw kolumn na kapitalizowane
df = rename_columns_to_capitalized(df)

# 5. Usunięcie kolumny 'Max poz'
df.drop(columns=['Max poz'], inplace=True)
