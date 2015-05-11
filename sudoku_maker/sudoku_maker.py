# coding: utf-8
""" SudokuMaker Class """

import math
import random


class SudokuMaker(object):
    """ SudokuMaker """
    def __init__(self, trgt_num):
        self.__trgt_num = trgt_num
        self.__decision_num = int(math.sqrt(trgt_num))

    def make(self):
        """ make sudoku function
        """
        self.__make_source()

    def __make_source(self):
        """ make source
        """
        #arr = [1, 2, 3, 4]
        #random.shuffle(arr)
        #print(arr)
        g = [[0]*self.__trgt_num for i in range(self.__trgt_num)]
        g = [[1]*self.__trgt_num for i in range(self.__trgt_num)]
        print(g)
        print([0]*self.__trgt_num)

    def __shuffle_block_row(self):
        """ shuffle block row
        """
        pass

    def __switch_row_column(self):
        """ switch row column
        """
        pass


# @TODO debug
if __name__ == '__main__':
    sudoku_maker = SudokuMaker(4)
    sudoku_maker.make()
