# 📺 iwatch - TUI YouTube playlist manager
**Version 2.0**

This is a program that handels a youtube playlist for easier usage.

## ℹ️ About it in short
This program creates a new file with *pickle* module to save your watched history localy on the machine.
Since version 2.0 the program has been migrated to **yt-dlp** for fetching playlist data, and the output is now colored for better readability.

To start using this program, you just have to fill in two atributes in config file, (*file_name*, *playlist*):
* file_name - name your local data file
* playlist - url to the playlist

That's it, enjoy watching!

## ⌨️ Commands
* **watch, w [video_id]** - Opens up a video from a playlist
* **next, nxt, n** - Opens directly the next video in queue
* **watched, seen, s** - Shows all videos you have allready watched, id and video title inclusive
* **clear, cls, clc, c** - clears console
* **help** - shows all cmds you can run
* **quit, exit, close, q** - quits program
