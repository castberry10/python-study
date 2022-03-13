import string

d = string.digits
p = string.punctuation


def Is_num_symbol(str):
    real_sr = ""
    for i in str:
        if i in d or i in p:
          real_sr += i

    print(real_sr)


st = input("your string: ")
Is_num_symbol(st)
