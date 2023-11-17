
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
    nums = []
    i = 0
    j = 0
    for x in range(repeats):
        i = (i+1) % 256
        j = (j+s[i]) % 256
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        PSRNumber = s[(s[i]+s[j]) % 256]
        nums.append(PSRNumber)
    return nums

def get_psuedo_random_nums(key, r):
    s = key_scheduling(key)
    return psuedoRandom_Gen(s, r)

def get_ciphertext(plaintext, key):
    plaintext = list(plaintext)
    ciphertext = []
    count = -1
    for letter in plaintext:
        count +=1
        letter = ord(letter)
        new_letter = letter^key[count]
        #ciphertext.append(hex(int(new_letter)))
        ciphertext.append(chr(int(new_letter)))
    return ciphertext
         


key = "AQACS"
r = 256
plaintext = "Computer Science"

key = get_psuedo_random_nums(key, r)
print(get_ciphertext(plaintext, key))
    