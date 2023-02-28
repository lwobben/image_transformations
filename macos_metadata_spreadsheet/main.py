import yaml
import os
import subprocess
import warnings
import csv

with open("settings.yaml") as s:
    config = yaml.safe_load(s)

folder = config["folder"]

with open("output.csv", "w") as output_file:
    writer = csv.writer(output_file)
    metadata_names = config["required_data"]
    metadata_names.sort()
    writer.writerow(["file"] + metadata_names)

    for f in os.listdir(folder):
        path = f"{folder}{f}"

        try:
            cmd_out = subprocess.check_output("mdls " + path, shell=True)
            print(f"Start extracting metadata from file '{path}'")
        except subprocess.CalledProcessError as e:
            warnings.warn(f"{e}; skipping and continuing with next file")
            continue

        out_list = cmd_out.decode("utf-8").split("\n")
        out_dict = {
            i.split("=")[0].strip(' "').lstrip(config["prefix"]): i.split("=")[-1].strip(' "')
            for i in out_list
        }
        metadata_dict = {k: out_dict.get(k) for k in metadata_names}
        writer.writerow([f] + [v for k, v in sorted(metadata_dict.items())])
