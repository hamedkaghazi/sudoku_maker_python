# coding:utf-8
""" sudoku_maker """

from .sudoku_maker import SudokuMaker


def main(trgt_num=9):
    """ main

    Keyword arguments:
    trgt_num -- target number of sudoku
    """
    if trgt_num != 9:
        trgt_num = 9

    sudoku_maker = SudokuMaker()
    sudoku_maker.make()
