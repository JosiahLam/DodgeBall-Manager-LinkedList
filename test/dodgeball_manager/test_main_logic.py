import unittest
from test.dodgeball_manager import DodgeballManagerTestCase
from dodgeball_manager import DodgeballManager

class TestMainLogic(DodgeballManagerTestCase):


    ###############
	#    Dodge    #
	###############

    # Typical

    def test_dodge_typical1(self):
        # A typical DM (unmodified with hits):
        #   3 throwers: Zuko 0, Iro 0, Azula 0
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0

        # initial state
        self.assertEqual(6, self._dm_typical_unmodifed.nActiveDodgers())
        self.assertEqual(0, self._dm_typical_unmodifed.nBenchedPlayers())
        
        self._dm_typical_unmodifed.dodge("Zuko", "Aang")

        # should have no changes
        self.assertEqual(6, self._dm_typical_unmodifed.nActiveDodgers())
        self.assertEqual(0, self._dm_typical_unmodifed.nBenchedPlayers())
        
        self._dm_typical_unmodifed.dodge("Azula", "Toph")

        # should have no changes
        self.assertEqual(6, self._dm_typical_unmodifed.nActiveDodgers())
        self.assertEqual(0, self._dm_typical_unmodifed.nBenchedPlayers())
        

    def test_dodge_typical2(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        

        # initial state
        self.assertEqual(4, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(2, self._dm_typical_modifed.nBenchedPlayers())
        
        self._dm_typical_unmodifed.dodge("Zuko", "Aang")

        # should have no changes
        self.assertEqual(4, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(2, self._dm_typical_modifed.nBenchedPlayers())
        
        self._dm_typical_unmodifed.dodge("Azula", "Toph")

        # should have no changes
        self.assertEqual(4, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(2, self._dm_typical_modifed.nBenchedPlayers())

    # Unusual
    def test_dodge_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0

        # initial state
        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())
        
        self._dm_unusual.dodge("Zuko", "Azula")

        # should have no changes
        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())
        
        self._dm_unusual.dodge("Zuko", "Azula")

        # should have no changes
        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())


    #############
	#    Hit    #
	#############


    # Typical

    def test_hit_typical(self):
        # A typical DM (unmodified with hits):
        #   3 throwers: Zuko 0, Iro 0, Azula 0
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0

        # initial state
        self.assertEqual(6, self._dm_typical_unmodifed.nActiveDodgers())
        self.assertEqual(0, self._dm_typical_unmodifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Zuko"))
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Iro"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Aang"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Toph"))
        
        self._dm_typical_unmodifed.hit("Zuko", "Aang")

        # Aang should be on bench
        self.assertEqual(5, self._dm_typical_unmodifed.nActiveDodgers())
        self.assertEqual(1, self._dm_typical_unmodifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Zuko"))
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Iro"))
        self.assertTrue(self._dm_typical_unmodifed.isBenchedPlayer("Aang"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Toph"))
        
        self._dm_typical_unmodifed.hit("Iro", "Toph")

        # Aang, Toph should be on bench
        self.assertEqual(4, self._dm_typical_unmodifed.nActiveDodgers())
        self.assertEqual(2, self._dm_typical_unmodifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Zuko"))
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Iro"))
        self.assertTrue(self._dm_typical_unmodifed.isBenchedPlayer("Aang"))
        self.assertTrue(self._dm_typical_unmodifed.isBenchedPlayer("Toph"))

    # Unusual
    
    def test_hit_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0

        # initial state
        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())
        self.assertTrue(self._dm_unusual.isThrower("Zuko"))
        self.assertTrue(self._dm_unusual.isActiveDodger("Azula"))
        
        self._dm_unusual.hit("Zuko", "Azula")

        self.assertEqual(0, self._dm_unusual.nActiveDodgers())
        self.assertEqual(1, self._dm_unusual.nBenchedPlayers())
        self.assertTrue(self._dm_unusual.isThrower("Zuko"))
        self.assertTrue(self._dm_unusual.isBenchedPlayer("Azula"))


    ###################
	#    catchBall    #
	###################

    # Typical
    def test_catchBall_typical(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        
        # initial state
        self.assertEqual(4, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(2, self._dm_typical_modifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_modifed.isThrower("Azula"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Katara"))
        self.assertTrue(self._dm_typical_modifed.isBenchedPlayer("Appa"))
        self.assertTrue(self._dm_typical_modifed.isBenchedPlayer("Momo"))

        self._dm_typical_modifed.catchBall("Azula", "Katara", "Appa")

        self.assertEqual(5, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(1, self._dm_typical_modifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_modifed.isThrower("Azula"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Katara"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Appa"))
        self.assertTrue(self._dm_typical_modifed.isBenchedPlayer("Momo"))

        self._dm_typical_modifed.catchBall("Azula", "Katara", "Momo")

        self.assertEqual(6, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(0, self._dm_typical_modifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_modifed.isThrower("Azula"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Katara"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Appa"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Momo"))

        self._dm_typical_modifed.catchBall("Azula", "Katara")

        self.assertEqual(6, self._dm_typical_modifed.nActiveDodgers())
        self.assertEqual(0, self._dm_typical_modifed.nBenchedPlayers())
        self.assertTrue(self._dm_typical_modifed.isThrower("Azula"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Katara"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Appa"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Momo"))

    
    # Unusual
    def test_catchBall_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0
        
         # initial state
        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())
        self.assertTrue(self._dm_unusual.isThrower("Zuko"))
        self.assertTrue(self._dm_unusual.isActiveDodger("Azula"))

        self._dm_unusual.catchBall("Zuko", "Azula")
        
        # no change
        self.assertEqual(1, self._dm_unusual.nActiveDodgers())
        self.assertEqual(0, self._dm_unusual.nBenchedPlayers())
        self.assertTrue(self._dm_unusual.isThrower("Zuko"))
        self.assertTrue(self._dm_unusual.isActiveDodger("Azula"))


