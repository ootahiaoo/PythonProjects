# Rude words detector

import string

# Should have at least 3 letters (?)
rude_words = ["crap", "darn", "heck", "jerk", "idiot"]


def check_line(line):
    rude_count = 0
    words = line.split(" ")
    for word in words:
        word = word.strip("\n").strip(string.punctuation).lower()
        if word in rude_words:
            rude_count += 1
            print(f"Found rude word: {word}")
    return rude_count


def check_file(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count += check_line(line)
    if rude_count == 0:
        print("Congratulations, your file has no rude words.")


def replace_in_line(line):
    result = []
    words = line.split(" ")
    for word in words:
        checkword = word.strip("\n").strip(string.punctuation).lower()
        if checkword in rude_words:
            wordlength = len(word) - 1
            # Replace with bleep but keep first letter
            wordresult = word[0]

            if "\n" in word:
                wordlength -= 1

            # Append punctuation if necessary
            if word[wordlength] in string.punctuation:
                asterisks = "*" * (wordlength - 1)
                wordresult = wordresult + asterisks + word[wordlength]
            else:
                asterisks = "*" * wordlength
                wordresult = wordresult + asterisks

            result.append(wordresult)
        else:
            result.append(word)
    return " ".join(result)


def replace_in_file(filename):
    result = []
    with open(filename) as myfile:
        for line in myfile:
            newline = replace_in_line(line)
            result.append(newline)

    writefile = open(filename, "w")
    writefile.write("\n".join(result))
    writefile.close()


# Can use when imported (not when directly run)
if __name__ == "__rudewords__":
    check_file(filename)
    check_line(line)
    replace_in_file(filename)
    replace_in_line(line)
