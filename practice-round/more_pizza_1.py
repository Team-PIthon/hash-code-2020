#import numpy
#import math
from sys import argv #used for getting desired input and output file names from the command line (shell script in this case)

#opening the input file
with open(argv[1]+".in", 'r') as f_in:
    #setting the input variables
    first_line = f_in.readline()
    goal, num_pizzas = [int(n) for n in first_line.split()]

    second_line = f_in.readline()
    pizzas_list = [int(n) for n in second_line.split()]

curr_pizzas = 0
curr_slices = 0
res = ()


for i in range(num_pizzas):
    if (curr_slices + pizzas_list[i]) < goal:
        curr_pizzas += 1
        curr_slices += pizzas_list[i]
        res += (i,)
    else:
        break



with open(argv[1]+".out", 'w+') as f_out:
    f_out.write(str(curr_pizzas)+'\n')
    for el in res:
        f_out.write(str(el)+" ")
