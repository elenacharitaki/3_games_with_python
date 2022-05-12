import random
import math

def chooseGame():
    game = int(input("Δι΄άλεξε παιχνίδι! \n Για να παίξεις 'Μάντεψε τον αριθμό' πληκτρολόγησε 1 \n Για να παίξεις Πέτρα-ψαλίδι-χαρτί πληκτρολόγησε 2 \n Για να παίξεις Mastermind πληκτρολόγησε 3 \n Για έξοδο πληκτρολόγησε 0\n"))
    if game == 1:
        guessTheNumber()
    if game == 2:
        paperRockScissors()
    if game == 3:
        mastermind()

   
    
def guessTheNumber():
    print("\n***********************************************")
    print("Μάντεψε τον αριθμό! \nΕπιλέγεται ένας τυχαίος αριθμός από 1 έως 100 και ο σκοπός είναι να μαντέψεις ποιος είναι αυτός.")
    print("Θα λαμβάνεις ένα μήνυμα για το αν ο αριθμός που μάντεψες είναι μικρότερος ή μεγαλύτερος από τον κρυμμένο αριθμό.")
    print("Έχεις 7 προσπάθειες!\n")
    tries = 0
    
    #hidden number
    number = int(random.random()*100//1)
    
    #7 rounds
    while tries < 7:
        #check user's input if it's a whole number in (0,100)
        userInput = False
        while userInput == False:
            try:
                guess = int(input("Διάλεξε έναν αριθμό από το 1 έως το 100: "))
                if guess < 100 and guess > 0:
                    userInput = True
            except:
                print("Διάλεξε έναν αριθμό από το 1 έως το 100: ")
        
        #compare hidden and user's number
        if guess > number:
            tries += 1
            print("Ο αριθμός {} είναι μεγαλύτερος από τον κρυμμένο αριθμό. Έχεις ακόμη {} προσπάθειες\n".format(guess, 7 - tries))
        elif guess < number:
            tries += 1
            print("Ο αριθμός {} είναι μικρότερος από τον κρυμμένο αριθμό. Έχεις ακόμη {} προσπάθειες\n".format(guess, 7 - tries))
        else:
            print("Μπράβο! Ο κρυμμένος αριθμός ήταν {}. Τον βρήκες με την {}η προσπάθεια!\n".format(number,tries))
            break
        
        if tries == 7:
            print("Δεν βρήκες τον κρυμμένο αριθμό στις 7 προσπάθειες... Παίξε ξανά!\n")
            break
        
    chooseGame()
        
def paperRockScissors():
    print("\n***********************************************")
    print("Πέτρα ψαλίδι χαρτί! \nΚερδίζεις αν φτάσεις πρώτος στις 3 νίκες. \n1: Πέτρα 2: Ψαλίδι 3: Χαρτί \nΠαίξε!\n")
    moves = {1:"Πέτρα", 2:"Ψαλίδι", 3:"Χαρτί"}
    computerWins = 0
    userWins = 0
     
    while userWins < 3 and computerWins < 3:
        userInput = False
        
        #computer's move
        number = random.random()
        if number < 1/3:
            computer = 1
        elif number < 2/3:
            computer = 2
        else:
            computer = 3
        
        #check users input if it is 1, 2 or 3
        while userInput == False:
            try:
                user = int(input("Η σειρά σου: "))
                if user == 1 or user == 2 or user == 3:
                    userInput = True
                else: 
                    print("1: Πέτρα 2: Ψαλίδι 3: Χαρτί\n")
            except:
                print("1: Πέτρα 2: Ψαλίδι 3: Χαρτί\n")
          
        #find the winner of this round
        if (computer == 1 and user == 1) or (computer == 2 and user == 2) or (computer == 3 and user == 3):
            print("Δάλεξες {}...\n".format(moves[user]))
            print("Ο αντίπαλος διάλεξε {}...\n".format(moves[computer]))
            print("Ισοπαλία!\n")
        elif (computer == 1 and user == 2) or (computer == 2 and user == 3) or (computer == 3 and user == 1):
            print("Δάλεξες {}...\n".format(moves[user]))
            print("Ο αντίπαλος διάλεξε {}...\n".format(moves[computer]))
            print("Έχασες σε αυτό το γύρο...\n")
            computerWins += 1
        elif (computer == 1 and user == 3) or (computer == 2 and user == 1) or (computer == 3 and user == 2):
            print("Δάλεξες {}...\n".format(moves[user]))
            print("Ο αντίπαλος διάλεξε {}...\n".format(moves[computer]))
            print("Κέρδισες το γύρο!\n")
            userWins += 1
            
    #announce the winner
    if userWins == 3:
        print("Μπράβο! Κέρδισες το παιχνίδι! Σκορ {}-{}".format(userWins, computerWins))
    if computerWins == 3:
        print("Έχασες... Σκορ {}-{} \nΠροσπάθησε ξανά!".format(userWins, computerWins))
        
    chooseGame()
    

def mastermind():
    print("\n***********************************************")
    print("Mastermind! \n\nΜία λίστα με 4 θέσεις θα γεμίζει με τυχαίους αριθμούς από 0 μέχρι 9, καθένας εκ των οποίων θα εμφανίζεται μόνο μία φορά.")
    print("Σκοπός σου είναι να διαλέξεις μία λίστα με 4 αρθμούς της επιλογής σου, ώστε τελικά να μαντεύεις την σωστή, με τα σωστά ψηφία στην σωστή σειρά.")
    print("Θα λαμβάνεις ένα μήνυμα που θα σε ενημερώνει πόσα σωστά ψηφία βρήκες συνολικά και πόσα στην σωστή θέση.")
    print("Για παράδειγμα, αν η λίστα στόχος είναι η [2,5,1,9] και μαντέψεις [4,5,9,0], θα λάβεις το μήνυμα: «υπάρχουν 2 σωστά ψηφία, το 1 σε σωστή θέση»")
    print("Το παιχνίδι τερματίζεται με 12 αποτυχημένες προσπάθειες.\n\n")
    hiddenList = []
    rounds = 1
    win = False
    
    #fill the hidden list
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    n1, n2, n3, n4 = random.sample(numbers, 4)
    
    hiddenList.append(n1)
    hiddenList.append(n2)
    hiddenList.append(n3)
    hiddenList.append(n4)

    while rounds <= 12 and win == False:
        usersList = []
        nums = 0
        
        print("{}ος γύρος!".format(rounds))
        #users guess
        print("Διάλεξε 4 αριθμούς από το 0 μέχρι το 9")
        while nums < 4:
            digits = 0
            positionDigits = 0
            
            #check users's input if it is a number in (0,9)
            #each number must be unique
            userInput = False
            while userInput == False:
                try:
                    user = int(input("{}ος αριθμός: ".format(nums+1)))
                    
                    # number from 0 to 9
                    if user < 10 and user >= 0:
                        
                        #number must be unique
                        if user not in usersList:
                            nums += 1
                            userInput = True
                        else:
                            print("Έχεις ήδη πει αυτόν τον αριθμό")
                    else:
                        print("Οι αριθμοί πρέπει να είναι από το 0 μέχρι το 9")
                    
                except:
                    print("Δεν έχεις εισάγει αριθμό")
            usersList.append(user)
            
        #compare the two lists
        for i in range(4):
            if usersList[i] in hiddenList:
                digits += 1
                if hiddenList[i] == usersList[i]:
                    positionDigits += 1
        print("Η λίστα σου ειίναι η {}, {}, {}, {}".format(usersList[0], usersList[1], usersList[2], usersList[3]))
        print("Έχεις {} σωστά ψηφία, {} στη σωστή θέση".format(digits, positionDigits))
        
        if positionDigits == 4:
            print("Μπράβο! Κέρδισες με την {}η προσπάθεια!\n".format(rounds))
            win = True
        else:
            print("Δεν βρήκες την λίστα στις 12 προσπάθειες... Παίξε ξανά!")
            
        rounds += 1
    
    chooseGame()
    
chooseGame()