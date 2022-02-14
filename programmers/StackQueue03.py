def solution(bridge_length, weight, truck_weights):

    onBridgeTruckCount = 0
    onBridgeTruckWeight = 0
    onBridgeTruck = []
    passBridgeTruck = []
    while(True):
        for i in range(bridge_length):
            if weight>=onBridgeTruckWeight+truck_weights[0]:
                onBridgeTruckCount += 1
                onBridgeTruckWeight += truck_weights[0]
                onBridgeTruck.append(truck_weights[0], 1)
                del truck_weights[0]
            else:

    answer = 0
    return answer