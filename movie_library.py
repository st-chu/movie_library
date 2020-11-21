import random


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


def get_movies(movies_library_list):
    movies_list = []
    for item in movies_library_list:
        if isinstance(item, Series) is not True:
            movies_list.append(item)
    return sorted(movies_list, key=lambda movie: movie.title)


def get_series(movies_library_list):
    series_list = []
    for item in movies_library_list:
        if isinstance(item, Series) is True:
            series_list.append(item)
    return sorted(series_list, key=lambda series: series.title)


def search(title, movies_library_list):
    for item in movies_library_list:
        if item.title.lower() == title.lower():
            return item


def generate_views(movie_library_list):
    index = random.randint(0, len(movie_library_list)-1)
    views = random.randint(0, 100)
    movie_library_list[index].play(views)


movie_library = [
    Movie('Funny Games', 2004, "thriller"),
    Series(1, 1, title='Alf', publish_year=1984, genre='comedy'),
    Movie('Team America', 2002, 'comedy'),
    Movie('Amelia', 1997, 'comedy')
]
generate_views(movie_library)
print(get_movies(movie_library))