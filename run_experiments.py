# run_experiments.pyt
#
# Author: 
# Student ID:
# Email: 
#
# Use this program to run experiments and time methods that you implement
# Commenting can be light in this file
# Based on code by Oliver Schneider


import time
import random
from dodgeball_manager import DodgeballManager
from list.array_list import ArrayList



# Sorting experiments
def exp1_arraylist_sort():
    SIZE = 5000
    STEP = SIZE // 20 # 20 evenly sampled sizes

    # print header
    print(f"n|Sort Time (ms)")
    
    # create arrays of size n
    for n in range(0, SIZE, STEP):

        # create random array list of size n
        a = ArrayList()
        for i in range(n):
            # random integer between -1000 and 1000
            a.append(random.randint(-1000,1000))

        # setup timing
        start_time_s = time.time()
        
        # sort
        a.sort()

        # end time (should be immediately following the action)
        end_time_s = time.time()
        
        # print out recorded time in ms
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        print(f"{n}|{d_time_ms}")
         
         


# experiment with DodgeballManager "isThrower" method
def exp2_dm_isThrower():
    SIZE = 10000
    STEP = SIZE // 100 # 100 samples

    # make a thrower list
    thrower_list = []
    for i in range(0,SIZE):
        thrower_list.append(str(i))

    # create DodgeballManagers
    dm = DodgeballManager(thrower_list, ["dodger"])

    # test time for every 10 indices
    #print the header
    print("Index|isThrower Time (ms)")
    for i in range(0,SIZE, STEP):
        start_time_s = time.time()
        dm.isThrower(str(i))
        end_time_s = time.time()
        d_time_s = end_time_s - start_time_s
        d_time_ms = d_time_s * 1000
        print(f"{i}|{d_time_ms}")



if __name__ == "__main__":
    # call experiments here
    # comment out when done

    exp1_arraylist_sort()
    # exp2_dm_isThrower()