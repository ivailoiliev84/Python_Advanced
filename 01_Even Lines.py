import re
with open('text.txt', 'w') as file:  # a file(text.txt) is created that will be used for the next task
    file.write('-I was quick to judge him, but it wasn\'t his fault.\n' #
               '-Is this some kind of joke?! Is it?\n'
               '-Quick, hide here. It is safer.')

with open('text.txt', 'r') as file:
    text = file.readlines()

for index, line in enumerate(text):
    if index % 2 == 0:
        pass
        line = re.sub('[-,.!?]', '@', line)
        line = ' '.join(reversed(line.split()))
        print(line)
