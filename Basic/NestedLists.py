name1=[]
score1=0
name2=[]
score2=0
for _ in range(int(input())):
    name = input()
    score = float(input())
    if score>score1:
        score2=score1
        name2=name1
        score1=score
        name1=[name]
    elif score==score1:
        name1.append(name)
    elif score>score2:
        name2=[name]
        score=score2
    elif score==score2:
        name2.append(name)

print(name1)
print(name2)

str="hello"
if str == "hello":
    print(str)
