#코드 참고했음
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0]*bridge_length
    while len(bridge):
        answer += 1
        bridge.pop(0)
        if truck_weights:
            sum_bridge = sum(bridge)
            if sum_bridge + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    
    return answer