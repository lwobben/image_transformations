import cv2
import os
import yaml

with open("settings.yaml") as s:
    config = yaml.safe_load(s)

input_folder = config["folder_input"]
image_names = [
    img
    for img in os.listdir(input_folder)
    if img.endswith(f".{config['image_format']}")
]
image_names.sort()

if config["stack_method"]:
    if config["stack_method"] not in ["vconcat", "hconcat"]:
        raise ValueError(
            "Invalid 'stack_method' value, should be 'vconcat', 'hconcat' or None"
        )
    if not config["folder_input2"]:
        raise ValueError("'folder_input2' must be specified if 'stack_method' is set")
    input_folder2 = config["folder_input2"]
    image_names2 = [
        img
        for img in os.listdir(input_folder2)
        if img.endswith(f".{config['image_format']}")
    ]
    assert len(image_names) == len(image_names2)
    image_names2.sort()

shape = cv2.imread(os.path.join(input_folder, image_names[0])).shape
height, width, channels = shape
if config["stack_method"] == "vconcat":
    height = height * 2
elif config["stack_method"] == "hconcat":
    width = width * 2

fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
writer = cv2.VideoWriter(
    config["folder_output"], fourcc, config["speed"], [width, height]
)

for i in range(len(image_names)):
    print(f"Writing frame {i+1}")
    img = cv2.imread(os.path.join(input_folder, image_names[i]))
    assert img.shape == shape, "Dimensions of all images should be equal"

    if config["stack_method"]:
        img2 = cv2.imread(os.path.join(input_folder2, image_names2[i]))
        assert img2.shape == shape, "Dimensions of all images should be equal"
        img = getattr(cv2, config["stack_method"])([img, img2])

    writer.write(img)

cv2.destroyAllWindows()
writer.release()
