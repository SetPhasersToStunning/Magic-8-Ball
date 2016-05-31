#python3 syntax
import re
import random

number = random.randrange(1,20,1)
answers = [
    'It is certain','It is decidedly so','Without a doubt','Yes, definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate and ask again','Dont count on it','My reply is no','My sources say no','Outlook not so good','Very doubtful',
]

def PlayGame():
    print('What is your question? (yes or no answer):')
    question = input(">> ")

    match = re.match(r'^[A-Za-z ]*\??$', question) #regex for characters only and a question mark if added with spaces

    if match:
        print("thinking...")
        print('Your answer is: %s' %(answers[number]))
        PlayAgain()

    else:
        print("Invalid question (characters only) :(")

def PlayAgain():
    playagainanswer = input('Would you like to play again? (y/n)')
    if playagainanswer == 'y':
        PlayGame()
    else:
        quit()

PlayGame()
