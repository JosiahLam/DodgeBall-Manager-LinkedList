import unittest
from test.dodgeball_manager import DodgeballManagerTestCase
from dodgeball_manager import DodgeballManager

class TestBooleanAccessors(DodgeballManagerTestCase):
        
    ####################
	#    isThrower     #
	####################
    
    def test_isThrower_typical_unmodified(self):
        # Typical DM (unmodified):
        #   3 throwers: Zuko 0, Iro 0, Azula 0
        #   6 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0

        # check throwers
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Zuko"))
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Azula"))
        self.assertTrue(self._dm_typical_unmodifed.isThrower("Iro"))

        # check active dodgers
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Aang"))
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Katara"))
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Sokka"))
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Toph"))
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Appa"))
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Momo"))
        
        # check completely different name
        self.assertFalse(self._dm_typical_unmodifed.isThrower("Spongebob"))

    def test_isThrower_typical_modified(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0

        # check throwers
        self.assertTrue(self._dm_typical_modifed.isThrower("Zuko"))
        self.assertTrue(self._dm_typical_modifed.isThrower("Azula"))
        self.assertTrue(self._dm_typical_modifed.isThrower("Iro"))

        # check active dodgers
        self.assertFalse(self._dm_typical_modifed.isThrower("Aang"))
        self.assertFalse(self._dm_typical_modifed.isThrower("Katara"))
        self.assertFalse(self._dm_typical_modifed.isThrower("Sokka"))
        self.assertFalse(self._dm_typical_modifed.isThrower("Toph"))

        # check bench
        self.assertFalse(self._dm_typical_modifed.isThrower("Appa"))
        self.assertFalse(self._dm_typical_modifed.isThrower("Momo"))
        
        # check completely different name
        self.assertFalse(self._dm_typical_modifed.isThrower("Spongebob"))
    
    
    def test_isThrower_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0

        # check thrower
        self.assertTrue(self._dm_unusual.isThrower("Zuko"))

        # check dodger
        self.assertFalse(self._dm_unusual.isThrower("Azula"))
        
        # check completely different name
        self.assertFalse(self._dm_unusual.isThrower("Spongebob"))


    #########################
	#    isActiveDodger     #
	#########################

    def test_isActiveDodger_typical_unmodified(self):
        # Typical DM (unmodified):
        #   3 throwers: Zuko 0, Iro 0, Azula 0
        #   6 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0

        # check throwers
        self.assertFalse(self._dm_typical_unmodifed.isActiveDodger("Zuko"))
        self.assertFalse(self._dm_typical_unmodifed.isActiveDodger("Azula"))
        self.assertFalse(self._dm_typical_unmodifed.isActiveDodger("Iro"))

        # check active dodgers
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Aang"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Katara"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Sokka"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Toph"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Appa"))
        self.assertTrue(self._dm_typical_unmodifed.isActiveDodger("Momo"))
        
        # check completely different name
        self.assertFalse(self._dm_typical_unmodifed.isActiveDodger("Spongebob"))


    def test_isActiveDodger_typical_modified(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        
        # check throwers
        self.assertFalse(self._dm_typical_modifed.isActiveDodger("Zuko"))
        self.assertFalse(self._dm_typical_modifed.isActiveDodger("Azula"))
        self.assertFalse(self._dm_typical_modifed.isActiveDodger("Iro"))
        
        # check active dodgers
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Aang"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Katara"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Sokka"))
        self.assertTrue(self._dm_typical_modifed.isActiveDodger("Toph"))

        # check bench
        self.assertFalse(self._dm_typical_modifed.isActiveDodger("Appa"))
        self.assertFalse(self._dm_typical_modifed.isActiveDodger("Momo"))
        
        # check completely different name
        self.assertFalse(self._dm_typical_modifed.isActiveDodger("Spongebob"))

    def test_isActiveDodger_unusual_true(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0

        # check thrower
        self.assertFalse(self._dm_unusual.isActiveDodger("Zuko"))

        # check dodger
        self.assertTrue(self._dm_unusual.isActiveDodger("Azula"))
        
        # check completely different name
        self.assertFalse(self._dm_unusual.isActiveDodger("Spongebob"))
    

    ##########################
	#    isBenchedPlayer     #
	##########################

    def test_isBenchedPlayer_typical_unmodified(self):
        # Typical DM (unmodified):
        #   3 throwers: Zuko 0, Iro 0, Azula 0
        #   6 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0, Appa 0, Momo 0

        # check throwers
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Zuko"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Azula"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Iro"))

        # check active dodgers
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Aang"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Katara"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Sokka"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Toph"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Appa"))
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Momo"))
        
        # check completely different name
        self.assertFalse(self._dm_typical_unmodifed.isBenchedPlayer("Spongebob"))


    def test_isBenchedPlayer_typical_modified_true(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        
        # check throwers
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Zuko"))
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Azula"))
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Iro"))

        # check active dodgers
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Aang"))
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Katara"))
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Sokka"))
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Toph"))
        
        # check bench
        self.assertTrue(self._dm_typical_modifed.isBenchedPlayer("Appa"))
        self.assertTrue(self._dm_typical_modifed.isBenchedPlayer("Momo"))
        
        # check completely different name
        self.assertFalse(self._dm_typical_modifed.isBenchedPlayer("Spongebob"))


    def test_isBenchedPlayer_unusual(self):
        # Unusual DM:
        #   1 thrower: Zuko 0
        #   1 active dodger: Azula 0

        # check thrower
        self.assertFalse(self._dm_unusual.isBenchedPlayer("Zuko"))

        # check dodger
        self.assertFalse(self._dm_unusual.isBenchedPlayer("Azula"))
        
        # check completely different name
        self.assertFalse(self._dm_unusual.isBenchedPlayer("Spongebob"))