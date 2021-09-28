from User import User
from Contact_system import TextContactSystem,OwlContactSystem
from Send import send_mass_messages

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