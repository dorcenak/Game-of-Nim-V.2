from inspect import getframeinfo, stack

from game_of_nim_v2 import NimII


def unittest(did_pass):
    """
    Print the result of a unit test.
    :param did_pass: a boolean representing the test
    :return: None
    """

    caller = getframeinfo(stack()[1][0])
    linenum = caller.lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def game_of_nim_test_suite():
    """
   This is a potential test suite that will be testing the different funtions of the main file

    :return: None
    """

    print("\n Running the game_of_nim_test_suite())")
    # The following tests test the create_label1() function
    # print("Testing create_label1()")
    # pass
    #
    # # The following tests test the create_label2() function
    # print("Testing create_label2()")
    # pass

    # The following tests test the text_box1() function
    # print("Testing text_box1()")
    # pass
    #
    # # The following tests test the text_box2() function
    # print("Testing text_box2()")
    # pass

    # The following tests test the fun_remove_balls() function

    # unittest(fun_remove_balls(12, 14) == 14)

    # Create an instance of the NimII class
    nim_instance = NimII(windowtext="")


    # The following tests the fun_remove_balls() function
    unittest(nim_instance.fun_remove_balls(10) == 14)
    unittest(nim_instance.fun_remove_balls(2) == 0)

    unittest(nim_instance.fun_comp_turn() == 14)
    print("\n Running the game_of_nim_test_suite())")


def main():
    """

    :return:
    """

    game_of_nim_test_suite()


if __name__ == "__main__":
    main()