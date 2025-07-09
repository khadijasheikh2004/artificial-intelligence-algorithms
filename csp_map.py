import random

regions = ["WA","NT","SA","Q","NSW","V","T"]

adjancency = {
    "WA":["NT","SA"],
    "NT":["WA","SA","Q"],
    "SA":["WA","NT","Q","NSW","V"],
    "Q":["NT","SA","NSW"],
    "NSW":["Q","SA","V"],
    "V":["SA","NSW"],
    "T":[]
}
colors = ["Red","Greem", "Blue"]

def is_valid(region,color,assignment):
    for neighbour in adjancency[region]:
        if neighbour in assignment and assignment[neighbour] == color:
            return False
    return True

def backtrack(assignment,index=0):
    if index == len(regions):
        return assignment
    region = regions[index]
    for color in colors:
        if is_valid(region,color,assignment):
            assignment[region]=color
            if backtrack(assignment,index+1):
                return True
            
            del assignment[region]
    return False

def map_coloring():
    assignment = {}
    if backtrack(assignment):
        print(assignment)
    else:
        print("No solution found")
    
map_coloring()
