
class Movie:
    def __init__(self, title, publish_year, genre):
        self.title = title
        self.publish_year = publish_year
        self.genre = genre
        self.play_number = 0

    def __repr__(self):
        return f'Movie(title={self.title}, publish_year={self.publish_year}, genre={self.genre}, '\
               f'play_number={self.play_number})'

    def __str__(self):
        return f'{self.title} ({self.publish_year})'

    def play(self, step=1):
        self.play_number += step


class Series(Movie):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'{self.title} S{self.season:02d}E{self.episode:02d}'

    def __repr__(self):
        return f'Series(episode={self.episode}, season={self.season}, title={self.title}, '\
               f'publish_year={self.publish_year}, genre={self.genre}, play_number={self.play_number})'


movie_library = [
    Series(1, 1, title='Alf', publish_year=1984, genre='comedy'),
    Movie('Funny Games', 2004, "thriller")
]

print(movie_library)