with open(r"HelpingWithStuff/2/input.txt", "r") as file:
    lines = file.readlines()

with open(r"HelpingWithStuff/2/output1.txt", "w") as file:
    for line in lines:
        file.write(line.split()[0] + "\n")
with open(r"HelpingWithStuff/2/output2.txt", "w") as file:
    for line in lines:
        file.write(line.split()[1] + "\n")
with open(r"HelpingWithStuff/2/output3.txt", "w") as file:
    for line in lines:
        file.write(line.split()[2] + "\n")