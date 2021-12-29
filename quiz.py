
import random
print("initialiser les boits")
boit1 = [i for i in range (40)]
boit2 = [j for j in range (40 ,80)]
somme =0 ;

while(boit1 !=[] or boit2 !=[]):
    print('prendre un allumentte ')
    randmeAllumentte = random.choice(boit1 + boit2)
    if randmeAllumentte in boit1 : boit1.remove(randmeAllumentte)
    elif randmeAllumentte in boit2 : boit2.remove(randmeAllumentte)
print(boit1)
print(boit2)

