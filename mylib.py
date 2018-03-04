import random as rn
import itertools as it
'''
@param 
This class is like the physical Sack in the game; In other words it contains all the letters with standart
quantities and their values. 
'''

class SakClass:
    def __init__(self):
        self.lets = {'Α': [12, 1], 'Β': [1, 8], 'Γ': [2, 4], 'Δ': [2, 4], 'Ε': [8, 1],
                     'Ζ': [1, 10], 'Η': [7, 1], 'Θ': [1, 10], 'Ι': [8, 1], 'Κ': [4, 2],
                     'Λ': [3, 3], 'Μ': [3, 3], 'Ν': [6, 1], 'Ξ': [1, 10], 'Ο': [9, 1],
                     'Π': [4, 2], 'Ρ': [5, 2], 'Σ': [7, 1], 'Τ': [8, 1], 'Υ': [4, 2],
                     'Φ': [1, 8], 'Χ': [1, 8], 'Ψ': [1, 10], 'Ω': [3, 3]}

        self.letlist = []   # A List with the letters of the players
        self.randomize_sak() #it Randomize the sack
        self.d = {} # a dictionary with all the possible words of the game as keys and 0 as value.
        with open("greek7.txt", "r", encoding="utf8") as myFile:
            for line in myFile:
                if line == '\ufeffΑΑΧ\n': #Removing the Signature of the file which is in the first line.
                    self.d['ΑΑΧ'] = 0
                else:
                    self.d[line.strip('\n')] = 0 # removing the \n chars

    '''
    This Function shows the quantity of letters remaining in the sack.
    '''
    def showSack(self):

        suma = 0
        for letters in self.lets:
            suma += self.lets[letters][0]
        print('~~~|Στο σακουλάκι έχει ', suma, 'γράμματα|~~~')
        return suma

    '''
    It randomize 2 times the sack
    '''
    def randomize_sak(self):
        for i in self.lets:
            for k in range(self.lets[i][0]):
                self.letlist.append(i)
        rn.shuffle(self.letlist)

    '''
    Fishing letters one by one and remove them from the sack
    '''
    def getletters(self, N):
        self.getlets = []
        while len(self.getlets) != N:
            let = rn.sample(self.letlist, 1)
            if self.lets[let[0]][0] > 0:
                self.lets[let[0]][0] -= 1
                self.getlets.append(let)
            if self.lets[let[0]][0] == 0:   #That means that there is no more of this letter
                continue
        # subtracting in self.lex!
        self.randomize_sak()
        if len(self.getlets) > 0:
            pass
        else:
            print('Πρεπει να σταματησει το παιχνιδι')
        return self.getlets

    '''
    When the player decides to change his/her letters: Quantinty of each letter is increased by one
    '''
    def putbackletters(self, L):
        # adding in self.lex!
        for i in L:
            if i[0] in self.lets:
                self.lets[i[0]][0] += 1
        self.randomize_sak()
    '''
    Calculate the points of the word
    '''
    def calculatePoints(self, word):

        suma = 0
        count = 0
        for letter in word:
            if letter in self.lets:
                suma += self.lets[letter][1]
        return suma

'''
Mother-Class of a physical and computer player inside it contains his/her letters (list) , name , score.
'''
class Player:
    def __init__(self, name, sk):
        self.name = name
        self.score = 0
        self.letterslist = sk.getletters(7)
    #Pirints The current letters of player whose turn is!
    def showLetters(self):
        for i in self.letterslist:
            print(i[0], end=' ')
        print('\n')

    '''
    When player write a valid word this function is called and it removes the letters which have been played
    '''
    def letterHandler(self, word, sk):
        for i in word:
            signif = 0
            for j in range(0, len(self.letterslist)):
                if (list(i) == self.letterslist[j] and signif == 0):
                    signif = 1
                    self.letterslist[j] = sk.getletters(1)[0]

    def addPoints(self, points):
        self.score += points

    def printScore(self):
        print('Ο παίχτης ', self.name, 'έχει ', self.score, 'πόντους')

    '''
    Taking back the 7 letters of the player and  returns 7 new ones.
    '''
    def changeLetters(self, sk):
        sk.putbackletters(self.letterslist)
        self.letterslist.clear()
        self.letterslist = sk.getletters(7)
'''
Sub - class of a player. here you can find the algorithms which are used from Pc-Player to play. 
'''

