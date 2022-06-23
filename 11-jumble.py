import random
wordlist=['race','bike','toy']
word=random.choice(wordlist)
correct=word
jumble="".join(random.sample(correct,len(correct)))
print(jumble)
while True:
    user_input =input("guess the word:").lower()
    if correct==user_input:
        print("correct")
        break
    else:
        print("not correct")