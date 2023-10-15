# Image transformations

A collection of personal image transformation scripts.

## Usage (equal for all 3 subdirectories):
1. Create & activate venv (`python3 -m venv venv && source venv/bin/activate`)
2. Install packages from requirements.txt
2. Alter the config in settings.yaml to your need
3. Run main.py

## `alter_access_modified_time`

Alter photo creation time by manipulating access and/or modified time. This script comes to the rescue when receiving images without creation time metadata, with one of the consequences being that they aren't automatically ordered chronologocially. `main.py` alters the access and/or modified time to a time before the (incorrect) creation time (automatically, using the information from the file name), so that the creation time is automatically adjusted as well.

## `macos_metadata_spreadsheet`

Write important photo (capturing) settings into a spreadsheet. Specifically useful when photos require transformation to a different file system (exFAT in my case) that doesn't support specific types of metadata. After running this script, I can 

## `timelapse`

Create an mp4 video out of a series of still pictures of the same frame.