import os
import cv2 as cv

path = '@dataset copy'
dataset = os.listdir(path)

# Define target directories
target_dirs = ['palm', 'down', 'C', 'fist', 'fist-side', 'index', 'L', 'ok', 'palm-side', 'thumb']

# Create target directories if they don't exist
for dir_name in target_dirs:
    os.makedirs(dir_name, exist_ok=True)

for folder in dataset:
    inner_path = os.path.join(path, folder)
    dirs = os.listdir(inner_path)
    for subfolder in dirs:
        class_path = os.path.join(inner_path, subfolder)
        classes = os.listdir(class_path)
        for image in classes:
            image_path = os.path.join(class_path, image)
            img = cv.imread(image_path)
            
            # Determine the target directory based on subfolder name
            if subfolder.endswith('palm'):
                target_dir = 'palm'
            elif subfolder.endswith('down'):
                target_dir = 'down'
            elif subfolder.endswith('c'):
                target_dir = 'C'
            elif subfolder.endswith('fist'):
                target_dir = 'fist'
            elif subfolder.endswith('_fist_moved'):
                target_dir = 'fist-side'
            elif subfolder.endswith('index'):
                target_dir = 'index'
            elif subfolder.endswith('l'):
                target_dir = 'L'
            elif subfolder.endswith('ok'):
                target_dir = 'ok'
            elif subfolder.endswith('palm_moved'):
                target_dir = 'palm-side'
            elif subfolder.endswith('_thumb'):
                target_dir = 'thumb'
            else:
                target_dir = 'unknown'  # Handle any other cases
            
            # Save the image to the corresponding target directory
            if target_dir in target_dirs:
                target_path = os.path.join(target_dir, image)
                cv.imwrite(target_path, img)
            else:
                print(f"Skipping image {image_path} - Unknown class '{subfolder}'")
