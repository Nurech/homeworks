import os
import datetime

today = datetime.datetime.today().strftime('%d.%m.%Y')

project_dir = '../'

for root, dirs, files in os.walk(project_dir):
    for file in files:
        if file.endswith('.tex'):
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.readlines()

            if content[0].startswith('%! Author') and content[1].startswith('%! Date'):
                content[0] = '%! Author = partsjoo\n'
                content[1] = f'%! Date = {today}\n'
            else:
                content.insert(0, f'%! Date = {today}\n')
                content.insert(0, '%! Author = partsjoo\n')

            with open(file_path, 'w') as f:
                f.writelines(content)
