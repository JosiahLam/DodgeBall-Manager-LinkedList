# dodgeball_player
#
# models a player of dodgeball with a score


def name_map(dodgeball_player):
    """Maps a dodgeball player to their name."""
    return dodgeball_player.get_name()

def score_map(dodgeball_player):
    """Maps a dodgeball player to their score."""
    return dodgeball_player.get_score()

class DodgeballPlayer:
    """A player of dodgeball."""

    def __init__(self, name : str):
        """Constructor. Sets up name and score."""
        self._name = name
        self._score = 0

    def __str__(self):
        """Prints the dodgeball's player and score with a space in-between."""
        return f"{self._name} {self._score}"

    def get_name(self) -> str:
        """Accessor for the player's name."""
        return self._name
    
    def get_score(self) -> int:
        """Accessor for the player's score."""
        return self._score
    
    def increment_score(self):
        """Increments the score for this player."""
        self._score += 1