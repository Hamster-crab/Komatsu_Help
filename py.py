import random

for _ in range(10):
    x = random.uniform(2,-2)
    print (x)

    if x == -2:
        question = 2 * -2 + 5
        print(question)
    elif x == -1:
        question = 2 * -1 + 5
        print(question)
    elif x == 0:
        question = 2 * 0 + 5
        print(question)
    elif x == 1:
        question = 2 * 1 + 5
        print(question)
    elif x == 2:
        question = 2 * 2 + 5
        print(question)

# 2 * ikisugi.x + 5