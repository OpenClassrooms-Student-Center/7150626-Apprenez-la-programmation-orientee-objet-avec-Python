"""Donne des méthodes d'aides pour l'utilisation du système de contact."""


def verify_adress(address):
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
