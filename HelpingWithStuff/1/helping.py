def stretch_line(line, max_width):
    words = line.split()
    if len(line) <= 1 or len(line) >= max_width or len(words) <= 1:
        return line

    total_spaces = max_width - len(line)
    spaces_between_words = total_spaces // (len(words) - 1)
    extra_spaces = total_spaces % (len(words) - 1)


    stretched_line = [words[0]]
    for i in range(1, len(words)):
        spaces = spaces_between_words + (1 if i <= extra_spaces else 0)
        stretched_line.append(' ' * spaces)
        stretched_line.append(words[i])

    return ''.join(stretched_line) + "\n"

with open(r"HelpingWithStuff/1/input.txt", "r") as file:
    lines = file.readlines()

max_width = 50

with open("HelpingWithStuff/1/output.txt", "w") as file:
    for line in lines:
        file.write(stretch_line(line, max_width))