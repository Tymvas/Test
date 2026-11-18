import hashlib
import itertools

all_char = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

md5_hash = "6ef9a8f5ee25e9924d77b33d78fc329c"
text = '*HOm*1*y*zMU'

index_arr = list()

def check_md5(line):
    output = hashlib.md5(line.encode())
    return output.hexdigest() == md5_hash

num = 0
for item in text:
    if item == "*":
        index_arr.append(num)
    num += 1

for combination in itertools.product(all_char, repeat = len(index_arr)):
    for i in range(len(index_arr)):
        text = text[:index_arr[i]] + combination[i] + text[index_arr[i] + 1:]
        if check_md5(text):
            print(text)
            break