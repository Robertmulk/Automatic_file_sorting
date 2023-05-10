import os
import shutil

# Downloads folder address must be entered
download_folder = 'C:/Users/User/Downloads'


file_types = {
    'txt': 'Texts',
    'pdf': 'PDFs',
    'exe': 'Programs',
    'jpg': 'Images',
    'jpeg': 'Images',
    'png': 'Images',
    'gif': 'Images',
    'mp3': 'Music',
    'wav': 'Music',
    'flac': 'Music',
    'mp4': 'Movies',
    'avi': 'Movies',
    'mkv': 'Movies',
    # Add additional extensions and destination folders as needed
}

for filename in os.listdir(download_folder):
    if os.path.isfile(os.path.join(download_folder, filename)):
        file_extension = filename.split('.')[-1]
        if file_extension in file_types:
            destination_folder = os.path.join(download_folder, file_types[file_extension])
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(os.path.join(download_folder, filename), os.path.join(destination_folder, filename))

print("Done sorting files.")            
