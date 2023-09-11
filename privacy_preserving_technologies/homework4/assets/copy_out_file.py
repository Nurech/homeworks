import os
import shutil
from datetime import datetime
import PyPDF2

def copy_pdf(source_path, dest_folder, dest_file_prefix, dest_file_suffix):
    dest_file_name = f"{dest_file_prefix}_{dest_file_suffix}.pdf"
    dest_path = os.path.join(dest_folder, dest_file_name)

    if not os.path.isfile(source_path):
        print(f"Source file '{source_path}' not found.")
        return

    if os.path.isfile(dest_path):
        os.remove(dest_path)

    shutil.copy(source_path, dest_path)
    print(f"Successfully copied the PDF file as '{dest_path}'")

if __name__ == "__main__":
    source_file = "../../out/main.pdf"
    dest_folder = ""
    dest_file_prefix = datetime.now().strftime("%d%b%y").upper()
    dest_file_suffix = "homework4_parts"

    copy_pdf(source_file, dest_folder, dest_file_prefix, dest_file_suffix)
