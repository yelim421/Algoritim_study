def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = []
    
    for truck in truck_weights:
        bridge.append(truck)
        time += 1
        if sum(bridge) > weight or len(bridge) > bridge_length :
            time += bridge_length-1
            bridge.pop(0)
        #else : 
            #time += 1
    while len(bridge) > 0 :
        bridge.pop(0)
        time += 1
    if bridge_length >= len(truck_weights):
        time += bridge_length - len(truck_weights)
    return time


# 未完



print(solution(3, 1, [1, 1, 1]))