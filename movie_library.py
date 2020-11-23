import random
from faker import Faker
import datetime


class Movie:
    def __init__(self, title, publish_year, genre):
        self.title = title
        self.publish_year = publish_year
        self.genre = genre
        self.views = 0

    def __repr__(self):
        return f'Movie(title={self.title}, publish_year={self.publish_year}, genre={self.genre}, ' \
               f'views={self.views})'

    def __str__(self):
        return f'{self.title} ({self.publish_year})'

    def play(self, step=1):
        '''
        increases the number of views of the title by 1
        :param step: int
        :return: <NoneType>
        '''
        self.views += step


class Series(Movie):
    counter = {}

    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season
        selector = False
        for key, value in Series.counter.items():
            if self.title == key:
                selector = True
        if selector is True:
            Series.counter[self.title] = Series.counter[self.title] + 1
        else:
            Series.counter[self.title] = 1

    @classmethod
    def titles_count(cls):
        return cls.counter

    def how_many_episodes(self):
        how_many = self.counter[self.title]
        return how_many

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

    def __repr__(self):
        return f'Series(episode={self.episode}, season={self.season}, title={self.title}, ' \
               f'publish_year={self.publish_year}, genre={self.genre}, views={self.views})'


def fake_movie_library(movie_library_list, how_many_items=100):
    '''
    a function that adds fake Movie or Series objects to the movie library
    :param movie_library_list: list
    :param how_many_items: int
    :return: list
    '''
    step = 1
    fake = Faker(['pl_PL', 'en_US'])
    my_genre = [
        'comedy', 'thriller', 'western', 'spy film', 'sport film', 'silent film', 'science fiction film', 'parody',
        'musical', 'remake', 'horror', 'melodrama', 'historical', 'erotic', 'drama', 'action', 'romantic comedy',
        'comedy drama', 'black comedy', 'cartoon', 'cabaret', 'biographical'
    ]
    while step <= how_many_items:
        selector = random.randint(0, 1)
        if selector == 1:
            movie_library_list.append(Movie(
                title=fake.sentence(nb_words=3),
                publish_year=random.randint(1960, 2020),
                genre=fake.sentence(ext_word_list=my_genre, nb_words=1)
            ))
            step += 1
        elif selector == 0:
            episodes = random.randint(1, 12)
            seasons = random.randint(1, 3)
            title = fake.sentence(nb_words=3)
            year = random.randint(1960, 2020)
            if episodes + year > 2020:
                episodes -= ((episodes + year) - 2020)
            genre = fake.sentence(ext_word_list=my_genre, nb_words=1)
            for season in range(1, seasons + 1):
                for episode in range(1, episodes + 1):
                    if step >= how_many_items:
                        break
                    else:
                        movie_library_list.append(Series(
                            episode=episode,
                            season=season,
                            title=title,
                            publish_year=year,
                            genre=genre
                        ))
                        year += 1
                        step += 1
    return movie_library_list


def get_movies(movies_library_list):
    '''
    a function that filters the movies_library_list and returns a sorted list of movies
    :param movies_library_list: list
    :return: movies_list: list
    '''
    movies_list = []
    for item in movies_library_list:
        if isinstance(item, Series) is not True:
            movies_list.append(item)
    return sorted(movies_list, key=lambda movie: movie.title)


def get_series(movies_library_list):
    '''
    a function that filters the movies_library_list and returns a sorted list of series
    :param movies_library_list: list
    :return: series_list: list
    '''
    series_list = []
    for item in movies_library_list:
        if isinstance(item, Series) is True:
            series_list.append(item)
    return sorted(series_list, key=lambda _series: _series.title)


def search(title, movies_library_list):
    '''
    function that searches for movies or series by title
    :param title: str
    :param movies_library_list: list
    :return: object: <class '__main__.Movie'> or <class '__main__.Series'>
    '''
    for item in movies_library_list:
        if item.title.lower() == title.lower():
            return item


def generate_views(movie_library_list):
    '''
    a function that randomly selects an item from the library and then adds a random (ranging from 1 to 100)
    number of plays
    :param movie_library_list: list
    :return: <class 'NoneType'>
    '''
    index = random.randint(0, len(movie_library_list) - 1)
    views = random.randint(0, 100)
    movie_library_list[index].play(views)


def run_generate_views(movie_library_list):
    '''
    runs functions generate_vievs 200 times
    :param movie_library_list: list
    :return: <class 'NoneType'>
    '''
    step = 0
    while step < 200:
        generate_views(movie_library_list)
        step += 1


def top_titles(movies_library_list, /, how_many_titles=3, content_type=None):
    '''
    If content_type=None, the function returns the most popular titles from the library.
    If content_type=1, the function returns the most popular movies.
    If content_type=2, the function returns the most popular series.
    :param movies_library_list: list
    :param how_many_titles: int
    :param content_type: None, 1, 2
    :return: <class 'NoneType'>
    '''
    if content_type == 1:
        list_to_sorted = get_movies(movies_library_list)
    elif content_type == 2:
        list_to_sorted = get_series(movies_library_list)
    else:
        list_to_sorted = movies_library_list
    _sorted = sorted(list_to_sorted, key=lambda movie: movie.views, reverse=True)
    #print(f'  Top {how_many_titles} Titles:')
    try:
        for index in range(how_many_titles):
            print(f'  {index + 1}. {_sorted[index]}, views {_sorted[index].views}')
    except IndexError:
        print(f" \n We only have {len(_sorted)} titles in the library.")


def add_season_to_movie_library(movie_library_list, title, year, genre, episodes, season):
    '''
    adds a full season to the movie library
    :param movie_library_list: list
    :param title: str
    :param year: int
    :param genre: str
    :param episodes: int
    :param season: int
    :return: list
    '''
    for episode in range(1, episodes + 1):
        movie_library_list.append(Series(title=title, publish_year=year, genre=genre, season=season, episode=episode))
    return movie_library_list


if __name__ == '__main__':
    print(' Biblioteka Filmów '.center(50, '*'))

    # filling the library with content
    movie_library = []
    fake_movie_library(movie_library)
    add_season_to_movie_library(movie_library, 'Alf', 1984, 'comedy', 10, 1)
    add_season_to_movie_library(movie_library, 'Alf', 1984, 'comedy', 11, 2)
    add_season_to_movie_library(movie_library, 'Gumisie', 1989, 'cartoon', 20, 1)
    add_season_to_movie_library(movie_library, 'Gumisie', 1989, 'cartoon', 15, 2)

    # generate views with the generate_views function
    run_generate_views(movie_library)

    # print top 3 titles from movie_library, print the best movie, print the best series
    date = datetime.date.today()
    print(f'\nNajpopularniejsze filmy i seriale dnia {date.day}.{date.month}.{date.year}')
    top_titles(movie_library, 3)
    print(f'\nNajpopularniejszy film dnia {date.day}.{date.month}.{date.year}')
    top_titles(movie_library, 1, 1)
    print(f'\nNajpopularniejszy serial dnia {date.day}.{date.month}.{date.year}')
    top_titles(movie_library, 1, 2)

    # print how many episodes of series is in movie_library
    series = get_series(movie_library)
    print(f'\nW bibliotece jest {series[0].how_many_episodes()} odcinków serialu {series[0].title}')