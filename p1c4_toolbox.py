"""Ici, nous allons serrer des vis et taper sur des clous!"""


class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        self.tools.append(tool)

    def remove_tool(self, tool):
        """Enleve un outil."""
        index = self.tools.index(tool)
        del self.tools[index]


class Screwdriver:
    """Tournevis."""

    def __init__(self, size=3):
        """Initialise la taille."""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        screw.tighten()

    def loosen(self, screw):
        """Desserre une vis."""
        screw.loosen()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Tournevis de taille {self.size}"


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color

    def paint(self, color):
        """Paint le marteau."""
        self.color = color

    def hammer_in(self, nail):
        """Enfonce un clou."""
        nail.nail_in()

    def remove(self, nail):
        """Enleve un clou."""
        nail.remove()

    def __repr__(self):
        """Représentation de l'objet."""
        return f"Marteau de couleur {self.color}"


class Screw:
    """Vis."""

    MAX_TIGHTNESS = 5

    def __init__(self):
        """Initialise son degré de serrage."""
        self.tightness = 0

    def loosen(self):
        """Déserre le vis."""
        if self.tightness > 0:
            self.tightness -= 1

    def tighten(self):
        """Serre le vis."""
        if self.tightness < self.MAX_TIGHTNESS:
            self.tightness += 1

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        return "Vis avec un serrage de {}".format(self.tightness)


class Nail:
    """Clou."""

    def __init__(self):
        """Initialise son statut "dans le mur"."""
        self.in_wall = False

    def nail_in(self):
        """Enfonce le clou dans un mur."""
        if not self.in_wall:
            self.in_wall = True

    def remove(self):
        """Enlève le clou du mur."""
        if self.in_wall:
            self.in_wall = False

    def __str__(self):
        """Retourne une forme lisible de l'objet."""
        wall_state = "dans le mur" if self.in_wall else "hors du mur"
        return f"Clou {wall_state}."


# Instanciez une boîte à outils, un tournevis, et un marteau.
hammer = Hammer()
screwdriver = Screwdriver()
toolbox = ToolBox()

# Placez le marteau et le tournevis dans la boîte à outils.
toolbox.add_tool(hammer)
toolbox.add_tool(screwdriver)

# Instanciez une vis, et serrez-la avec le tournevis.
# Affichez la vis avant après avoir été serrée.
screw = Screw()
print(screw)
screwdriver.tighten(screw)
print(screw)

# Instanciez un clou, puis enfoncez-le avec le marteau.
# Affichez le clou avant et après avoir été enfoncé.
nail = Nail()
print(nail)
hammer.hammer_in(nail)
print(nail)


# --------------------------------------------------------------
# Que pouvez-vous faire d’autre avec ces classes et ces objets ?

# enlever un outil
print("outils dans la boîte:", toolbox.tools)
toolbox.remove_tool(hammer)
print("on a enlevé le marteau")
print("outils dans la boîte:", toolbox.tools)

# désserrer la vis
screwdriver.loosen(screw)
print(screw)

# enlever le clou
hammer.remove(nail)
print(nail)

# repeindre le marteau
hammer.paint("yellow")
print(hammer)
