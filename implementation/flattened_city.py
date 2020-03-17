import math

n,m = [int(i) for i in str(input()).split(" ")]
cities_with_space_station = sorted( [int(i) for i in str(input()).split(" ")] )

print("cities_with_space_station: ", cities_with_space_station)

distances = []
counter = 0
for i in range(0, n):
    distances.append( abs(cities_with_space_station[counter] - i))
    if i in cities_with_space_station:
        counter+=1

print(distances)
    

