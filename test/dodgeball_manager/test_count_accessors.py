import unittest
from test.dodgeball_manager import DodgeballManagerTestCase
from dodgeball_manager import DodgeballManager

class TestCountAccessors(DodgeballManagerTestCase):


	#########################
	#    nBenchedPlayers    #
	#########################

    def test_nBenchedPlayers_typical_unmodified(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0
        
        self.assertEqual(0, self._dm_typical_unmodifed.nBenchedPlayers())

    def test_nBenchedPlayers_typical_modified(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        
        self.assertEqual(2, self._dm_typical_modifed.nBenchedPlayers())

    def test_nBenchedPlayers_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0
        
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())
    



    ########################
	#    nActiveDodgers    #
	########################

    def test_nActiveDodgers_typical_unmodified(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0

        self.assertEqual(6, self._dm_typical_unmodifed.nActiveDodgers())

    def test_nActiveDodgers_typical_modified(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0

        self.assertEqual(4, self._dm_typical_modifed.nActiveDodgers())

    def test_nActiveDodgers_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0

        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
