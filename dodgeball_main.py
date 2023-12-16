import argparse
import time
from dodgeball_manager import DodgeballManager

def one_throw(dodgeball_manager : DodgeballManager):
    """ oneThrow
        Handles the details of handling one throw.
        
        Shows the current dodgeball positions,
        prompts the user for a thrower name,
        prompts the user for a target,
        then prompts the user for whether the throw was a hit or a dodge
    """
    # print current lists
    print("Throwers: ", end="")
    dodgeball_manager.printThrowers()
    print()
    print("Dodgers: ", end="")
    dodgeball_manager.printDodgers()
    print()
    print("Bench: ", end="")
    dodgeball_manager.printBench()
    print()


    # prompt for thrower
    print()
    thrower_name = input("Thrower name? ").strip()
    while not dodgeball_manager.isThrower(thrower_name):
        print("Not a thrower.")
        print()
        thrower_name = input("Thrower name? ").strip()
        
    # prompt for target
    print()
    target_name = input("Target name? ").strip()
    while not dodgeball_manager.isActiveDodger(target_name):
        print("Not an active dodger.")
        print()
        target_name = input("Target name? ").strip()
       
    # prompt for hit/dodge/catch
    print()
    choice = input("Was it a hit (h), dodge (d), or catch (c)? ").strip().lower()
    
    # handle the hit or dodge
    if choice.startswith("h"):
        # hit
        dodgeball_manager.hit(thrower_name, target_name)
    elif (choice.startswith("d")):
        # dodge
        dodgeball_manager.dodge(thrower_name, target_name)
    elif choice.startswith("c"):
        # catch
        print()
        if dodgeball_manager.nBenchedPlayers() > 0:
            # there are players on the bench to come back
            print("Which benched player will be brought back? ", end="")
            bench_back_name = input().strip()
            while not dodgeball_manager.isBenchedPlayer(bench_back_name):
                print("Not a benched dodger.")
                print()
                print("Which benched player will be brought back? ")
                bench_back_name = input().strip()
            dodgeball_manager.catchBall(thrower_name, target_name, bench_back_name)
        else:
            # empty bench
            dodgeball_manager.catchBall(thrower_name, target_name)
    
    # illegal choice
    else:
        print("Could not recognize action '" + choice + "'" )
    print()



def get_player_list():
    """ get_player_list()
    returns a list of players as read from standard input
    """
    # read in thelist as comma separated values
    unprocessed_list = input().strip().split(sep=",")

    # remove additional whitespace
    processed_list = list(map(lambda s: s.strip(), unprocessed_list))
    return processed_list


def run_interactive_session():
    """ run_interactive_session()
    runs an interactive dodgeball game through standard input
    """
    # read in throwers and dodgers as a comma-separated list, removing white space
    throwers = get_player_list()
    dodgers = get_player_list()

    dodgeball_manager = DodgeballManager(throwers, dodgers)

    # prompt the user for actions until the target score is reached
    while dodgeball_manager.nActiveDodgers() > 0:
        one_throw(dodgeball_manager)
    
    # report the winner(s)
    print()
    print("MVP(s): ")
    dodgeball_manager.printMVP()
    print()
    
    # report sorted scores
    print()
    print("All scores, in order:")
    dodgeball_manager.printSortedScores()
   

if __name__ == "__main__":
    run_interactive_session()

