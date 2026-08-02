def minion_game(string):
    kevin = 0
    stuart = 0
    vowels = "AEIOU"
    
    # your code goes here
    for i in range(len(string)):
        points = len(string) - i
        if string[i] in vowels:
            kevin += points
        else:
            stuart += points

    if kevin > stuart:
        print("Kevin", kevin)
    elif stuart > kevin:
        print("Stuart", stuart)
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)