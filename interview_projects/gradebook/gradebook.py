"""Gradebook: read a CSV of student marks and compute averages and top students.

This module shows simple file I/O using csv and small data processing functions.
Functions are written to be easy to test (see tests/test_gradebook.py) and easy to explain in an interview.
"""
import csv
import sys


def read_gradebook(path):
    """Read a CSV gradebook and return a list of student dicts with numeric scores and average.

    Each row in the CSV should have columns: name, math, science
    The function converts string scores to integers and adds an 'avg' key.
    """
    students = []
    with open(path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert score strings to integers and compute average
            row['math'] = int(row['math'])
            row['science'] = int(row['science'])
            row['avg'] = (row['math'] + row['science']) / 2
            students.append(row)
    return students


def find_top_students(students):
    """Return a list of student dict(s) with the highest average.

    If multiple students share the top average, all are returned.
    """
    if not students:
        return []
    top_avg = max(s['avg'] for s in students)
    return [s for s in students if s['avg'] == top_avg]


if __name__ == '__main__':
    # Simple CLI demo: read a file path from argv or use a sample file
    path = sys.argv[1] if len(sys.argv) > 1 else 'gradebook_sample.csv'
    students = read_gradebook(path)
    print('Students and averages:')
    for s in students:
        print(f"{s['name']}: {s['avg']}")
    top = find_top_students(students)
    print('\nTop student(s):')
    for s in top:
        print(f"{s['name']} with avg {s['avg']}")
