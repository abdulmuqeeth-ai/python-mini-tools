import os
import shutil

def organize_files(folder_path):
    """Organize files by extension"""
    extensions = {
        'Images': ['.jpg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Python': ['.py'],
        'Data': ['.csv', '.json', '.xlsx']
    }
    
    for folder, exts in extensions.items():
        folder_dir = os.path.join(folder_path, folder)
        os.makedirs(folder_dir, exist_ok=True)
        
        for file in os.listdir(folder_path):
            if any(file.endswith(ext) for ext in exts):
                src = os.path.join(folder_path, file)
                dst = os.path.join(folder_dir, file)
                shutil.move(src, dst)
    
    print("Files organized successfully!")

# Usage
# organize_files("/path/to/your/folder")
