def longest_voca(text):
    voca = ""

    for i in text.split(" "):
        if len(i) > len(voca):
            voca = i
        else:
            continue
    print(voca, len(voca))


def additional_input(s):
    add_word = ""
    y_input = input("enter your additional input: ")

    for i in s.split(" "):
        count = 0
        i = i.strip(",.!")
        if y_input in i:
            for word in add_word.split("\n"):
                if i.lower() == word.lower():
                    count += 1
                    break
            if count == 0:
                add_word += i + "\n"

    print(add_word)


def one_of_upper(s):
    add_word = ""

    for i in s.split(" "):
        count = 0
        i = i.strip(",.!")
        for j in i:
            if j.isupper():
                for word in add_word.split("\n"):
                    if i.lower() == word.lower:
                        count += 1
                        break
                if count == 0:
                    add_word += i + "\n"
                    break

    print(add_word)


Fp = open("input.txt", "r")

text = Fp.read()

CyF = input("Choice your Function(1,2,3): ")

if CyF == "1":
    longest_voca(text)
elif CyF == "2":
    additional_input(text)
elif CyF == "3":
    one_of_upper(text)
