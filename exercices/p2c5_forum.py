"""Définit les classes propres à notre forum. ;)"""

import time
from abc import ABC


class File(ABC):
    """Fichier."""

    def __init__(self, name, size):
        """Initialise le nom et la taille."""
        self.name = name
        self.size = size

    def display(self):
        """Affiche le fichier."""
        pass


class ImageFile(File):
    """Fichier image."""

    def display(self):
        """Affiche l'image."""
        print(f"Fichier image '{self.name}'.")


class GifImageFile(ImageFile):
    """Fichier image Gif."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'Gif'.")


class PNGImageFile(ImageFile):
    """Fichier image PNG."""

    def display(self):
        """Affiche l'image."""
        super().display()
        print("L'image est de type 'PNG'.")


class User:
    """Utilisateur."""

    def __init__(self, username, password):
        """Initialise le nom d'utilisateur et le mot de passe."""
        self.username = username
        self.password = password

    def login(self):
        """Connecte l'utilisateur."""
        print(f"L'utilisateur {self.username} est connecté.")

    def post(self, thread, content, file=None):
        """Poste un message dans un fil de discussion."""
        if file:
            post = FilePost(self, "aujourd'hui", content, file)
        else:
            post = Post(user=self, time_posted="aujourd'hui", content=content)
        thread.add_post(post)
        return post

    def make_thread(self, title, content):
        """Créé un nouveau fil de discussion."""
        post = Post(self, "aujourd'hui", content)
        return Thread(title, "aujourd'hui", post)

    def __str__(self):
        """représentation de l'utilisateur."""
        return self.username


class Moderator(User):
    """Utilisateur modérateur."""

    def edit(self, post, content):
        """Modifie un message."""
        post.content = content

    def delete(self, thread, post):
        """Supprime un message."""
        index = thread.posts.index(post)
        del thread.posts[index]


class Post:
    """Message."""

    def __init__(self, user, time_posted, content):
        """Initialise l'utilisateur, la date et le contenu."""
        self.user = user
        self.time_posted = time_posted
        self.content = content

    def display(self):
        """Affiche le message."""
        print(f"-- Message posté par {self.user} {self.time_posted} --")
        print(self.content)


class FilePost(Post):
    """Message comportant un fichier."""

    def __init__(self, user, time_posted, content, file):
        """Initialise le fichier."""
        super().__init__(user, time_posted, content)
        self.file = file

    def display(self):
        """Affiche le contenu et le fichier."""
        super().display()
        print("pièce jointe:")
        self.file.display()


class Thread:
    """Fil de discussions."""

    def __init__(self, title, time_posted, post):
        """Initialise le titre, la date et les posts.

        Attention ici: on commence par un seul post, celui du sujet.
        Les réponses à ce post ne pourrons s'ajouter qu'ultérieurement.
        En effet, on ne créé pas directement un nouveau fil avec des réponses. ;)
        """
        self.title = title
        self.time_posted = time_posted
        self.posts = [post]

    def display(self):
        """Affiche le fil de discussion."""
        print("----- THREAD -----")
        print(f"titre: {self.title}, date: {self.time_posted}")
        print()
        for post in self.posts:
            post.display()
            print()
        print("------------------")

    def add_post(self, post):
        """Ajoute un post."""
        self.posts.append(post)


def main():
    """Lance le code principal."""
    user = User("John", "superpassword")
    moderator = Moderator("Lucie", "helloworld")

    cake_thread = user.make_thread("Gâteau à la vanille 🍰 ???", "Vous aimez ou non ?")
    cake_thread.display()

    moderator.post(cake_thread, content="Oui j'aime beaucoup ! 😚")
    cake_thread.display()

    irrelevant_post = user.post(cake_thread, content="Et vous aimez les voitures ?")
    response = moderator.post(cake_thread, content="C'est hors sujet sur ce forum 😕")
    cake_thread.display()

    print()
    print("après quelques minutes, le modérateur supprime les messages hors sujets...")
    print()
    # importer time n'était pas necessaire, c'est un plus:
    time.sleep(2)
    moderator.delete(cake_thread, irrelevant_post)
    moderator.delete(cake_thread, response)
    cake_thread.display()

    image = PNGImageFile(name="image de gâteau", size=3)
    user.post(cake_thread, content="Voici une image de mon gâteau !", file=image)
    moderator.post(cake_thread, "Woah, sublime !")
    cake_thread.display()


main()
