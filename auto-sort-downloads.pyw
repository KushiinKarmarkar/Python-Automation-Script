import time
import pathlib
import os
from pathlib import Path
import shutil

while True:
    source_dir= Path(r"C:\Users\Karmarkar\Downloads")
    extension= set()
    
    for file in source_dir.iterdir():
        if file.is_file():
            files=file.name        
            if file.suffix != "" and file.suffix != "tmp":
                ext = file.suffix.lstrip(".")
                extension.add(ext)
                print(extension)
    
    for ext in extension:
         folder_path= source_dir / ext
         if not os.path.exists(folder_path):
            folder_path.mkdir()
            print(f"Created folder: {ext}")
    
         for file in source_dir.iterdir():
            if file.is_file and file.suffix.lstrip('.') == ext:
                destination =  folder_path / file.name 
                if destination.exists():
                    counter = 1
                    new_name = f"{file.stem}({counter}){file.suffix}"
                    new_destination = folder_path / new_name

                    # Keep renaming until a unique name is found
                    while new_destination.exists():
                        counter += 1
                        new_name = f"{file.stem}({counter}){file.suffix}"
                        new_destination = folder_path / new_name

                    # ✅ Rename the file before moving
                    file = os.rename(file, new_destination)

                    destination = new_destination  # Update destination after renaming

                try:
                    shutil.move(str(file), str(destination))
                    print(f"Moved: {file.name} → {destination}")
                except Exception as e:
                    print(f"Error moving {file.name}: {e}")

    time.sleep(50);