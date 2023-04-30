#levenstein.py 

#ensure you had numba module install
#pip install numba
#if your python ver is 3.11.1, it may not compatible with numba 
#can try use python ver that is 3.9.x or 3.10.x

import numpy
from numba import njit

@njit 
def levenshteinDistanceDP(token1,token2):
    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

    for t1 in range(len(token1) + 1):
        distances[t1][0] = t1

    for t2 in range(len(token2) + 1):
        distances[0][t2] = t2
        
    a = 0
    b = 0
    c = 0
    
    for t1 in range(1, len(token1) + 1):
        for t2 in range(1, len(token2) + 1):
            if (token1[t1-1] == token2[t2-1]):
                distances[t1][t2] = distances[t1 - 1][t2 - 1]
            else:
                a = distances[t1][t2 - 1]
                b = distances[t1 - 1][t2]
                c = distances[t1 - 1][t2 - 1]
                
                if (a <= b and a <= c):
                    distances[t1][t2] = a + 1
                elif (b <= a and b <= c):
                    distances[t1][t2] = b + 1
                else:
                    distances[t1][t2] = c + 1

    return distances[len(token1)][len(token2)]

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
