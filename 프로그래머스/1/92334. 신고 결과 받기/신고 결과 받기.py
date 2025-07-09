def solution(id_list, report, k):
    answer = [0 for _ in id_list]
    
    report_dict = dict([(id, {'report': [], 'reported': 0}) for id in id_list])
    
    for r in report :
        user, reported = r.split()
        if reported in report_dict[user]['report'] :
            continue
        report_dict[user]['report'].append(reported)
        report_dict[reported]['reported'] += 1
        
    reported_id = [id if report_dict[id]['reported'] >= k else "" for id in id_list]
    
    for idx, id in enumerate(id_list) :
        for r in report_dict[id]['report'] :
            if r in reported_id :
                answer[idx] += 1
    
    return answer