# coding: utf-8
""" SudokuMaker Class """

import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')
from sudoku_maker.sudoku_maker import SudokuMaker


class TestSudoku(unittest.TestCase):

    def test_args1(self):
        sudoku_maker = SudokuMaker(4)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 4, "error")
        sudoku_maker = SudokuMaker(9)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 9, "error")
        sudoku_maker = SudokuMaker(16)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 16, "error")
        sudoku_maker = SudokuMaker(25)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 25, "error")
        sudoku_maker = SudokuMaker(36)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 36, "error")
        sudoku_maker = SudokuMaker(49)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 49, "error")
        sudoku_maker = SudokuMaker(64)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 64, "error")
        sudoku_maker = SudokuMaker(81)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 81, "error")
        sudoku_maker = SudokuMaker(100)
        check = sudoku_maker.make()
        self.assertEqual(len(check), 100, "error")
        sudoku_maker = SudokuMaker(3)
        check = sudoku_maker.make()
        self.assertNotEqual(len(check), 3, "error")
