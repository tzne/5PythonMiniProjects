name = input("What's your name?\n").capitalize()
print(f"Welcome to this journey, {name}")

answer = input("You are on a dirty road, it has come to an end and you can go [left] or [right]. Which way wuold you go?").lower()

if answer == "left":
    answer = input("You come to a river. You can [walk] around it or [swim] accross").lower()

    if answer == "swim":
        print("You swam accross the river and were eaten by an alligator")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and died")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input("You come to a bridge. It looks wobbly. You can [cross] it or head [back]").lower()

    if answer == "back":
        answer = input("You cresso the bridge and meet a stranger. Do you talk to them? ([yes]/[no])").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win")
        elif answer == "no":
            print("You ignore the stranger and they are offended and kill you")
        else:
            print("Not a valid option. You lose.")

    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print(f"Thank you for playing, {name}")
