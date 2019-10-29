import os
import time
import getpass

def sublist(list, n):
    for i in range(0, len(list), n):
        yield list[i:i+n]

def encipher(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ 1234567890!\"$%&'()*+,-./:;<=>?@[\]_"
    res = ""
    for ltr in string:
        if ltr in alphabet:
            encipher_index = alphabet.find(ltr)+n
            if encipher_index >= len(alphabet):
                res += alphabet[encipher_index-len(alphabet)]
            else:
                res += alphabet[encipher_index]
        else:
            res += ltr
    return res

def decipher(string, n):
    alphabet = "abcdefghijklmnopqrstuvwxyzäöüßABCDEFGHIJKLMNOPQRSTUVWXYZÄÖÜ 1234567890!\"$%&'()*+,-./:;<=>?@[\]_"
    res = ""
    for ltr in string:
        if ltr in alphabet:
            decipher_index = alphabet.find(ltr)-n
            if decipher_index < 0:
                res += alphabet[decipher_index+len(alphabet)]
            else:
                res += alphabet[decipher_index]
        else:
            res += ltr
    return res


def encipher_key(string, key):
    if len(string) <= len(key):
        return "".join([enciphered for enciphered in map(encipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([enciphered for enciphered in map(encipher,string,key)])
        return res

def decipher_key(string, key):
    if len(string) <= len(key):
        return "".join([deciphered for deciphered in map(decipher,string,key)])
    else:
        str_segs = sublist(string, len(key))
        res = ""
        for string in str_segs:
            res += "".join([deciphered for deciphered in map(decipher,string,key)])
        return res

key = list(int(_) for _ in getpass.getpass("KEY: "))
print("1. DECRYPT FOLDER")
print("2. ENCRYPT FOLDER")
action = input("CHOOSE ACTION: ")

start_time = time.time()
file_counter = 0

if action == "1":
    for file in os.listdir("."):
        if file.endswith(".cv.txt"):
            file_counter += 1
            with open(file) as msg_file:
                msg = msg_file.read()
            deciphered_msg = decipher_key(msg,key)
            with open(file[:-7] + ".txt", "w") as output:
                output.write(deciphered_msg)
            os.system("rm " + file)
elif action == "2":
    for file in os.listdir("."):
        if file.endswith(".txt"):
            file_counter += 1
            with open(file) as msg_file:
                msg = msg_file.read()
            enciphered_msg = encipher_key(msg,key)
            with open(file[:-4] + ".cv.txt","w") as output:
                output.write(enciphered_msg)
            os.system("rm " + file)

end_time = time.time()
print(str(file_counter) + " files processed in " + str(round(end_time-start_time, 2)) + " second(s).")
