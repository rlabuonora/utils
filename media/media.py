import sys
import os
import pipes
import glob


def get_dest_files(new_extension, new_location, original_files):
    # retrun a list of new files based on the original files
    # new_names = [ os.path.splitext(os.path.basename(video_file))[0] for video_file in original_files]
    # return new_names
    return True

def get_original_files(source_location):
    # returns a list of files to be ripped or converted
    return glob.glob(os.path.join(source_location, '*.avi'))
    

def run_commands(commands):
    # quotes and runs a list of commands
    [os.system(pipes.quote(command)) for command in commands]


def interpolate_command(command, old_file, new_file):
    # returns a str with the command to be run
    ffmpeg_command = substitute_filenames(command, old_file, new_full)
    return ffmpeg_command


def rip_audio(source, destination):
    pass

def compress_video(source, destination):
    pass


