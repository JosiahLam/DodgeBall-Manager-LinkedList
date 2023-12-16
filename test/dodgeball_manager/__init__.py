# Global setup functions for the test cases

import unittest
from dodgeball_manager import DodgeballManager


class DodgeballManagerTestCase(unittest.TestCase):
    """
    Base class for DodgeballManager test cases.
    Implements setUp() for every test case that inherits it.
    """


    def setUp(self):
        """ sets up typical and unusual cases"""

        # Setup a typical DM:
        #   3 throwers: Zuko 0, Iro 0, Azula 0
        #   6 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0
        self._dm_typical_unmodifed = DodgeballManager(
            ["Zuko", "Iro", "Azula"],
            ["Aang", "Katara", "Sokka", "Toph", "Appa", "Momo"])


        # Setup a typical DM:
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        self._dm_typical_modifed = DodgeballManager(
            ["Zuko", "Iro", "Azula"],
            ["Aang", "Katara", "Sokka", "Toph","Appa", "Momo"])
        self._dm_typical_modifed.hit("Zuko", "Appa")
        self._dm_typical_modifed.hit("Azula", "Momo")


        # Setup unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0
        self._dm_unusual = DodgeballManager(
            ["Zuko"],
            ["Azula"])