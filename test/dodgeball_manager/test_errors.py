import unittest
from test.dodgeball_manager import DodgeballManagerTestCase
from dodgeball_manager import DodgeballManager

class TestErrors(DodgeballManagerTestCase):
        
    #############################
	#    Constructor Errors     #
	#############################
    
    def test_constructor_error_none(self):
       with self.assertRaises(ValueError):
           dm = DodgeballManager(None, ["Iro", "Ozai"])

       with self.assertRaises(ValueError):
           dm = DodgeballManager(["Iro", "Ozai"], None)

       with self.assertRaises(ValueError):
           dm = DodgeballManager(None, None)


    def test_constructor_error_empty(self):
       with self.assertRaises(ValueError):
           dm = DodgeballManager([], ["Iro", "Ozai"])

       with self.assertRaises(ValueError):
           dm = DodgeballManager(["Iro", "Ozai"], [])

       with self.assertRaises(ValueError):
           dm = DodgeballManager([], [])

    #######################
	#    dodge Errors     #
	#######################
    def test_dodge_error_notinlist(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("Spongebob", "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("Zuko", "Spongebob")
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("Spongebob", "Spongebob")

    def test_dodge_error_null(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge(None, "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("Zuko", None)
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge(None, None)


    def test_dodge_error_empty(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("", "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("Zuko", "")
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.dodge("", "")



    #######################
	#    hit Errors     #
	#######################
    
    def test_hit_error_notinlist(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("Spongebob", "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("Zuko", "Spongebob")
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("Spongebob", "Spongebob")

    def test_hit_error_null(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit(None, "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("Zuko", None)
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit(None, None)


    def test_hit_error_empty(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("", "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("Zuko", "")
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.hit("", "")



    #######################
	#    catch Errors     #
	#######################
    
    def test_catch_error_notinlist(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Spongebob", "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Zuko", "Spongebob")
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Spongebob", "Spongebob")


    def test_catch_error_null(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall(None, "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Zuko", None)
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall(None, None)


    def test_catch_error_empty(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("", "Katara")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Zuko", "")
        
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("", "")


    def test_catch_error_catcher(self):
        # A typical DM (modified with hits):
        #   3 throwers: Zuko 1, Iro 0, Azula 1
        #   4 active dodgers: Aang 0, Katara 0, Sokka 0, Toph 0
        #   2 benched dodgers: Appa 0, Momo 0
        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Zuko", "Katara", "Spongebob")

        with self.assertRaises(ValueError):
            self._dm_typical_modifed.catchBall("Zuko", "Katara", "")