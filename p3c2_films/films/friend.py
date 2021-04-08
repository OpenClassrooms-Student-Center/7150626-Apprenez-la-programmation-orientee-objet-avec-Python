"""Définit les amis."""

from .data import friends


class Friend:
    """Ami."""

    def __init__(self, name, film=None):
        """Initialise le nom, et un film prêté si c'est le cas."""
        self.name = name
        self.film = film
        if film:
            film.where = self

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return self.__str__()


class FriendCleaner:
    """Génère un ami d'après les données brutes."""

    NAME_INDEX = 0
    FILM_INDEX = 1

    def __init__(self):
        """Initialise les données d'amis."""
        self.friends = friends

    def generate(self, data, library):
        """Retourne un ami à partir des données brutes.

        Attention ici l'exercice consistait à utiliser
        de vrais objets films et pas juste le nom du film !
        """
        name = data[self.NAME_INDEX]
        if len(data) > 1:
            film_name = data[self.FILM_INDEX]
            film = library.find_by_name(film_name)
        else:
            film = None

        return Friend(name, film)

    def list_from_data(self, library):
        """Retourne une liste d'amis à partir des données brutes.

        Attrs:
        - library (Library) : une instance de bibliothèque de films.

        Note: On pourrait aussi utiliser une liste de compréhension ici.
        """
        result = []
        for data in self.friends:
            friend = self.generate(data, library)
            result.append(friend)
        return result
