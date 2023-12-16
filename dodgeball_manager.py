#dodgeball_manager.py
#
# Author: Josiah Lam
# Email: j23lam@uwaterloo.ca
# Student ID: 21026577
#
# Source code for the DodgeballManager class

from list.linked_list import LinkedList
from dodgeball_player import DodgeballPlayer, name_map, score_map


class DodgeballManager:
    """ DodgeballManager
    A class to handle the main functionality of a one-sided Dodgeball game
    """


    def __init__(self, throwers : [str], dodgers : [str]):
        """ Constructor

        throwers: a Python list of thrower names (strings)
        dodgers: a Python list of dodger names (strings)
        """
        self._throwerList = LinkedList()
        self._dodgerList = LinkedList()
        self._benchList = LinkedList()

        #create and append players in respective lists

        #error: none
        if throwers == None or dodgers == None:
            raise ValueError("Please enter a thrower or dodger list")
        
        throwers = list(throwers)
        dodgers = list(dodgers)
        
        #error: empty
        if len(throwers) == 0 or len(dodgers) == 0:
            raise ValueError("Please enter a thrower or dodger list greater than 1")
        
        
        #append players in thrower list
        for ele in throwers:
            self._throwerList.append(DodgeballPlayer(ele))
            
        #append player in dodgers list
        for ele in dodgers:
            self._dodgerList.append(DodgeballPlayer(ele))
        

	###########################
	#    Boolean Accessors    #
	###########################

    def isThrower(self, name : str) -> bool:
        """ Returns True if a player named name is a thrower. """
        return self._FindPlayerHelper(name, self._throwerList)

    def isActiveDodger(self, name : str) -> bool:
        """ Returns True if a player named name is an active dodger. """
        return self._FindPlayerHelper(name, self._dodgerList)

    def isBenchedPlayer(self, name : str) -> bool:
        """ Returns True if a player named name is a benched dodger. """
        return self._FindPlayerHelper(name, self._benchList)

	#########################
	#    Count Accessors    #
	#########################


    def nBenchedPlayers(self) -> int:
        """Returns the number of benched players."""
        return self._benchList.length()

    def nActiveDodgers(self) -> int:
        """Returns the number of active dodgers."""
        return self._dodgerList.length()

    ####################
	# Private Function #
	####################
 
    def _FindPlayerHelper(self, PlayerName : str , Check_list : LinkedList) -> bool:
        """Returns True if a player named in inputed check list"""
        return Check_list.contains(value = PlayerName, map_to_key = name_map)
 
    def _get_index(self, PlayerName : str, Check_list: LinkedList) -> int:
        """Returns a interger index of the given PlayerName and check list  """
        return Check_list.find_index_byvalue(value = PlayerName, map_to_key=name_map)

	####################
	#    Main Logic    #
	####################

    def dodge(self, throwerName : str, dodgerName : str):
        """ dodge
            Conducts the main logic for a dodged throw.

            throwerName: the name of the thrower
            dodgerName: the name of the successful dodger
        """    
        #error: input none or empty string
        if throwerName == None or throwerName == "" or dodgerName == None or dodgerName == "":
            raise ValueError("Please enter a existing thrower or doger name in each list")
        
        #error: if throwerlist do not have throwerName 
        elif not self.isThrower(throwerName):
            raise ValueError("Please Enter a throwerName in thrower list")
        
        #error: if dodgerlist do not have dodgerName
        elif not self.isActiveDodger(dodgerName):
            raise ValueError("Please Enter a dodgerName in dodger list")
        
        else:
            #get dodger index
            dodger_index = self._get_index(dodgerName,self._dodgerList)
            
            #add a point for the dodger
            self._dodgerList.get(dodger_index).increment_score()   
            
        
        
    def hit(self, throwerName : str, dodgerName : str):
        """ hit
            Conducts the main logic for a successful throw.

            throwerName: the name of the successful thrower
            dodgerName: the name of the hit dodger
        """
        #error: input none or empty string
        if throwerName == None or throwerName == "" or dodgerName == None or dodgerName == "":
            raise ValueError("Please enter a existing thrower or doger name in each list")
        
        #error: if throwerlist do not have throwerName 
        elif not self.isThrower(throwerName):
            raise ValueError("Please Enter a throwerName in thrower list")
        
        #error: if dodgerlist do not have dodgerName
        elif not self.isActiveDodger(dodgerName):
            raise ValueError("Please Enter a dodgerName in dodger list")

        #if each list contains the throwerName or dodgerName
        else:
            #get thrower index
            thrower_index = self._get_index(throwerName, self._throwerList)
            dodger_index = self._get_index(dodgerName, self._dodgerList)
            
            #add a point for thrower
            self._throwerList.get(thrower_index).increment_score()
            
            #append dodger to bench list
            self._benchList.append(self._dodgerList.get(dodger_index))
            
            # remove dodger from dodger list
            self._dodgerList.remove(dodger_index)
                    

    def catchBall(self, throwerName : str, dodgerName : str, benchBackName : str = None):
        """ catchBall
            Conducts the main logic for a caught ball,
            which brings a player back from the bench.

            throwerName: the name of the thrower
            dodgerName: the name of the dodger who caught the ball
            benchBackName: the optional name of the dodger who caught the ball
        """
        #check if there are no bench players
        if self.nBenchedPlayers() <= 0: 
            #exit
            return

        #error: input none or empty string
        elif throwerName == None or throwerName == "" or dodgerName == None or dodgerName == "": 
            raise ValueError("Please enter a existing thrower or doger name in each list")
        
        #error: if throwerlist do not have throwerName 
        elif not self.isThrower(throwerName):
            raise ValueError("Please Enter a throwerName in thrower list")
        
        #error: if dodgerlist do not have dodgerName
        elif not self.isActiveDodger(dodgerName):
            raise ValueError("Please Enter a dodgerName in dodger list")
        
        elif self.nBenchedPlayers() > 0:
            #error: if benchlist do not have benchBackName
            if not self.isBenchedPlayer(benchBackName):
                raise ValueError("Please Enter a benchBackName in bench list")
            
            #error: input none or empty string for bench players
            elif benchBackName == "" or benchBackName == None: 
                raise ValueError("Please enter a benchBackName with that is not a empty string or null")

            #get index
            dodger_index = self._get_index(dodgerName, self._dodgerList)
            bench_index = self._get_index(benchBackName, self._benchList)
            
            #add a point for dodger who catch the ball
            self._dodgerList.get(dodger_index).increment_score()
            
            #insert bench player one after the stored index
            self._dodgerList.insert(dodger_index + 1, self._benchList.get(bench_index))
            
            #remove bench player from bench list
            self._benchList.remove(bench_index)
            
        
	#######################
	#    Main Printing    #
	#######################

    def printThrowers(self):
        """Prints the throwers to stdout."""
        for i in range(self._throwerList.length()):
            
            #print the players 
            if i == 0:
                print(f'{self._throwerList.get(i)}', end=",")

            #print the players 
            elif i > 0 and i < self._throwerList.length() -1:
                print(f' {self._throwerList.get(i)}', end=",")
            
            #print the last players
            elif i == self._throwerList.length() -1:
                print(f' {self._throwerList.get(i)}', end="")

        #print new line
        print()

    def printDodgers(self):
        """Prints the dodgers to stdout."""
        for i in range(self._dodgerList.length()):
            
            #print the players 
            if i == 0:
                print(f'{self._dodgerList.get(i)}', end=",")
            
            elif i > 0 and i < self._dodgerList.length() -1:
                print(f' {self._dodgerList.get(i)}', end=",")
            
            #print the last players
            elif i == self._dodgerList.length() -1:
                print(f' {self._dodgerList.get(i)}', end="")
                
        #print new line
        print()

    def printBench(self):
        """Prints the benched players to stdout."""
        for i in range(self._benchList.length()):
            
            #print the players 
            if i == 0:
                print(f'{self._benchList.get(i)}', end=",")
                
            elif i > 0 and i < self._benchList.length() -1:
                print(f' {self._benchList.get(i)}', end=",")
            
            #print the last players
            elif i == self._benchList.length() -1:
                print(f' {self._benchList.get(i)}', end="")
                
        #print new line
        print()


	##########################
	#    Complex Printing    #
	##########################
    def printMVP(self):
        """Prints out the MVP(s) like a standard list (with scores)."""
        
        #create a new Array list to store all players
        store_list = LinkedList()
        #create a new Array list to store mvp
        mvp_list = LinkedList()
        
        #get a player info from each list
        for i in range(self._throwerList.length()):
            store_list.append(self._throwerList.get(i))
                       
        for j in range(self._benchList.length()):
            store_list.append(self._benchList.get(j))
            
        #sort the list
        store_list.sort(map_to_key = score_map, descending = True)
                
        #find the mvp(s)
        for i in range(store_list.length()):
            #create a pointer j (next)
            j = i + 1

            #cross checking largest value
            largest_value = score_map(store_list.get(0))
                
            #if pointer j index is equal to the length of the list, exit
            #since it will raise an error in the LinkedList.get function
            if j == store_list.length():
                pass

            #check: if pointer i score equal to point j score
            #more than one mvp
            elif score_map(store_list.get(i)) == score_map(store_list.get(j)):

                if score_map(store_list.get(i)) == largest_value:
                #check: if pointer i (player) is in mvp_lisl
                #check: if pointer j (player) is in mvp_list
                
                    # if store_list.get(i) and (j) not in mvp_list:
                    if mvp_list.contains(store_list.get(i)) == False and mvp_list.contains(store_list.get(j)) == False:
                        
                        # print("add two - mult case")
                        #append both player who are mvp
                        mvp_list.append(store_list.get(i))
                        mvp_list.append(store_list.get(j))
                    
                    # elif only store_list.get(j) not in mvp_list:
                    elif mvp_list.contains(store_list.get(i)) == True and mvp_list.contains(store_list.get(j)) == False:
                        
                        # print("add one - mult case")
                        mvp_list.append(store_list.get(j))
                        
            #check: if pointer i score does not equal point j score
            #only one mvp
            elif mvp_list.contains(store_list.get(i)) == False and i == 0: #check: if appended already and if first element
                    # print("add one only")
                    # print()
                    mvp_list.append(store_list.get(i))
                    #only needed to append once, therefore break the loop
                    break

        #print the mvp(s)
            
        #only one mvp
        if mvp_list.length() == 1:
            #print the only mvp player
            print(f'{mvp_list.get(0)}')
        
        #more than one mvp
        else:
            for k in range(mvp_list.length()):
                
                #print the mvp player 
                if k < mvp_list.length() -1:
                    print(f'{mvp_list.get(k)} ', end=",")
                
                #print the last mvp player
                elif k == mvp_list.length() -1:
                    print(f'{mvp_list.get(k)}', end="")

                    
    def printSortedScores(self):
        """Prints out the sorted scores from highest to lowest, one on each line."""
        
        #create a temp LinkedList to store player info
        store_list = LinkedList()
        
        #get player info from thrower list and append to a temp list 
        for i in range(self._throwerList.length()):
            store_list.append(self._throwerList.get(i))
            
        #get player info from thrower list and append to a temp list 
        for j in range(self._dodgerList.length()):
            store_list.append(self._dodgerList.get(j)) 
          
        #get player info from bench list and append to a temp list             
        for k in range(self._benchList.length()):
            store_list.append(self._benchList.get(k))
            
        #sort list
        store_list.sort(map_to_key=score_map ,descending=True)
        
        #loop through the store list and print out result
        for u in range(store_list.length()):
            print(f'{store_list.get(u)}')