class PcPlayer(Player):
    # =======minLetters=======#
    def MinLetters(self, dict):
        for i in range(2, 7):
            myComb = list(it.permutations(self.letterslist, i))

            for j in myComb:
                s = ''
                for k in j:
                    s += k[0]
                if s in dict.keys():
                    return s

                else:
                    continue

                    # ========maxLetters=======#

    def MaxLetters(self, dict):
        for i in range(7, 2, -1):
            myComb = list(it.permutations(self.letterslist, i))

            for j in myComb:
                s = ''
                for k in j:
                    s += k[0]
                if s in dict.keys():
                    print(s)
                    return s

    # ==========Smart===========#

    def SmartPlay(self, dict, sk):
        word = ''
        for i in range(7, 3, -1):
            myComb = list(it.permutations(self.letterslist, i))

            for j in myComb:
                s = ''
                for k in j:
                    s += k[0]
                if s:
                    if s in dict.keys():
                        points = sk.calculatePoints(s)
                        sk.d[s] = points
                        if not word:
                            word = s
                        elif (points > sk.d[word]):
                            word = s

        return word
'''
This class is a Factory class that creates all the before. Initialize The sack the player the hardness of Pc-Player.
'''
class GamePlay:
    def __init__(self, hard):
        sk = SakClass()
        pc = PcPlayer('PC', sk)
        name = input('Δώσε το όνομα σου.\n')
        person = Player(name, sk)
        self.game(sk, pc, person, hard)

    def game(self, sk, pc, person, hard):
        word = ''
        num = 1
        while word != 'q' and num > 0:
            print('*================* New-Round *================*')
            num = sk.showSack()
            word = self.computerTurn(pc, sk, hard)
            if word == 'break':
                break
            word = self.playerTurn(sk, person)
            print('Οι συνολικοί πόντοι του Υπολογιστή είναι:\n', pc.score)
            print('Οι συνολικοί πόντοι σου είναι:\n', person.score)
        if (pc.score > person.score):
            print('PC: ΣΕ ΝΙΚΗΣΑ !!!')
        elif (pc.score < person.score):
            print('PC: ΕΧΑΣΑ , ΠΩΣ ΓΙΝΕΤΑΙ ΑΥΤΟ ;\nPC: ΠΑΜΕ ΑΛΛΟ ΕΝΑ ΤΩΡΑ!')
        else:
            print('PC: ΙΣΟΠΑΛΙΑ ΕΙΣΑΙ ΠΟΛΥ LUCKY')
        print("ΑΝΤΕ ΓΕΙΑ ! :)")
        name = person.name
        score = str(person.score)
        with open('history.txt', 'a+', encoding="utf8") as his:
            his.seek(0)
            if his.readline() == '':
                his.write('ΟΝΟΜΑ ΠΑΙΧΤΗ')
                his.write(7 * ' ')
                his.write('ΣΚΟΡ\n')

            his.write(name)
            number = 20 - len(name)
            his.write(number * ' ')
            his.write(score)
            his.write('\n')
    '''
    This is a Function that defines how pc plays.
    '''
    def computerTurn(self, pc, sk, hard):
        print('Ο υπολογιστής έχει τα εξής γράμματα: ')

        pc.showLetters()
        word = ''
        if hard == 1:
            word = pc.MinLetters(sk.d)
        elif hard == 2:
            word = pc.MaxLetters(sk.d)
        else:
            word = pc.SmartPlay(sk.d, sk)

        if word:
            print('O Υπολογιστής βρήκε :', word)
            pc.letterHandler(word, sk)
            pc.addPoints(sk.calculatePoints(word))
        else:
            print('PC: Νομίζω ότι ηρθε η ώρα να τελειώσουμε το παιχνίδι...')
            return 'break'

        print('Οι πόντοι που συγκέντρωσε ειναι: ', sk.calculatePoints(word))
        return word

    '''
    This is a Function that defines how human player plays.
    '''
    def playerTurn(self, sk, person):
        print(person.name, ' έχεις τα εξής γράμματα: ')

        word = ''
        # ====== letter-validation======#
        bool = 0
        bol = 0
        while bol == 0:
            person.showLetters()
            word = input('Παιζείς εσύ:\n')

            if word == 'q': #Player Exits game
                break

            elif word == 'p':   # Change All his letters! And Loses his turn too
                print("ΑΛΛΑΞΕ ΚΑΚΕ ΛΥΚΕ")
                person.changeLetters(sk)
                print("Τα καινούργια σου γράμματα είναι: ")
                print(person.showLetters())
                return ''

            for i in word:
                bool = 0
                for j in person.letterslist:
                    if i == j[0]:
                        bool = 1
                if bool == 0:
                    print('Έχεις χρησιμοποιήσει γράμματα τα οποία δεν έχεις')
                    break

            if bool == 1:# A valid word is found so we calculate the points and update the dictionary (Future use).
                if word in sk.d.keys():
                    points = sk.calculatePoints(word)
                    sk.d[word] = points
                    person.addPoints(points)
                    print('Οι πόντοι της λέξης σου είναι οι εξής: ', points)
                    bol = 1
                    person.letterHandler(word, sk)
                    print('Well done :) ')
                else:
                    print('Η λέξη που πληκτρολόγησες δεν υπάρχει: ')
                    # =================================
        return word