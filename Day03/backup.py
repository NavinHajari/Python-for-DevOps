import shutil # to create archvies
import os     # purpose of this library is not clear in this code
import datetime

def create_backup(source_path,destination_path):
    
    date_name = datetime.date.today()
    backup_name = os.path.join(destination_path,f"backup{date_name}")
    shutil.make_archive(backup_name,'gztar',source_path)
    print("Backup complete")

source_path = "/Users/navinsinghhajari/Python"
destination_path = "/Users/navinsinghhajari/backups"

create_backup(source_path,destination_path)