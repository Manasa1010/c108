import random
randomRolls=[]
import plotly.figure_factory as ff

for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    sum=dice1+dice2
    randomRolls.append(sum)

print(randomRolls)

fig=ff.create_distplot([randomRolls],["Results"],show_hist=False)
fig.show()