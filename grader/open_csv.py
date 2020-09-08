from pathlib import Path
import csv
from typing import List


class Student:
    def __init__(self, student_id: str, name_en: str, name_th: str):
        self.id = student_id
        self.name_en = name_en
        self.name_th = name_th


def read(filepath: Path) -> List[Student]:
    students = []
    with filepath.open('r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            students.append(Student(*tuple(row)))
    return students



