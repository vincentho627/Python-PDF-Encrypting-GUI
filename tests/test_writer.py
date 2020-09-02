import os
import unittest
import PyPDF2
import writer


class TestWriter(unittest.TestCase):
    def test_os_path_split_cases(self):
        pathname, file = os.path.split("/Home/user/vho001/Desktop/hello.pdf")
        self.assertEqual("/Home/user/vho001/Desktop", pathname)
        self.assertEqual("hello.pdf", file)

    # Makes an encrypted tester.pdf file and test for right password and if it exists
    def test_encrypting_cases(self):
        w = writer.Writer()
        self.assertTrue(w.encrypting("tests/fixture/tester.pdf", "password", "password"))
        pdf_reader = PyPDF2.PdfFileReader("tests/fixture/encrypted_tester.pdf")
        self.assertTrue(pdf_reader)
        self.assertTrue(pdf_reader.decrypt("password"))
        self.assertFalse(pdf_reader.decrypt("hello"))


if __name__ == '__main__':
    unittest.main()
