#levenstein.py 

#ensure you had numba module install
#pip install numba
#if your python ver is 3.11.1, it may not compatible with numba 
#can try use python ver that is 3.9.x or 3.10.x

import numpy
from numba import njit

@njit 
def levenshteinDistanceDP(token1, token2):
    
    # token1- original word
    # token2- new word
    
    token1 = "#" + token1
    token2 = "#" + token2
    distance = numpy.zeros((len(token2), len(token1)))
    
    for t1 in range(len(token1)):
        distance[0][t1] = t1

    for t2 in range(len(token2)):
        distance[t2][0] = t2
        
    if token1[1] != token2[1]:
        distance[1,1] = 2
    
    for c in range(1, len(token1)):
        for r in range(1, len(token2)):
            
            if token1[c] != token2[r]:
                distance[r,c] = min(distance[r-1,c], distance[r,c-1])+1
            
            else:
                distance[r,c] = distance[r-1,c-1]
                
    return distance[(len(token2)-1)][(len(token1)-1)]

def treshold(line1,line2):
    # calculate the Levenshtein distance between the lines
    distance = levenshteinDistanceDP(line1, line2)

    # set a threshold for the minimum distance
    # ask the user for the threshold
    threshold = int(input("Enter the minimum distance threshold: "))

    # if the distance is below the threshold, the lines are similar
    if distance <= threshold:
        print("The lines are similar and should be attributed to the same author.")
    else:
        print("The lines are different and should be attributed to different authors.")