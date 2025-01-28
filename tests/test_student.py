# pylint: disable=missing docstring
import pytest

from src.student import get_logins


@pytest.fixture()
def file_student(tmpdir):
    filename = "data.txt"
    filename = tmpdir.join(filename)
    with open(filename, "w") as file_:
        file_.write("""Невеличка Проблема ; Immortalgleam
Най Буде;Immortalgleam
""")
    return filename

@pytest.fixture()
def file_student_wrong(tmpdir):
    filename = "data_wrong.txt"
    filename = tmpdir.join(filename)
    with open(filename, "w") as file_:
        file_.write("""Невеличка Проблема ; Immortalgleam
Най Буде;anetto-2
""")
    return filename

def test_student(file_student):
    sh_ans = [{'fio': 'Невеличка Проблема', 'login': 'Immortalgleam'},
              {'fio': 'Най Буде', 'login': 'Immortalgleam'}]
    ans = get_logins(file_student)

    assert ans == sh_ans

def test_student_wrong(file_student_wrong):
    sh_ans = [{'fio': 'Невеличка Проблема', 'login': 'Immortalgleam'},
              {'fio': 'Най Буде', 'login': 'Imortalgleam'}]
    with pytest.raises(RuntimeError):
        ans = get_logins(file_student_wrong)
