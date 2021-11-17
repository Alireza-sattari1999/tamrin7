import random
boys = ['ali', 'reza', 'yasin','benyamin', 'mehrdad', 'sajjad', 'aidin', 'shahin']

girls = ['sara', 'zari', 'neda', 'homa', 'eli', 'goli', 'mary', 'mina']

marriage=[]


c=len(boys)

for i in range(c):

    if len(girls)==0:

        break

    a=random.choice(boys)

    b=random.choice(girls)
    boys.remove(a)

    girls.remove(b)

    couple=[a,b]

    marriage.append(couple)


print("results=",marriage)
print("goodbye😇")