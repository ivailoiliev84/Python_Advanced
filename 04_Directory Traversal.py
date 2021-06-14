import os

_, _, filename = next(os.walk('.'))
sheet = {}
for file in filename:
    data = file.split('.')
    extension = data[-1]

    if extension not in sheet:
        sheet[extension] = []

    sheet[extension].append(file)

with open(os.path.expanduser('~/Desktop/report.txt'), 'w') as output_file:
    for extension in sorted(sheet.keys()):
        files = sorted(sheet[extension])
        output_file.write(f'.{extension}\n')
        for file in files:
            output_file.write(f'---{file}\n')


