"""Définit des classes d'outils."""


class ToolBox:
    """Boite à outils."""

    def __init__(self):
        """Initialise les outils."""
        self.tools = []

    def add_tool(self, tool):
        """Ajoute un outil."""
        pass

    def remove_tool(self, tool):
        """Enleve un outil."""
        pass


class Screwdriver:
    """Tournevis."""

    def __init__(self, size):
        """Initialise la taille."""
        self.size = size

    def tighten(self, screw):
        """Serrer une vis."""
        pass

    def loosen(self, screw):
        """Desserre une vis."""
        pass


class Hammer:
    """Marteau."""

    def __init__(self, color="red"):
        """Initialise la couleur."""
        self.color = color

    def paint(self, color):
        """Paint le marteau."""
        pass

    def hammer_in(self, nail):
        """Enfonce un clou."""
        pass

    def remove(self, nail):
        """Enleve un clou."""
        pass
