#import statement

import random
import string
def greeting():
    print ("This random password generator is designed to make your passwords more secure by adding "
    + "\ncharacters like a $ or numbers along with the word you choose to enter!")

class password_generator(object):
    def __init__(word, length):
        
    def get_word(word):
        user_word = input("Enter in a word for your random password: ")
        random_char_choice = input("How many random characters do you want in your password")

        
        

    def random_char(length):
        characters = string.ascii_letters + string.digits
        random_chars = random.choice(characters)
        print (random_chars)

def main():
    random_char()

if __name__ == "__main__":
    main()
