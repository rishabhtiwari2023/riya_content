# Tests for gradebook module: checks reading and finding top student
from interview_projects.gradebook.gradebook import read_gradebook, find_top_students


def test_read_gradebook_and_top():
    # Read the sample file and check number of students and top student name
    students = read_gradebook('gradebook_sample.csv')
    assert len(students) == 3
    top = find_top_students(students)
    assert top and top[0]['name'] == 'Riya'
