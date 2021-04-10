"""Définit l'utilisateur."""


class User:
    """Un utilisateur."""

    def __init__(self, name, contact_method):
        """Initialise un nom et une methode de contact."""
        self.name = name
        self.contact_method = contact_method

    def send(self, message):
        """Envoit un message."""
        self.contact_method.send(message)
