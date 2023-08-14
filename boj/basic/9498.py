if __name__ == "__main__":
    A = int(input())
    B = ''
    if (A >= 90 and A <= 100):
        B = 'A'
    elif (A >= 80 and A <= 89):
        B = 'B'
    elif (A >= 70 and A <= 79):
        B = 'C'
    elif (A >= 60 and A <= 69):
        B = 'D'
    else :
        B = 'F'
    print(B)