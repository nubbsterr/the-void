import time
import os

def SinglePWHash():
    """Hash a single given input"""
    os.system('cls')
    pw = str(input("Enter input: "))

    startHashTime = time.time()
    pw_hash = str(hash(pw))
    print(f"Hashed input: {pw_hash}")
    print(f"Hash time: {(time.time() - startHashTime)*10**3:0.3f} milliseconds")

def MultiPWHash():
    """
    Hashes multiple inputs given by user
    """
    global hashLight
    global multiPWHashTime
   
    hashList = []
    while True:
        os.system('cls')
        pw = str(input("Enter input: "))
        hashList.append(pw)
        stopInput = str(input("Continue to hash input(s)? (Y/N)\n\n$ "))
       
        match stopInput:
            case "Y":
                os.system('cls')
                break
            case "N":
                continue
   
    multiPWHashTime = time.time()
    for iteration, pw in enumerate(hashList):
        startHashTime = time.time()
        print(f"Iteration {iteration+1}\tHashed Password: {str(hash(pw))}\tHash time: {(time.time() - startHashTime)*10**3:0.3f} milliseconds")
   
    print(f"\nTotal hash time: {(time.time() - multiPWHashTime)*10**3:0.3f} milliseconds")

while True:
    mode = str(input("Hash 1) multiple passwords or 2) one password: "))
    match mode:
        case "1":
            MultiPWHash()
            break
        case "2":
            SinglePWHash()
            break
        case _:
            print("Misinput, select mode.")
            time.sleep(2)
            os.system('cls')
           
            continue