#
# Take a weighted graph representing a social network where the weight
# between two nodes is the "love" between them.  In this "feel the
# love of a path" problem, we want to find the best path from node `i`
# and node `j` where the score for a path is the maximum love of an
# edge on this path. If there is no path from `i` to `j` return
# `None`.  The returned path doesn't need to be simple, ie it can
# contain cycles or repeated vertices.
#
# Devise and implement an algorithm for this problem.
#
from collections import deque

def feel_the_love(G, i, j):
    score_so_far = deque([i])
    score = {i:0}
    paths = {i:[i]}    

    while len(score_so_far) != 0:
        w = score_so_far.popleft()
        for x in G[w]:            
            new_score = max(score[w], G[w][x])
            if x not in score or new_score > score[x]:
                score[x] = new_score
                paths[x] = paths[w] + [x]
                score_so_far.append(x)
            
    if j not in paths: return None
    return paths[j]
                    


   

#########
#
# Test

def score_of_path(G, path):
    max_love = -float('inf')
    for n1, n2 in zip(path[:-1], path[1:]):
        love = G[n1][n2]
        if love > max_love:
            max_love = love
    print 'max love', max_love
    return max_love

def test():
    G = {'a':{'c':1},
         'b':{'c':1},
         'c':{'a':1, 'b':1, 'e':1, 'd':1},
         'e':{'c':1, 'd':2},
         'd':{'e':2, 'c':1},
         'f':{}}
    path = feel_the_love(G, 'a', 'b')
    assert score_of_path(G, path) == 2

    path = feel_the_love(G, 'a', 'f')
    assert path == None

print test()
    
