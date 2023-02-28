import yaml
import os
from datetime import datetime
import time
import warnings

with open("settings.yaml") as s:
    config = yaml.safe_load(s)

folder = config["folder"]

for f in os.listdir(folder):
    path = f"{folder}{f}"
    file_name = "".join(f.split(".")[:-1])

    new_date_str = file_name if config["from_file_name"] else config["date_constant"]

    try:
        new_date = datetime.strptime(new_date_str, config["datetime_format"])
        print(f"Start altering time metadata of file '{path}' to '{new_date}'")
    except ValueError as e:
        warnings.warn(f"{e}; skipping and continuing with next file")
        continue

    new_date_u = time.mktime(new_date.timetuple())

    stat = os.stat(path)
    access_new = new_date_u if config["alter_access"] else stat.st_atime
    modified_new = new_date_u if config["alter_modified"] else stat.st_mtime

    os.utime(path, (access_new, modified_new))
