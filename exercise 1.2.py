phrase = input("Tell me a sentence and I'll tell you approximately how long it would take you to say it: ")

split_words = phrase.split(" ")

cuantity_of_words = len(split_words)

print(f"You said {cuantity_of_words} words, and it would take you {cuantity_of_words/2} seconds to say it")

print(f"Dalto would say it in {cuantity_of_words / 2*1.3} seconds")

if cuantity_of_words >= 120:
    print("Hey, I told you a phrase, not the Bible.")