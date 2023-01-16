# 6.2
guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number < guess_me:
        print("oops")
        break
    else:
        print("found it!")
        break
    number = number + 1