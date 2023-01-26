import random

LETTERS = "abcdefghijklmnopqrstuvwxyz"

def isLegalKey(key):

    key = key.lower()

    return ( len(key) == 26 and all( [ch in key for ch in LETTERS ] ))

def makeRandomKey():

    letter_list = list(LETTERS)

    random.shuffle(letter_list)

    return ''.join(letter_list)

def conversion_Dict(list1, list2):

    con_dict = {}
    
    for i in range(0, 26):

        con_dict[list1[i]] = list2[i]
    
    return con_dict

class SubstitutionCipher:

    def __init__(self, key = makeRandomKey()):
        self.__key = key

    def getKey(self):
        return self.__key
    
    def changeKey(self, newKey):

        self.__key = newKey

    def encryptFile(self, inFile, outFile):

        with open(inFile, 'r') as f:

            self.input_string = f.read()
        
        self.new_string = ""

        self.conversion_dict = conversion_Dict(LETTERS, self.__key)

        for ch in self.input_string:

            if ch.lower() in LETTERS:

                if ch.islower():

                    self.new_string += self.conversion_dict[ch]
                
                elif ch.isupper():

                    self.encoded_string = self.conversion_dict[ch.lower()]

                    self.new_string += self.encoded_string.upper()
            else:

                self.new_string += ch
        
        with open(outFile, 'w') as f:

            f.write(self.new_string)
    
    def decryptFile(self, inFile, outFile):

        with open(inFile, 'r') as f:

            self.input_string = f.read()
        
        self.new_string = ""

        self.conversion_dict = conversion_Dict(self.__key, LETTERS)
        
        for ch in self.input_string:

            if ch.lower() in self.__key:

                if ch.islower():

                    self.new_string += self.conversion_dict[ch]
                
                elif ch.isupper():

                    self.encoded_string = self.conversion_dict[ch.lower()]

                    self.new_string += self.encoded_string.upper()
            else:

                self.new_string += ch
        
        with open(outFile, 'w') as f:

            f.write(self.new_string)

def main():

    curr_instance = SubstitutionCipher()

    user_input = input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ")


    while user_input != "quit":
        

        if user_input.lower() == "getkey":

            print(f"Current cipher key: {curr_instance.getKey()}")
        
        elif user_input.lower() == "changekey":

            key_input = input("Enter a valid cipher key, \'random\' for a random key, or \'quit\' to quit: ")

            while key_input != 'quit':

                if isLegalKey(key_input):

                    curr_instance.changeKey(key_input)

                    print(f"New cipher key: {curr_instance.getKey()}")

                    break
                
                elif key_input == 'random':

                    curr_instance.changeKey(makeRandomKey())

                    print(f"New cipher key: {curr_instance.getKey()}")

                    break
                
                else:

                    print("Illegal key entered. Try again!")
                
                key_input = input("Enter a valid cipher key, \'random\' for a random key, or \'quit\' to quit: ")

        
        elif user_input.lower() == "encryptfile":

            user_file = input("Enter a filename: ")

            curr_instance.encryptFile(user_file + ".txt", user_file + "-Enc.txt")
        
        elif user_input.lower() == "decryptfile":

            user_file = input("Enter a filename: ")

            curr_instance.decryptFile(user_file + ".txt", user_file + "-Dec.txt")

        else:

            print("Command not recognized. Try again!")
        
        user_input = input("Enter a command (getKey, changeKey, encryptFile, decryptFile, quit): ")
    
    else:

        print("Thanks for visiting!")

main()