def solution(bridge_length, weight, truck_weights):
    time_count = 0
    out_bridge = list()
    on_bridge = list()
    truck_time_count = list()

    truck_count = len(truck_weights)
    while len(out_bridge)<truck_count :
        out_bridge_count = 0 
        for index in range(len(truck_time_count)):
            truck_time_count[index] += 1
            if truck_time_count[index] == bridge_length:
                out_bridge_count += 1

        for _ in range(out_bridge_count):
            end_truck = on_bridge.pop(0)
            out_bridge.append(end_truck)
            truck_time_count.pop(0)

        if truck_weights and sum(on_bridge)+truck_weights[0]<=weight and len(on_bridge)+1<=bridge_length:
            truck_weight = truck_weights.pop(0)
            on_bridge.append(truck_weight)
            truck_time_count.append(0)

        time_count += 1
    return time_count

print(solution(100, 100, 	[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))