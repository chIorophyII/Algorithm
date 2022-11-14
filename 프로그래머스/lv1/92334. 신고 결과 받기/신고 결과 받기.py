def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = list(set(report))

    warning = {}
    
    for r in report:
        user, bad = r.split(" ")
        if bad not in warning:
            warning[bad] = 1
        else:
            warning[bad] += 1
    
    for i in range(len(report)):
        user, bad = report[i].split(" ")

        if warning[bad] >= k:
            answer[id_list.index(user)] += 1

    return answer