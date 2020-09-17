This is a PDF encryption GUI interface done with tkinter in Python.
Python Requirements: 3.7.8
Useful files: encrypter.py, writer.py

Once you open the exe, you can input your passwords and choose your file. After inputting the informations, by pressing encrypt, it will make an encrypted version of the given files and name it (original file name)_protected.pdf

Encrypter.py contains a class that initialises the GUI interface and using the writer class in writer.py to encrypt pdf files. 


To make into EXE, run following command in terminal in this directory

pyinstaller -w -F encrypter.py

The EXE file will be contained in the dist directory (EXE file can be run without any external files)


To run tests, run following command in terminal in this directory

pytest tests
