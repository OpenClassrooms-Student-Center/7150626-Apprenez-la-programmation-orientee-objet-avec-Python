"""Point d'entrée."""

from contact.user import User
from contact.owlcontact import OwlContactSystem
from contact.textcontact import TextContactSystem
from contact.helpers import send_mass_messages


def main():
    """Main function."""
    alice = User("Alice", TextContactSystem("0102030405"))
    bob = User("Bob", OwlContactSystem("4 Privet Drive"))

    user_list = [alice, bob]
    send_mass_messages("Hello {name}, Comment vas-tu?", user_list)
    send_mass_messages(
        "Salut {name}. Tes informations de contact sont-elles corrects?"
        " Nous avons celles-ci: {contact_info}.",
        user_list,
    )


if __name__ == "__main__":
    main()
