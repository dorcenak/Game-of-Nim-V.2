######################################################################
# Author(s): Kichemy & Diego
# Username(s): dorcenak & coloradod
#
# Assignment: Final Project
#
# Purpose: Test some methods in the game_of_nim_v2.py file
######################################################################
# Acknowledgements: hw06: The Game of Nim by Kichemy & Jaela for the test file template
#                   Dr. Scott helped us understand how testing method of a class varies from testing a global function
#                   Python 360 Youtube channel. We used it as a blueprint to learn how to create unit t
#                   ests with classes.
#                   Link to the video we used: https://www.youtube.com/watch?v=WmJwA-ys39A&ab_channel=Python360
#
####################################################################################

from inspect import getframeinfo, stack
from game_of_nim_v2 import NimII


def unittest(did_pass, test_name):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :param test_name: name of the test
    :return: None
    """
    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = f"Test '{test_name}' at line {linenum} ok."
    else:
        msg = f"Test '{test_name}' at line {linenum} FAILED."
    print(msg)


def game_of_nim_test_suite():
    """
    Testing the methods that return a value in the game_of_nim_v2.py file
    :return: None
    """
    print("\n Running the game_of_nim_test_suite())")

    # Test 1: fun_remove_balls
    nim_instance = NimII(windowtext="")
    nim_instance.number_of_balls = 50
    unittest(nim_instance.fun_remove_balls(1) == 49, "fun_remove_balls")   # should pass
    unittest(nim_instance.fun_remove_balls(2) == 20, "fun_remove_balls")   # should fail
    unittest(nim_instance.fun_remove_balls(3) == 10, "fun_remove_balls")   # should fail
    unittest(nim_instance.fun_remove_balls(3) == 41, "fun_remove_balls")   # should pass
    unittest(nim_instance.fun_remove_balls(1) == 40, "fun_remove_balls")   # should pass
    unittest(nim_instance.fun_remove_balls(1) == 50, "fun_remove_balls")   # should fail

    # Test 2: fun_comp_turn
    nim_instance = NimII(windowtext="")
    nim_instance.number_of_balls = 17
    unittest(nim_instance.fun_comp_turn() == 2, "fun_comp_turn")           # should pass
    unittest(nim_instance.fun_comp_turn() == 4, "fun_comp_turn")           # should fail
    unittest(nim_instance.fun_comp_turn() == 2, "fun_comp_turn")           # should fail

    print("\n Finished running the game_of_nim_test_suite()")


def main():
    """
    :return: None
    """
    game_of_nim_test_suite()


if __name__ == "__main__":
    main()
