import pandas as pd


def get_album_data():
    '''Pobiera dane o najlepiej sprzedających się albumach wszech czasów z oficjalnej strony UK Charts'''
    try:
        url = 'https://www.officialcharts.com/chart-news/the-best-selling-albums-of-all-time-on-the-official-uk-chart__15551'
        data = pd.read_html(url, header=0)
        df = pd.DataFrame(data[0])
        df.drop(columns=['POS'], inplace=True)
        return df
    except Exception as e:
        print(f"Wystąpił błąd podczas pobierania danych: {e}")
        raise  # Ponowne zgłoszenie wyjątku, aby obsłużyć go wyżej


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


def get_top_year(df):
    '''Zwraca rok z największą liczbą albumów na liście'''
    top_year = df['Rok'].value_counts().idxmax()
    return top_year


def get_lowest_year(df):
    '''Zwraca najniższy rok wydania albumu na liście'''
    lowest_year = df['Rok'].min()
    return lowest_year


def get_oldest_albums_by_unique_artists(df):
    '''Zwraca najstarsze albumy dla unikalnych artystów'''
    oldest_albums = df.sort_values(by='Rok').drop_duplicates(
        subset=['Artysta'], keep='first')
    return oldest_albums


def save_dataframe_to_csv(df, filename):
    '''Zapisuje DataFrame do pliku CSV'''
    df.to_csv(filename, index=False)


def main():
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

    # 6. W którym roku wyszło najwięcej albumów znajdujących się na liście?
    print(f'Rok z największą liczbą albumów na liście: {get_top_year(df)}')
    # output: Rok z największą liczbą albumów na liście: 1987

    # 7. Ile albumów wydanych między 1960 a 1990 rokiem włącznie znajduje się na liście?
    print(
        f"Liczba albumów wydanych między 1960 a 1990 rokiem włącznie: {len(df.query('1960 <= Rok <= 1990'))}")
    # output: 22

    # 8. W którym roku wydany został najmłodszy album na liście?
    print(f'Najniższy rok wydania albumu na liście: {get_lowest_year(df)}')
    # output: Najniższy rok wydania albumu na liście: 1965

    # 9. Przygotuj listę najwcześniej wydanych albumów każdego artysty, który znalazł się na liście.
    list_of_oldest_albums = get_oldest_albums_by_unique_artists(
        df).drop(columns=['Rok']).reset_index(drop=True)

    # 10. Listę zapisz do pliku csv
    save_dataframe_to_csv(list_of_oldest_albums,
                          'oldest_albums_by_unique_artists.csv')


if __name__ == "__main__":
    main()
