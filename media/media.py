import sys
import os
import pipes
import glob


def get_dest_files(new_extension, new_location, original_files):
    # retrun a list of new files based on the original files
    new_names = [ os.path.splitext(os.path.basename(video_file))[0] for video_file in original_files ]
    new_files = [ os.path.join(new_location, "{}.{}".format(new_name, new_extension)) for new_name in new_names ]
    # return new_names
    return new_files

def get_original_files(source_location, extension):
    # returns a list of files to be ripped or converted
    return glob.glob(os.path.join(source_location, '*.{}'.format(extension)))
    

def run_commands(commands):
    # quotes and runs a list of commands
    [os.system(command) for command in commands]


def build_commands(command, old_files, new_files):
    # returns a str with the command to be run
    commands = [ command.format(pipes.quote(old_file), pipes.quote(new_file)) for old_file, new_file in zip(old_files, new_files)]
    return commands


def rip_audio(source, destination):
    original_files = get_original_files(source, "avi")
    new_files = get_dest_files("mp3", destination, original_files)
    audio_command = "ffmpeg -i {0} -vn -sn -c:a mp3 -ab 192k {1}"
    commands = build_commands(audio_command, original_files, new_files)
    run_commands(commands)

def compress_video(source, destination):
    original_files = get_original_files(source, "avi")
    new_files = get_dest_files("mp4", destination, original_files)
    audio_command = "ffmpeg -i {0} {1}"
    commands = build_commands(audio_command, original_files, new_files)
    run_commands(commands)


if __name__ == '__main__':
    source = sys.argv[1]
    dest = sys.argv[2]
    #rip_audio(source, dest)
    compress_video(source, dest)
    
