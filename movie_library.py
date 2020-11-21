import random
from faker import Faker
from faker.providers import lorem


class Movie:
    def __init__(self, title, publish_year, genre):
        self.title = title
        self.publish_year = publish_year
        self.genre = genre
        self.views = 0

    def __repr__(self):
        return f'Movie(title={self.title}, publish_year={self.publish_year}, genre={self.genre}, '\
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
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

    def __repr__(self):
        return f'Series(episode={self.episode}, season={self.season}, title={self.title}, '\
               f'publish_year={self.publish_year}, genre={self.genre}, views={self.views})'


def fake_movie_library(how_many_items=100):
    '''
    generates a list of fakes objects in <class '__main__.Movie'> or <class '__main__.Series'>
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
    _movie_library = []
    while step <= how_many_items:
        selector = random.randint(0, 1)
        if selector == 1:
            _movie_library.append(Movie(
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
            for season in range(1, seasons+1):
                if step <= how_many_items:
                    break
                else:

                    for episode in range(1, episodes+1):
                        _movie_library.append(Series(
                            episode=episode,
                            season=season,
                            title=title,
                            publish_year=year,
                            genre=genre
                        ))
                        year += 1
                        step += 1
    return _movie_library


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
    return sorted(series_list, key=lambda series: series.title)


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
    index = random.randint(0, len(movie_library_list)-1)
    views = random.randint(0, 100)
    movie_library_list[index].play(views)


def run_generate_views(movie_library_list):
    '''
    runs functions generate_vievs 10 times
    :param movie_library_list: list
    :return: <class 'NoneType'>
    '''
    step = 0
    while step < 10:
        generate_views(movie_library_list)
        step += 1


def top_titles(movies_library_list, how_many_titles):
    _sorted = sorted(movies_library_list, key=lambda movie: movie.views, reverse=True)
    print(f'  Top {how_many_titles} Titles:')
    for index in range(how_many_titles):
        print(f'  {index+1}. {_sorted[index]}, views {_sorted[index].views}')


movie_library = [
    Movie('Funny Games', 2004, "thriller"),
    Series(1, 1, title='Alf', publish_year=1984, genre='comedy'),
    Movie('Team America', 2002, 'comedy'),
    Movie('Amelia', 1997, 'comedy')
]

run_generate_views(movie_library)
top_titles(movie_library, 3)