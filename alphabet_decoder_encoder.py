#Code encodes and decodes the latin alphabet based on this:
#The keyword cipher uses a keyword to rearrange the letters in the alphabet.
#A keyword is used as the key, which determines the letter matchings of the cipher alphabet to the plain alphabet.
#The repeats of letters in the word are removed, then the cipher alphabet is generated with the keyword matching to A, B, C, etc. until the keyword is used up, whereupon the rest of the ciphertext letters are used in #alphabetical order, excluding those already used in the key.

#example of usage at the last lines of the code
class Cipher:
    def __init__(self, operationalkey):
        self.operationalkey = operationalkey
        self.alphabet_to_use = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                                "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.crypto_alphabet = []
        self.departed_key = list(self.operationalkey)
        for i in range(len(self.departed_key)):
            self.departed_key[i] = self.departed_key[i].upper()
        self.helper_list = self.departed_key + self.alphabet_to_use
        for j in self.helper_list:
            if j not in self.crypto_alphabet:
                self.crypto_alphabet.append(j)

    def encode(self, data):
        encoded_data = ""
        char_converted = ""
        for k in data:
            if k != " ":
                if k.isupper():
                    helper_index = self.alphabet_to_use.index(k)
                    encoded_data += self.crypto_alphabet[helper_index]
                elif k.islower():
                    char_converted = k.upper()
                    helper_index = self.alphabet_to_use.index(char_converted)
                    encoded_data += self.crypto_alphabet[helper_index].lower()
            elif k == " ":
                encoded_data += " "
        print(encoded_data)
        return encoded_data

    def decode(self, data):
        decoded_data = ""
        char_converted = ""
        for k in data:
            if k != " ":
                if k.isupper():
                    helper_index = self.crypto_alphabet.index(k)
                    decoded_data += self.alphabet_to_use[helper_index]
                elif k.islower():
                    char_converted = k.upper()
                    helper_index = self.crypto_alphabet.index(char_converted)
                    decoded_data += self.alphabet_to_use[helper_index].lower()
            elif k == " ":
                decoded_data += " "
        print(decoded_data)
        return decoded_data

cipher = Cipher("crypto")
cipher.encode("Hello world")

cipher.decode("Fjedhc dn atidsn")

