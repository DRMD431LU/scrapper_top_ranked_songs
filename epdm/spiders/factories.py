import itertools

def get_formatted_url_dates() ->list:
    dates = list(itertools.product(range(2010, 2024), range(1, 53)))
    return [f"https://www.elportaldemusica.es/lists/top-100-canciones/{year}/{week}" for year, week in dates]




