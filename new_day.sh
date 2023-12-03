#!/usr/bin/env bash

NEW_FOLDER=day_$1
mkdir $NEW_FOLDER
cd $NEW_FOLDER
touch input
echo "from utils import open_file


def solution():
    values = open_file(\"$1\").split(\"\\n\")
    solution_1 = __solution_1(values)
    solution_2 = __solution_2(values)
    return (solution_1, solution_2)


def __solution_1(values: list[str]):
    return None


def __solution_2(values: list[str]):
    return None
" >> main.py