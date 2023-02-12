import unittest


class TestFunction(unittest.TestCase): # Eric Salkovic
    # unit test class
    def testFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            open("testfile.txt")
            # test case to check if file 'testfile.txt' does not exist

    def testFileNotFound2(self):
        with self.assertRaises(FileNotFoundError):
            open("32100358.csv")
            # test case to check if file '32100358.csv' does not exist


