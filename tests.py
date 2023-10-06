import pytest
import filereader

class TestFileReader:

    def test_read_file(self):
        data = filereader.read_file("data.json")
        assert isinstance(data, dict)
    
    def test_generate_new_emails(self):
        