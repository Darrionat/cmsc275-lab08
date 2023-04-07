# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 13:32:15 2021
from https://realpython.com/python-csv/
@author: Kerri-Ann Norton
"""

import csv


def load_data(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        line_count = 0
        data = []
        for row in reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                for i in range(len(row)):
                    row[i] = float(row[i])
                data.append(row)
                line_count += 1
        print(f'Processed {line_count} lines.')
        return data
