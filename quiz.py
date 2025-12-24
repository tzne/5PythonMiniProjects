print("Welcome to my computer quiz")

playing = input("Do you want to play?\n")
print(playing)

if playing.lower() != "yes":
    quit()

print("Okay! Let's play")
score = 0

answer = input("What dows CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What dows GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What dows RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What dows PSU stand for? ")
if answer.lower() == "power supply":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {score} questions correct! ({score/4 * 100} %)")
