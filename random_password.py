# import statements
#Random Password Generator
import random
import string


def greeting():
    print("This programs makes your password more secure based on a word you provide!"
          + "\nIt increases the strenth of your password by adding random letters and digits before or after the word\n")


class password_generator():

    def __init__(self, word, length=8):
        self.word = word
        self.length = length

    def random_char(self):
        characters = string.ascii_letters + string.digits
        pass_list = []
        len_to_add = self.length - len(self.word)
        while len_to_add != 0:
            len_to_add -= 1

            random_chars = random.choice(characters)
            pass_list.append(random_chars)

        return pass_list

    def letters_to_add(self, to_add):
        list_word = list(self.word)
        length_of_to_add = len(to_add)

        while length_of_to_add != 0:
            popped = to_add.pop()
            rand_choice = random.randint(0, 1)

            if rand_choice == 0:
                list_word.insert(0, popped)

            elif rand_choice == 1:
                list_word.append(popped)

            length_of_to_add -= 1

        return list_word


def main():
    print('\n' * 10)
    greeting()
    word = input("Enter in a word for your random password: ")
    length_word = int(input("How many random characters do you want in your password: "))

    while len(word) > length_word:
        print('Sorry your word is longer than the passwords length')

        word = input("Enter in a word for your random password: ")
        length_word = int(input("How many random characters do you want in your password: "))

    users_password = password_generator(word, length_word)
    add_to_word = users_password.random_char()

    the_password = users_password.letters_to_add(add_to_word)

    print(f"\n\nYour new password is \n{''.join(the_password)}")


if __name__ == "__main__":
    main()
