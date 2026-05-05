import shutil # to create archvies
import os     # purpose of this library is not clear in this code
import datetime

def create_backup(source_path,destination_path):
    
    date_name = datetime.date.today()
    backup_name = os.path.join(destination_path,f"backup{date_name}")
    try: #Exception Handling
        shutil.make_archive(backup_name,'gztar',source_path)
        print("Backup complete")
    except Exception as e:
        print(e)

source_path = input("Enter source path") # "/Users/navinsinghhajari/Python"
destination_path = input("Enter destination path") # "/Users/navinsinghhajari/backups"

create_backup(source_path,destination_path)