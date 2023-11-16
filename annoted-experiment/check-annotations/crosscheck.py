import os
import glob


side_folder_path = "D:/cow50gb/Pixel/B4/Side/annotations"
rear_folder_path = "D:/cow50gb/Pixel/B4/Rear/annotations"


side_images = glob.glob(os.path.join(side_folder_path, "*.jpg___fuse"))
rear_images = glob.glob(os.path.join(rear_folder_path, "*.jpg___fuse"))

common_identifiers = set()
for image_path in side_images + rear_images:
    filename = os.path.basename(image_path)
    identifier = filename.split("_")[2]  # Extract the "69" part from "1_b4-1_s_69_F.jpg___fuse"
    common_identifiers.add(identifier)


for identifier in common_identifiers:
    side_image_path = os.path.join(side_folder_path, f"*_{identifier}_s_*")
    rear_image_path = os.path.join(rear_folder_path, f"*_{identifier}_r_*")

    side_image_exists = len(glob.glob(side_image_path)) > 0
    rear_image_exists = len(glob.glob(rear_image_path)) > 0

    if side_image_exists and rear_image_exists:
        print(f"Both side and rear images exist for identifier {identifier}")
    else:
        print(f"Images missing for identifier {identifier}")
