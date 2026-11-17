happy_words = ["happy", "good", "joy", "love", "great", "excited"]

sad_words = ["sad", "bad", "cry", "upset", "lonely", "unhappy"]

sentence = input("Enter a sentence: ")

text = sentence.lower()

happy_score = 0
sad_score = 0

for word in happy_words:
    if word in text:
        happy_score += 1

for word in sad_words:
    if word in text:
        sad_score += 1

if happy_score > sad_score:
    print("This sentence is Happy!")

elif sad_score > happy_score:
    print("This sentence is Sad!")

else:
    print("Cannot decide - Neutral!")