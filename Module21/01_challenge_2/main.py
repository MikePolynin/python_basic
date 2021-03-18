def challenge_2(num, i=1):
    if i == num:
        return num
    print(i)
    return challenge_2(num, i + 1)


print(challenge_2(10))
