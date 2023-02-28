A collection of simple scripts to solve metadata related issues with photos (or possibly other types of files).

Use: after you edited the config in settings.yaml to your need, run main.py in your venv with the packages from requirements.txt installed.

I personally sometime receive images without metadata information about creation time, that contain the creation time in their titles. (The creation time then automatically becomes the time my Mac received the photos.) When I get annoyed by my camera roll not being ordered chronologically, the script in `alter_access_modified_time` comes to the rescue. It alters the access and/or modified time to a time before the (incorrect) creation time (automatically, using the information from the file name), so that the creation time is automatically adjusted as well.

I store my photos taken with my DSLR camera on an external hard drive formatted in exFAT (most importantly for compatibility with both Mac and Windows computers). When I go through my photos on this drive, to decide which ones to edit or to remove for example, I would like to take the settings I used to take the picture (like the f-stop) in consideration. Unfortunately, this kind of metadata is not supported in exFAT. So, I always use the script in `macos_metadata_spreadsheet` to create a spreadsheet with the important settings, before I move the photos to the drive.
