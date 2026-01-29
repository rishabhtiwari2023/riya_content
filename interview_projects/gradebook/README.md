# Gradebook CLI

A small project that reads student scores from a CSV file and computes averages and top students. Good demo of file I/O, `csv` module, simple data processing, and presenting results.

How to run:
- `python gradebook.py gradebook_sample.csv`

Presentation script:
- Elevator pitch: "This reads a CSV of student marks, calculates averages and shows the top student(s). It demonstrates file handling and basic data aggregation."
- Show the CSV, describe `csv.DictReader`, and show the output of the script.
- Extension ideas: add CLI flags for sorting, write results to new CSV, or add per-subject statistics.

File guide:
- `gradebook.py` — `read_gradebook(path)` reads CSV and converts strings to integers and computes averages; `find_top_students(students)` finds top average(s).
- `gradebook_sample.csv` — example data used by the script and tests.
- `tests/test_gradebook.py` — simple tests that verify reading and top-student logic.

Tips for interview: show the CSV content, explain how dictionaries in the reader make it easy to access columns by name, and mention a possible improvement such as adding per-subject statistics or CLI options.
