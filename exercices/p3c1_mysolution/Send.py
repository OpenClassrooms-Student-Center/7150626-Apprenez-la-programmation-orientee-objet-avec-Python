def send_mass_messages(message, user_list):
    """Envoi des messages en masse.

    Utilise la méthode de message de chaque utilisateur."""
    for user in user_list:
        mail_merge = {"name": user.name, "contact_info": user.contact_method}
        customised_message = message.format(**mail_merge)
        user.send(customised_message)
