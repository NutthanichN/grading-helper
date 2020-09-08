from typing import Union
import warnings

import unittest
from unittest import mock

import sys
import io

import importlib
from pathlib import Path

import itertools
import unrandomizer as random

STDIN = sys.stdin
STDOUT = sys.stdout


paths = Path('.').glob('files/*.py')
importlib.import_module('files.6210545505_lab4_task1')


def set_input(filepath: str):
    sys.stdin = open(filepath, 'r')


def reset_input():
    sys.stdin = STDIN


def set_output(filepath: str):
    sys.stdin = open(filepath, 'w')


def reset_output():
    sys.stdout = STDOUT


class Grade:
    """Represents a student's grade"""
    def __init__(self):
        self.scores = {}

    def get_score(self, lab_num: int):
        try:
            return self.scores[lab_num]
        except KeyError as e:
            raise ValueError("Student don't have lab", str(lab_num), "score") from e

    def add_score(self, lab_num: int, score: Union[int, float]):
        assert 0 <= score <= 100
        try:
            self.scores[lab_num]
        except KeyError:
            pass
        else:
            warnings.warn('score already exists')
        self.scores[lab_num] = score


class Student:
    """Represents a student"""
    @staticmethod
    def _to_valid_id(input_) -> str:
        """Check if `input_` is valid id

        Args:
            input_: The input to be checked

        Raises:
            ValueError: If input_ is of valid type but wrong value
            TypeError: If input_ is of invalid type

        Returns:
            A valid id
        """
        if isinstance(input_, int):
            input_ = str(input_)
        if isinstance(input_, str):
            if len(input_) == 10:
                return input_
            raise ValueError('Student ID should be of len 10 not ', len(input_))
        raise TypeError("Student ID should be of type 'str' or 'int'")

    def __init__(self, id_: Union[int, str], name: str):
        self.id = self._to_valid_id(id_)
        self.name = name
        self.grade = Grade()


def get_filepath(student: Student, lab_num: int, s: str) -> str:
    """Return the filepath to a python file to be graded

    Args:
        student: student to grade
        lab_num: number of lab to test
        s: string to append to the end after lab_num

    Examples:
        >>> get_filepath()

    """
    return 'files.' + student.id + '_lab' + str(lab_num) + s


class TestLab(unittest.TestCase):
    def setUp(self) -> None:
        assert sys.stdin is STDIN
        assert sys.stdout is STDOUT

    def tearDown(self) -> None:
        assert sys.stdin is STDIN
        assert sys.stdout is STDOUT

    def test_lab1():
        pass
