#!/usr/bin/python

# Command line tool to convert avi files to mp4
# requires ffmpeg
# usage: compress .
# TODO: rip audio from video with this ffmpeg command
# ffmpeg -i video.mp4 -vn -sn -c:a mp3 -ab 192k audio.mp3
# per
# https://superuser.com/questions/892996/ffmpeg-is-doubling-audio-length-when-extracting-from-video
# TODO 2: specify destiantion folder as a second command line argument


import os
import glob
import sys

def build_command(avi_file):
    # create a conversion command from an avi file
    # avi_file -> "files/bird.avi"
    import pipes
    f = os.path.splitext(os.path.basename(avi_file))[0]
    mp4_filename = "{0}.mp4".format(f)
    mp4_full = pipes.quote(os.path.join(".", mp4_filename))
    command_template = "ffmpeg -i {0} {1}"
    ffmpeg_command = substitute_filenames(command_template, avi_file, mp4_full)
    return ffmpeg_command

def substitute_filenames(command, original_file, new_file):
    return command.format(original_file, new_file)

def build_commands(files):
    # builds commands for a list of files
    return [build_command(file) for file in files]

def run_commands(commands):
    # calls os.system on a list of commands
    # quote it here!
    [os.system(command) for command in commands]

def get_files(extension):
    # returns a list of all the files in a directory
    # with extension
    files = glob.glob(os.path.join(sys.argv[1], '*.avi'))
    return files

if __name__ == '__main__':
    files = get_files('.avi') # still works? use stubs to test out
    commands = build_commands(files)
    run_commands(commands)


