word = "laptop"
with open("train.txt", "r") as text:
    for line in text:
        if word in line:
            print(line)