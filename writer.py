import os
from _md5 import md5

import PyPDF2
import PyPDF2.pdf as pdf
from PyPDF2.generic import ByteStringObject, ArrayObject, DictionaryObject, NameObject, NumberObject
from PyPDF2.utils import b_


class Writer(pdf.PdfFileWriter):

    def encrypt(self, user_pwd, owner_pwd=None, use_128bit=True):
        """
        Encrypt this PDF file with the PDF Standard encryption handler.

        :param str user_pwd: The "user password", which allows for opening
            and reading the PDF file with the restrictions provided.
        :param str owner_pwd: The "owner password", which allows for
            opening the PDF files without any restrictions.  By default,
            the owner password is the same as the user password.
        :param bool use_128bit: flag as to whether to use 128bit
            encryption.  When false, 40bit encryption will be used.  By default,
            this flag is on.
        """
        import time, random
        if owner_pwd == None:
            owner_pwd = user_pwd
        if use_128bit:
            V = 2
            rev = 3
            keylen = int(128 / 8)
        else:
            V = 1
            rev = 2
            keylen = int(40 / 8)
        # prevents everything:
        P = -3904
        O = ByteStringObject(pdf._alg33(owner_pwd, user_pwd, rev, keylen))
        ID_1 = ByteStringObject(md5(b_(repr(time.time()))).digest())
        ID_2 = ByteStringObject(md5(b_(repr(random.random()))).digest())
        self._ID = ArrayObject((ID_1, ID_2))
        if rev == 2:
            U, key = pdf._alg34(user_pwd, O, P, ID_1)
        else:
            assert rev == 3
            U, key = pdf._alg35(user_pwd, rev, keylen, O, P, ID_1, False)
        encrypt = DictionaryObject()
        encrypt[NameObject("/Filter")] = NameObject("/Standard")
        encrypt[NameObject("/V")] = NumberObject(V)
        if V == 2:
            encrypt[NameObject("/Length")] = NumberObject(keylen * 8)
        encrypt[NameObject("/R")] = NumberObject(rev)
        encrypt[NameObject("/O")] = ByteStringObject(O)
        encrypt[NameObject("/U")] = ByteStringObject(U)
        encrypt[NameObject("/P")] = NumberObject(P)
        self._encrypt = self._addObject(encrypt)
        self._encrypt_key = key

    def encrypting(self, input_file, user_password, owner_password):
        """makes a encrypted file with name encrypted__(original file)"""
        # gets path and filename to make a new encrypted_file
        path_to_file, filename = os.path.split(input_file)
        root, extension = filename.split(".")
        protected_filename = root + "_protected." + extension
        output_file = os.path.join(path_to_file, protected_filename)

        # initialise all PDF writers and readers
        output = Writer()
        try:
            input_reader = open(input_file, "rb")
            input_stream = PyPDF2.PdfFileReader(input_reader)

            for i in range(0, input_stream.getNumPages()):
                output.addPage(input_stream.getPage(i))

            editing = open(output_file, "wb")

            # sets password without given encrypt function
            output.encrypt(user_password, owner_password)
            output.write(editing)
        except:
            return False
        finally:
            editing.close()
            input_reader.close()

        return True

