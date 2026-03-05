'''
Author: Divija Saini
KUID: 3210396
Date: 3/5/2026
Lab: lab05
Last modified: 3/5/2026
Purpose: Captain's Log
'''
mission_over = 'n'
visited = []
visited_lower = []
while mission_over != 'y' and mission_over != 'Y':
    planet = input('Enter planet name: ')
    visited.append(planet)
    visited_lower.append(planet.lower())
    mission_over = input('Is the mission over? (y/n): ')
neighbor = input('Which planet do you want the neighbors for?: ')
print('Planet(s) neighboring', neighbor + ':')

neighbor1 = (visited_lower.index(neighbor.lower()) - 1)
if neighbor1 > 0:
    neighbor1 = visited[visited_lower.index(neighbor.lower()) - 1]
else:
    neighbor1 = ''

neighbor2 = (visited_lower.index(neighbor.lower()) + 1)
if neighbor2 < len(visited):
    neighbor2 = visited[visited_lower.index(neighbor.lower()) + 1]
else:
    neighbor2 = ''

print(neighbor1+'\n'+neighbor2)
print('Program Ending...')
