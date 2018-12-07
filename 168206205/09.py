# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 17:03:47 2018

@author: asus
"""

start = 'hit'
end = 'cog'

adict = ['hot','dot','dog','lot','log','dit']

def find_path(start,end,paths):
    if start == end:
        return "start=end"
    else:
        m = 0
        visited = []
        visited.append(start)
        for word in visited:
            #print(word)   
            for i in range(len(word)):            
                for j in range(ord('a'),ord('z')+1,1):
                    word = word[:i] + chr(j) + word[i+1:]
                    word1=word
                    #print(word)
                    word = visited[0]
                    if word1 in paths:
                        
                        #print(word1)
                        visited.append(word1)
                        m += 1
                        break
    print(visited)                    


find_path(start,end,adict)

