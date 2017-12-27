import unittest

from media.media import *



class TestMedia(unittest.TestCase):

    def test_get_dest_files(self):
        input = ['../files/bird1.avi', '../files/bird1   (copy).avi', '../files/bird.avi']
        expected = ['../out/bird1.mp3', '../out/bird1   (copy).mp3', '../out/bird.mp3']
        self.assertEqual(get_dest_files("mp3", "../out", input), expected)


    
    # add mock for get_original_files for the call to glob.glob
    # this function interacts with the filesystem
    def test_build_commands(self):
        old_files = ['../files/bird1.avi', '../files/bird.avi']
        new_files = ['../out/bird1.mp3',   '../out/bird.mp3']
        expected = ['ffmpeg ../files/bird1.avi ../out/bird1.mp3',
                    'ffmpeg ../files/bird.avi ../out/bird.mp3']
        audio_command = "ffmpeg {0} {1}"
        actual = build_commands(audio_command, old_files, new_files)
        self.assertEqual(build_commands(audio_command, old_files, new_files), expected)

        
if __name__ == '__main__':
    unittest.main()
