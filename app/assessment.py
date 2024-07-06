def compute_scores(answers):
    question_mapping = {
        1: 'I', 2: 'R', 3: 'S', 4: 'A', 5: 'S',
        6: 'E', 7: 'I', 8: 'A', 9: 'E', 10: 'R',
        11: 'C', 12: 'A', 13: 'E', 14: 'R', 15: 'I',
        16: 'S', 17: 'C', 18: 'A', 19: 'E', 20: 'R',
        21: 'I', 22: 'C', 23: 'S', 24: 'A', 25: 'E',
        26: 'R', 27: 'I', 28: 'S', 29: 'C', 30: 'A'
    }
    
    scores = {'R': 0, 'I': 0, 'A': 0, 'S': 0, 'E': 0, 'C': 0}

    for i in range(1, 31):
        answer = answers.get(f'q{i}')
        if answer == 'yes':
            scores[question_mapping[i]] += 2
        elif answer == 'maybe':
            scores[question_mapping[i]] += 1

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    top_3 = sorted_scores[:3]
    
    return top_3
