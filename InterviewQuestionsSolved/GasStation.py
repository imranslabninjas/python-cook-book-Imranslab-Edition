"""
Note that:
- We can only move forward
- The gas tank starts empty
- gas[i] represents the amount of gas at the station i
- cost[i] represents the cost to go from the station i to the next one
- the answer is guaranteed to be unique
- if the station we're searching for doesn't exist, return -1
"""

gas = [1, 5, 3, 3, 5, 3, 1, 3, 4, 5]
cost = [5, 2, 2, 8, 2, 4, 2, 5, 1, 2]

def can_traverse(gas, cost, start):
    remaining = 0
    n = len(gas)
    i = start
    started = False

    while i != start or not started:
        started = True
        remaining += gas[i] -cost[i]
        if remaining < 0:
            return False
        i = (i + 1) %n # It will divide by the length of the array and make it into a circular array
    return True

def gas_station(gas, cost):
    for i in range(len(gas)):
        if can_traverse(gas, cost, i):
            return i
    return -1

print(gas_station(gas, cost))
