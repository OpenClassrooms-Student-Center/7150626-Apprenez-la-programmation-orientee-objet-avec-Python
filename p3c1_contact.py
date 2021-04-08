"""Contacts.

Séparez le programme en plusieurs modules et packages,
en ajoutant les fichiers __init__.py et les imports si necessaire.

Vérifiez que le programme s'éxecute correctement en lancant main.py depuis la racine
du projet.
"""

from abc import ABC, abstractmethod


class User:
    """Un utilisateur."""

    def __init__(self, name, contact_method):
        """Initialise un nom et une methode de contact."""
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        """Envoit un message."""
        self.contact_method.send(message)


class ContactSystem(ABC):
    """Classe abstraite utilisée pour envoyer un message à un utilisateur."""

    @abstractmethod
    def send(self, message):
        """Toutes les sous-classes de ContactSystem doivent implémenter send."""
        pass


class TextContactSystem(ContactSystem):
    """Envoi un message à l'utilisateur par SMS."""

    def __init__(self, phone_number):
        """Initialise le numéro de téléphone."""
        super().__init__()
        validate_phone(phone_number)
        self.phone_number = phone_number

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" au numéro {self.phone_number}')

    def __str__(self):
        """Représentation lisible."""
        return f"Le numéro de téléphone est {self.phone_number}"


class OwlContactSystem(ContactSystem):
    """Envoi un message en utilisant une chouette ! 🧙‍♂️"""

    def __init__(self, address):
        """Initialise l'addresse."""
        varify_address(address)
        self.address = address
        self.owl = "Hedwige"
        super().__init__()

    def send(self, message):
        """Envoi le message."""
        print(f'Envoi du message "{message}" par chouette {self.owl}')

    def __str__(self):
        """Représentation."""
        return f"L'addresse est '{self.address}'"


def varify_address(address):
    """Fausse fonction qui retourne True."""
    return True


def validate_phone(phone_number):
    """Retourne True par défaut."""
    return True


def send_mass_messages(message, user_list):
    """Envoi des messages en masse.

    Utilise la méthode de message de chaque utilisateur."""
    for user in user_list:
        mail_merge = {"name": user.name, "contact_info": user.contact_method}
        customised_message = message.format(**mail_merge)
        user.send(customised_message)


# Our main program.
alice = User("Alice", TextContactSystem("0102030405"))
bob = User("Bob", OwlContactSystem("4 Privet Drive"))

user_list = [alice, bob]
send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
send_mass_messages(
    "Salut {name}. Tes informations de contact sont-elles corrects?"
    " Nous avons celles-ci: {contact_info}.",
    user_list,
)
