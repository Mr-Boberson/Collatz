from bitarray import bitarray, decodetree
from bitarray.util import ba2int
import matplotlib.pyplot as plt
import operator
from collatz_generator import CollatzGenerator

gen = CollatzGenerator(7)
gen.generate()

# d = decodetree({'0': bitarray('0'), '1': bitarray('1')})

# a_values = [[[1, bitarray('')]]] #A list that contains a list of values for each level. 
# set_values = {1}

# n = 20 #Final value
# c = 1 #Starting level

# #Loop from c to n
# while not c > n:
#     #Append a new list for the level
#     a_values.append([])

#     #Loop through the values in the previous list
#     for list in a_values[c - 1]:
#         #Generate an entry for the times 2 value(created for each previous value)
#         t_possible = list[0] * 2
#         if t_possible not in set_values:
#             a_values[c].append([t_possible, bitarray('0' + ''.join( bitarray(list[1]).decode(d)))])
#             set_values.add(t_possible)

#         # #Generate an entry for the three n value(created for each previous value)
#         a_possible = (list[0] - 1) / 3
#         if a_possible % 1 == 0 and a_possible % 2 == 1 and a_possible not in set_values:
#             a_values[c].append([(list[0] - 1) / 3, bitarray('1' + ''.join(bitarray(list[1]).decode(d)))])
#             set_values.add(a_possible)
#     c += 1

# #Format some output
# final_list = []
# for list_a in a_values:
#     final_list.extend(list_a)

# sorted_list = sorted(final_list, key=operator.itemgetter(1))

# with open(, 'w') as f:
#     f.write("value\t\tcode\n")
#     for item in sorted_list:
#         if len(bitarray(item[1])) > 0:
#             f.write("{}\t\t{}\t\t{}\n".format(item[0], ''.join(bitarray(item[1]).decode(d)), ba2int(bitarray(item[1]))))
#         else:
#             f.write("{}\t\t{}\t\t{}\n".format(item[0], ''.join(bitarray(item[1]).decode(d)), None))


# fig = plt.figure()
 
# # syntax for 3-D projection
# ax = plt.axes(projection ='3d')
# x = []
# y = []
# z = []

# for item in final_list:
#     x.append(len(bitarray(item[1])))
#     y.append(item[0])
#     if len(bitarray(item[1])) > 0:
#         z.append(ba2int(bitarray(item[1])))
#     else:
#        z.append(0)     
#     # ax.text(len(bitarray(item[1])),item[0],ba2int(bitarray(item[1])),  (len(bitarray(item[1])),item[0],ba2int(bitarray(item[1]))), size=5, zorder=1,  
#     # color='black') 

# ax.scatter(x, y, z)
# # # plt.scatter(x, y, label= "stars", color= "black",  
# # #             marker= "*", s=10)
# # # x-axis label 
# ax.set_xlabel('x - Generated distance from 1', fontweight ='bold') 
# ax.set_ylabel('y - Decimal value', fontweight ='bold') 
# ax.set_zlabel('z - Integer value of Collatz code', fontweight ='bold')
# # plt.xlabel('x - Generated distance from 1') 
# # # # frequency label 
# # plt.ylabel('y - Decimal value')

# # plt.zlabel('z - Integer value of Collatz code')

# # function to show the plot 
# ax.set_title('3d Scatter plot of values relating to collatz code')
# plt.show()