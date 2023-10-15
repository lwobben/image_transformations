import cv2
import os
import yaml

with open("settings.yaml") as s:
    config = yaml.safe_load(s)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter(config["path_output"], fourcc, config["speed"], config["size"])

input_folder = config["folder_input"]
images = [img for img in os.listdir(input_folder) if img.endswith(f".{config['image_format']}")]
for image in images:
    print(image)
    writer.write(cv2.imread(os.path.join(input_folder, image)))

cv2.destroyAllWindows()
writer.release()
