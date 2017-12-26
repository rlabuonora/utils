import unittest

from media.media import *

# file_list = ['../files/bird1.avi', '../files/bird1   (copy).avi', '../files/bird.avi']

class TestMedia(unittest.TestCase):

    def test_true(self):
        self.assertTrue(get_dest_files("", "", ""))

        
if __name__ == '__main__':
    unittest.main()
