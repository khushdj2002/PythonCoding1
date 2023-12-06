def leapyear(year):
    leap = False
    if year//4==0:
        # nonlocal leap
        leap = True
        if year//400==0:
            leap = True
        elif year//100==0:
            leap=False

    return leap

print(leapyear(2000))

print(40%4)
print(1,end="")
print(1,end="")