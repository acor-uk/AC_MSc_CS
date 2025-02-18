import random as rnd

vals = []

def getMean(total, count):
    return total / count

for i in range(100):
    temp = [rnd.randint(1,100),rnd.randint(500,1000)]
    vals.append(temp)
    
#print(vals)

temps = []
for val in vals:
    print(val[0])
    temps.append(val[0])
    
print(getMean(sum(temps),len(temps)))
