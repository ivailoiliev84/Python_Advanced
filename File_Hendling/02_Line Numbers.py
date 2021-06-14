

with open('text.txt', 'r') as file:  # the file (text.txt) was created at task start (number-01) and is reused
    text = file.readlines()

for index, line in enumerate(text):
    letters = sum([len(word) for word in line.split()])
    punctuation = sum([1 for word in line.split() for punc in word if punc in r'-,\.!?\''])
    with open('output.txt', 'a') as file:
        file.write(f'Line {index}: {line} ({letters - punctuation})({punctuation}))\n')
