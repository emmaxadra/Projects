import random
import time
import sys

def quiz():
    timeout = 7#time for the game to end is 7sec
    time_start = time.time()

    questions = []  #empty list to append the other lists
    qu1 = [0,"the date of today is?\n(a)23\n(b)12\n(c)39", 'a']
    qu2 = [0,"today is?\n(a)monday\n(b)tuesday\n(c)wednesday", 'b']
    qu3 = [0,"i got how many phones\n(a)8\n(b)76\n(c)98", 'a']
    qu4 = [0,"what is the name of america president\n(a)asa\n(b)akon\n(c) bill_gate",'c']
    qu5 = [0, "where is nigeria located?\n(a)africa\n(b)europe\n(c)asia",'a']
    qu6 = [0,"what year was the second world war\n(a)1942\n(b)1950\n(c)1970",'a']
    score = 0 #score increase by 2 when you get any question right

    questions.append(qu1) #appending the other list to ll
    questions.append(qu2)
    questions.append(qu3)
    questions.append(qu4)
    questions.append(qu5)
    questions.append(qu6)


    random.shuffle(questions) #shuffling the question with the help of ramdom
    for i,j,k in questions:
        print(j)
        ans = input("enter the correct option:").lower()

        while True:
            i = time.time()-time_start
            if i >= timeout:
                print("game over\nyour total score is:",score)
                sys.exit() #exit the game when the time limit is reached and print the final score.
            elif ans == k:
                time.sleep(0.1)
                score += 2
                print("correct: +2")
                print('')
                break
            else:
                print("wrong:", score)
                print("")
                break
quiz()
