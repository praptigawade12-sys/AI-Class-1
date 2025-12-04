print("Hello, I am an AI Chat bot! What is your name?")
name = input()

print(f"Nice to meet you {name}!")
print("How are you feeling today?(good/bad)")
mood = input().lower()

if mood == 'good':
    print("I am happy to hear that")
elif mood == 'bad':
    print("I am sorry to hear that, I hope you feel better soon")
else:
    print("I see, Sometime's its hard to putting your feeling into a word")

print(f"It was nice chatting with you {name}! Goodbye.")