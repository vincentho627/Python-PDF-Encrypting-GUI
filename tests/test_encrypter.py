import os
import unittest
from unittest.mock import patch
from encrypter import Encryption
from tkinter import Label


class TestEncrypter(unittest.TestCase):
    def setUp(self):
        self.enc = Encryption()

    @patch('encrypter.filedialog.askopenfilename')
    def test_open_file__no_files_picked(self, _m):
        # Mock the return value of askopenfilename (_m)
        _m.return_value = ""

        file_name_label = Label()
        # Check if initially file label is empty
        assert file_name_label['text'] == ""
        self.enc.open_file(file_name_label=file_name_label)

        # Check if file label is updated without initial file
        assert _m.called is True
        assert file_name_label['text'] == ""

    @patch('encrypter.filedialog.askopenfilename')
    def test_open_file__one_file_picked(self, _m):
        # Mock the return value of askopenfilename (_m)
        _m.return_value = os.path.join(os.path.realpath("."), "tests/fixture/tester.pdf")

        file_name_label = Label()
        # Check if initially file label is empty
        assert file_name_label['text'] == ""
        self.enc.open_file(file_name_label=file_name_label)

        # Check if file label is updated without initial file
        assert _m.called is True
        assert file_name_label['text'] == "tester.pdf"

    @patch('encrypter.filedialog.askopenfilename')
    def test_open_file__two_file_picked_consecutively(self, _m):
        # Mock the return value of askopenfilename (_m)
        _m.return_value = os.path.join(os.path.realpath("."), "tests/fixture/tester.pdf")

        file_name_label = Label()
        # Check if initially file label is empty
        assert file_name_label['text'] == ""
        self.enc.open_file(file_name_label=file_name_label)

        # Check if file label is updated with initial file inputted
        _m.return_value = os.path.join(os.path.realpath("."), "tests/fixture/hello.pdf")
        self.enc.open_file(file_name_label=file_name_label)
        assert _m.called is True
        assert file_name_label['text'] == "hello.pdf"
