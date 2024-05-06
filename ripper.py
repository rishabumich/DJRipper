#!/usr/bin/env python3

import sys
import os
from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


DOWNLOAD_PATH = '/Users/rishab/Desktop/Music'

def main():
    if len(sys.argv) != 2:
        print("Bad usage")
        sys.exit(1)
    elif not isinstance(sys.argv[1], str):
        print("Give me a string URL to Rip")
        sys.exit(1)
    
    # isolate audio from youtube video
    you_tube = YouTube(sys.argv[1])
    audio_stream = you_tube.streams.get_audio_only()
    out_file = audio_stream.download(output_path=DOWNLOAD_PATH)

    # convert file to mp3 for download

    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    print(you_tube.title, "ripped successfully :)")


if __name__ == "__main__":
    main()