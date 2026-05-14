def solution(players, callings):
    
    player = dict()
    
    for i in range(len(players)):
        player[players[i]] = i
        
    for calling in callings:
        current = player[calling]
        previous = players[current - 1]
        
        players[current], players[current - 1] = players[current - 1], players[current]
        
        player[calling] -= 1
        player[previous] += 1
    
    
    return players