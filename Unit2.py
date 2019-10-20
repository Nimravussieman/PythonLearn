import random
import os
l = list(range(0,101,100//7))

def fPrint(percent):
    #print(percent,l)
    print(" -------")
    print(" |") if not percent > l[0] else print(" |     |")
    print(" |") if not percent > l[1] else print(" :     O")
    print(" |") if not percent > l[2] else print(" |     :")
    print(" |") if not percent > l[3] else print(" :  >--*--<")
    print(" |") if not percent > l[4] else print(" |     |")
    print(" |") if not percent > l[5] else print(" |     |")
    print(" |") if not percent > l[6] else print(" |    | |")
    print(" |") if not percent > l[7] else print(" |    | |")
    print(" |")
    print("---------------")




def func2():
    with open("Unit_words_dict","r") as f:
        wordsList = f.read().split("\n")
    #clear = lambda: os.system('cls')


    while True:
        wordForPrint = random.choice(wordsList)
        word = [x for x in wordForPrint]
        userWord = ["_" for x in word]
        attempts = len(word)
        correctAnswers = 0


        print("       New Game","    you have " + str(attempts) + " attempts", sep='\n')
        #clear()
        while attempts != 0 and len(word) != correctAnswers:
            ch = input("enter a letter: ") or " "

            #print("\033[H\033[J")
            #os.system('cls')
            #print("   your answer is: {}".format(ch[0]))

            try:
                index = word.index(ch[0])
                userWord[index] = word[index]
                word[index] = '|'
                correctAnswers += 1
                print("   correct answer! {} digits left to guess".format(len(word)-correctAnswers))
            except ValueError:
                attempts = attempts-1 if attempts == len(word)-correctAnswers - 1 else len(word)-correctAnswers - 1
                fPrint((1 - attempts / len(word))*100)
                print("   Incorrect answer! you have "+str(attempts)+" attempts")
                if attempts == 1:
                    print("   >-(now you will die)-<")
            print(''.join(userWord)+"\n\n")
        else:
            if attempts:
                print("Epic victory!", "you guessed the word: {}".format(''.join(userWord)),sep="\n")
            else:
                print("Did you hang yourself? Haah!","the word one was ordered: {}".format(wordForPrint),sep="\n")

        ch = input("do you want to play? y/n ")
        if ch == 'n':
            break

func2()

