import getpass
from math import log
import random

pCode = input("Enter Password:")

'''A strong password must have these requirements as of now:
- At least 8 characters long
- 1 special character
- 3 uppercase letters
'''

def generateWordPassword(minLength = 20, words = 1, returnText = True) -> str:
    password = ""
    acronym = "" #An acronym to help the person remember the password
    for _ in range(words):
        if len(password) < minLength + 7:
            word = random.choice(open("everyWord.txt","r").readlines())
            password = password.replace("\n", " ")
            password = password + word
            acronym = acronym + word[0].upper()
    if returnText:
        print(f"password is: {password}. A way to remember it is {acronym}") #print test
        strippedCode = password.strip()
        password = Password(strippedCode)
        return strippedCode
    else:
        strippedCode = password.strip()
        strippedCode = Password(strippedCode)
        passwordList = [strippedCode, acronym]
        print(passwordList)
        return passwordList

class Password:
    def __init__(self, passcode):
        self.password = passcode

    def getLength(self):
        return len(self.password)

    def getSpecial(self):
        return sum(not i.isalpha() or i.isdigit() for i in self.password)

    def getLower(self):
        return sum((i.islower()) for i in self.password)
    
    def getNumber(self):
        return sum(i.isdigit() for i in self.password)
    
    def getUpper(self):
        return sum(i.isupper() for i in self.password)
    
    def getSpaces(self):
        return self.password.count(' ')
    
    def save(self, filename = "password.txt"):
        with open(filename, 'a') as file:  
            file.write(f"\n{self.password}") 
            
    def checkStrength(self, returnText = False) -> str | float:
        passLen = self.getLength()
        if passLen == 0:
            return "Your variable is just an empty string."
        WEAK_MAX = 1/3
        entropyBits = int(self.getLength()) * log(self.getLength(), 2)
        if entropyBits <= 30:
            return WEAK_MAX * entropyBits / 30
        HARD_BITS = 30*3
        HARD_VAL = 0.950
        """ Get password strength as a number normalized to range {0 .. 1}.
        Normalization is done in the following fashion:
        1. If entropy_bits <= 30   -- linear in range{0.0 .. 0.33} (weak)
        2. If entropy_bits <= 30*2 -- almost linear in range{0.33 .. 0.66} (medium)
        3. If entropy_bits > 30*3  -- asymptotic towards 1.0 (strong)
        :param 30: Minimum entropy bits a medium password should have.
        :type 30: int
        :return: Normalized password strength:
            * <0.33 is WEAK
            * <0.66 is MEDIUM
            * >0.66 is STRONG
        :rtype: float
        """
        # https://github.com/kolypto/py-password-strength/blob/master/password_strength/stats.py
        k = -log((1 - HARD_VAL) / (1-WEAK_MAX), 2) / HARD_BITS
        f = lambda x: 1 - (1-WEAK_MAX)*pow(2, -k*x)
        score = round(f(entropyBits - 30) * 100,2)
        if returnText:
            print(f"Your password has a score of {score}%")
        else:
            return score


pass1 = generateWordPassword(words = 4)
print(pass1.checkStrength())



