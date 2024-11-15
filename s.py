import pyfiglet
import cryptography
from cryptography.fernet import Fernet
import argparse
from pathlib import Path

def full_experience():
    title1 = pyfiglet.figlet_format("HIDE-IT\nPhantom\nLocker\nStealthGuard\n4000 000", font="smkeyboard", justify="center")
    title2 = pyfiglet.figlet_format("\nHIDE-IT\nPhantom\nLocker\nStealthGuard\n4000 000", font="binary", justify="center")
    print(title1)

    text1 = ("""\nTired of understanding what's in your files?!\n
    Want to avoid reading yesterday's nonsense!?\n
    Worried about leaving documents unread by people who don't care???\n\n

    Encrypt EVERYTHING that doesn't matter TODAY with the all-new:\n""")

    cen_text1 = "\n".join(line.center(80) for line in text1.splitlines())
    print(cen_text1)

    print(title2)

    text2 = ("""oh yeah I forgot you're mortal...\n\n- - - HIDE-IT PHANTOM LOCKER STEALTHGUARD 4000 000 - - -\n\n\n
    INSTRUCTIONS FOR HUMANS\n""")

    cen_text2 = "\n".join(line.center(80) for line in text2.splitlines())
    print(cen_text2)

    print("""
    Don't take it personal. Some instructions for dummies coming your way:\n
    You always begin with writing <python> (yes, without the pointy things)
    After that you need to write my file name <s.py> (see what I did there?)
    Now it's time for what you want me to do: <generate>, <encrypt> or <decrypt>
    If you want me to encrypt or decrypt I also need the file name (duh)\n
    Encryption will look like this: \033[32mpython s.py encrypt sillydoc.txt\033[0m\n
    If you forget to generate a key before you encrypt I'll do it for you (as usual) (happy to help!).
    See, wasn't so bad? Now let's get started, encrypt and decrypt something nobody cares about.\n\n\n\n
    \033[31m[WELL WELL WELL]\033[0m LOOK WHO MADE IT! Now scroll up and start from the beginning.\n""")

def generate_key():
    key = Fernet.generate_key()
    with open("created_key", "wb") as key_file:
        key_file.write(key)
    return key

## PROGRAM ##

print("""\n\033[34mFOR FULL EXPERIENCE TYPE:\033[0m python s.py more\n
Always with the waiting...\n""")

parser = argparse.ArgumentParser(description="[The unfriendly encryption tool by Tissika]")
parser.add_argument("o", choices=["generate", "encrypt", "decrypt", "more"])
parser.add_argument("file", nargs="?", type=str)
args = parser.parse_args()

if args.o == "more":
    full_experience()

if args.o == "generate": 
    key = generate_key()
    print(f"This pointless key (named created_key) is now ready to be used for encryption:\n{key.decode()}\n")

elif args.o == "encrypt":

    if args.file:
        file_name = args.file

        if '.' not in file_name or len(file_name.split('.')[-1]) == 0:
            print("I need a stupid file extension (.txt, .pdf, .jpg etc) to find your file.\n")
            exit()

        else:
            file_path = next(Path("C:/Users").rglob(file_name), None)
    
        if file_path is None:
            print(f"The file does not exist. Did you spell it wrong? Pathetic.\n")
            exit()

        else:
            if not Path("created_key").exists():
                key = generate_key()
                print("One ugly key has been created and is named: created_key\n")

            else:
                with open("created_key", "rb") as key_file:
                    key = key_file.read()
        
            fernet_key = Fernet(key)

        with open(file_path, "rb") as file:
            data = file.read()
        encrypted_data = fernet_key.encrypt(data)

        with open("enc_" + args.file, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
            print(f"The file {args.file} has been elimin... I mean encrypted and saved as enc_{args.file}\n")
        
    else:
        print("Want me to encrypt air? Choose a file moron.\n")

elif args.o == "decrypt":
    if args.file:
        file_name = args.file

        if '.' not in file_name or len(file_name.split('.')[-1]) == 0:
            print("You can't just skip the file extension (.txt, .pdf, .jpg etc) and expect me to work.\n")
            exit()

        if not Path(args.file).exists():
            print(f"The file does not exist. Did you spell it wrong? You never learn.\n")
        else:
            with open(args.file, "rb") as file:
                data = file.read()

            if Path("created_key").exists():
                with open("created_key", "rb") as key_file:
                    key = key_file.read()
            else:
                print("There is no key to decrypt the file with. Did you delete it? I knew you would screw up. Start over.\n")
                exit()

            fernet_key = Fernet(key)

            try:
                decrypted_data = fernet_key.decrypt(data)
                decrypted_file_name = args.file[4:]
                with open("dec_" + decrypted_file_name, "wb") as dec_file:
                    dec_file.write(decrypted_data)
                    print(f"The file {args.file} has been destro... I mean decrypted and saved as dec_{decrypted_file_name}\n")
            except cryptography.fernet.InvalidToken:
                print("This is not the right key! What are you up to?!\n")
                
    else:
        print("I can do a lot of shit but decrypting nothing isn't on the list. Choose a file.\n")
