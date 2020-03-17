import math

n,m = [int(i) for i in str(input()).split(" ")]
cities_with_space_station = sorted( [int(i) for i in str(input()).split(" ")] )

#print("cities_with_space_station: ", cities_with_space_station)


longest_chain = []
chains = []

for i in range(0,len(cities_with_space_station)):
    if len(cities_with_space_station) == 1 and cities_with_space_station[i] != 0:
        longest_chain.append(len(range(0, cities_with_space_station[i])))
    elif i == len(cities_with_space_station) -1:
        longest_chain.append(len(range(cities_with_space_station[i]+1, n)))
    elif i == 0 and cities_with_space_station[i] == 0:
        longest_chain.append(len(range(0, cities_with_space_station[i])))
        longest_chain.append(len(range(cities_with_space_station[i]+1, cities_with_space_station[i+1])))
    elif i == 0:
        longest_chain.append(len(range(0, cities_with_space_station[i])))
    else:
        longest_chain.append(len(range(cities_with_space_station[i]+1, cities_with_space_station[i+1])))


#longest_chain = sorted(longest_chain)
    
#print(longest_chain)
max_val = max(longest_chain)



if max_val == longest_chain[-1] or max_val == longest_chain[0]:
    print(max_val)
else:
    print((max_val + 1)//2)


    

