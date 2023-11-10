
def key_scheduling(key):
    keylength = len(key)
    s = [0]*256
    for i in range(255):
        s[i] = i
    j = 0
    for i in range(255):
        j = (j + s[i] + ord(key[i % keylength])) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
    return s

def psuedoRandom_Gen(s, repeats):
    i = 0
    j = 0
    for x in range(repeats):
        i = (i+1) % 256
        j = (j+s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        PSRNumber = s[(s[i]+s[j]) % 256]
        print(PSRNumber)

def get_psuedo_random_nums(key, r):
    s = key_scheduling(key)
    psuedoRandom_Gen(s, r)

def get_ciphertext(plaintext, key):
    plaintext = list(plaintext)
    ciphertext = []
    count = -1
    for letter in plaintext:
        count +=1
        new_letter = chr(int(bin(ord(letter))^bin(key[count])))
        ciphertext.append(new_letter)
         


key = "AQACS"
r = 256
get_psuedo_random_nums(key, r)

get_ciphertext("Compu", [241,99,212,73,127])
    