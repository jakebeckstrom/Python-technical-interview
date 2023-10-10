import pytest
from filereader import FileReader


def test_read_file():
    data = FileReader("data.json").read_file()
    assert isinstance(data, dict)

def test_generate_new_emails():
    filereader = FileReader("data.json")
    data = filereader.read_file()
    new_emails = filereader.generate_new_emails(data)

    assert isinstance(new_emails, list)
    assert len(new_emails) == len(filereader.employees)

    for email in new_emails:
        assert "supercoolcompany.com" in email
        assert "gmail" not in email
        assert "yahoo" not in email

def test_get_all_new_employees():
    filereader = FileReader("data.json")
    data = filereader.read_file()
    new_employees = filereader.get_all_new_employees(data)

# def test_update_experience():
#     filereader = FileReader("data.json")
#     old_experience = [e.experience for e in filereader.employees]
#     filereader.update_experience()
#     new_experience = [e.experience for e in filereader.employees]

#     for i, j in zip(old_experience, new_experience):
#         assert int(j) - int(i) == 1

        