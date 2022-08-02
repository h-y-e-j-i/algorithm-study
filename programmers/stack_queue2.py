def solution(priorities, location):
    answer = 0
    printer = []
    result_printer = []
    answer = 0
    num = sorted(priorities)
    num.reverse()
    
    for i in range(len(priorities)):
        printer.append((i, priorities[i])) 
        
    for n in num :
        index = 0
        count = len(printer)
        while(True):
            if count == 0 : break
            doc_num, data = printer[index]
            if n==data:
                result_printer.append(printer[index])
                if doc_num == location:
                    answer = len(result_printer)
                del printer[index]
                break
            else :
                del printer[index]
                printer.append((doc_num, data))
            count -= 1
    
    return answer