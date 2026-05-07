import os
import shutil

folder_path = r'C:\Users\rahul\Desktop\test'

file_types = {
    'images': ['.jpg', 'jpeg', '.png', '.gif'],
    'PDFs': ['.pdf'],
    'documents':['.doc', '.docx', '.txt'],
    'videos':['mp4', '.mkv', '.avi']
}

files = os.listdir(folder_path)
# print(files)

for file in files:
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):
        file_extension = os.path.splitext(file)[1].lower()
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_folder = os.path.join(folder_path, folder)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                    shutil.move(full_path, destination_folder)
    
    print(f"Moved {file} to {destination_folder}")