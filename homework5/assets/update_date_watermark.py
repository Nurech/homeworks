import os
import datetime

def add_or_update_watermark(file_path, author, date):
    """Add or update watermark in the given file."""
    with open(file_path, 'r') as file:
        content = file.readlines()

    if content[0].startswith('%! Author') and content[1].startswith('%! Date'):
        content[0] = f'%! Author = {author}\n'
        content[1] = f'%! Date = {date}\n'
    else:
        content.insert(0, f'%! Date = {date}\n')
        content.insert(0, f'%! Author = {author}\n')

    with open(file_path, 'w') as file:
        file.writelines(content)

today = datetime.datetime.today().strftime('%d.%m.%Y')
project_dir = '../'
author_name = 'partsjoo'

for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.tex'):
            file_path = os.path.join(root, file)
            add_or_update_watermark(file_path, author_name, today)
