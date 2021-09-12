import string
def ciper(text,number):
    t=string.ascii_lowercase
    j=t[number:] + t[:number]
    