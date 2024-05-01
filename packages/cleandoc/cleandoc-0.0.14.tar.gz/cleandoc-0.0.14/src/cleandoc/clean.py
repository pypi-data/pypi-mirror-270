# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 12:18:08 2023

@author: jkris
"""

import logging

from . import helper as ch


def run_isort(pyfilepath: str, write: bool = True):
    """Run "isort" command on .py file via subprocess and check output.
    isort is a Python library to sort imports by name and type.

    Parameters
    ----------
    pyfilepath : str
        Full path to python (.py) file
    write : bool
        True = write the auto-formatted code in-place
    Returns
    -------
    str
        Summary of command outputs
    """
    # Auto-sort imports with isort
    isort_out, isort_err = ch.run_capture_out(["isort", pyfilepath, "--diff"])
    if write:
        isort_out, isort_err = ch.run_capture_out(["isort", pyfilepath])
    if len(isort_out.strip()) + len(isort_err.strip()) == 0:
        return ""
    isort_str = f"{ch.format_header('isort Output')}\n{isort_out}\n{isort_err}\n"
    logger = logging.getLogger("cleandoc")
    logger.debug(isort_str)
    return isort_str


def run_black(pyfilepath: str, write: bool = True):
    """Run "black" command on .py file via subprocess and check output.
    Black is a python package which auto-formats python code according to PEP8.

    Parameters
    ----------
    pyfilepath : str
        Full path to python (.py) file
    write : bool
        True = write the auto-formatted code in-place
    Returns
    -------
    str
        Summary of command outputs
    """
    # Auto-format code with black
    black_out, black_err = ch.run_capture_out(["black", pyfilepath, "--diff"])
    if write:
        black_out, black_err = ch.run_capture_out(["black", pyfilepath])
    black_str = f"{ch.format_header('Black Output')}\n{black_out}\n{black_err}\n"
    if "1 file" in black_str and "left unchanged" in black_str:
        return ""
    logger = logging.getLogger("cleandoc")
    logger.debug(black_str)
    return black_str


def run_pylint(pyfilepath: str):
    """Run "pylint" command on .py file via subprocess and check output.
    Pylint is a python package which checks for code cleanliness.

    Parameters
    ----------
    pyfilepath : str
        Full path to python (.py) file
    Returns
    -------
    str
        Summary of command outputs
    """
    # Check code cleanliness with pylint
    pylint_out, pylint_err = ch.run_capture_out(["pylint", pyfilepath])
    pylint_str = f"{ch.format_header('Pylint Output')}\n{pylint_out}\n{pylint_err}"
    if "Your code has been rated at 10.00/10" in pylint_str:
        return ""
    if len(pylint_out.strip()) + len(pylint_err.strip()) == 0:
        return ""
    logger = logging.getLogger("cleandoc")
    logger.debug(pylint_str)
    return pylint_str


def run_mypy(pyfilepath: str):
    """Run "mypy" command on .py file via subprocess and check output.
    Mypy is a python package which staticly checks variable types
    according to type hints.

    Parameters
    ----------
    pyfilepath : str
        Full path to python (.py) file
    Returns
    -------
    str
        Summary of command outputs
    """
    # Check variable type hints with mypy
    mypy_args = [
        "mypy",
        pyfilepath,
        "--check-untyped-defs",
        "--ignore-missing-imports",
        "--follow-imports=skip",
    ]
    mypy_out, mypy_err = ch.run_capture_out(mypy_args)
    mypy_str = f"{ch.format_header('Mypy Output')}\n{mypy_out}\n{mypy_err}"
    if "Success: no issues found" in mypy_str:
        return ""
    logger = logging.getLogger("cleandoc")
    logger.debug(mypy_str)
    return mypy_str
