"""Définit le contact par téléphone."""

from contact.abstract import ContactSystem
from contact.helpers import validate_phone


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
