def compute_scores(answers):
    question_mapping = {
        1: 'You are Investigative', 2: 'You are Realistic', 3: 'You are a Socializer', 4: 'You are Artistic', 5: 'You are a Socializer',
        6: 'You are Enterprising', 7: 'You are Investigative', 8: 'You are Artistic', 9: 'You are Enterprising', 10: 'You are Realistic',
        11: 'You are Conventional', 12: 'You are Artistic', 13: 'You are Enterprising', 14: 'You are Realistic', 15: 'You are Investigative',
        16: 'You are a Socializer', 17: 'You are Conventional', 18: 'You are Artistic', 19: 'You are Enterprising', 20: 'You are Realistic',
        21: 'You are Investigative', 22: 'You are Conventional', 23: 'You are a Socializer', 24: 'You are Artistic', 25: 'You are Enterprising',
        26: 'You are Realistic', 27: 'You are Investigative', 28: 'You are a Socializer', 29: 'You are Conventional', 30: 'You are Artistic'
    }

    scores = {'You are Realistic': 0, 'You are Investigative': 0, 'You are Artistic': 0, 'You are a Socializer': 0, 'You are Enterprising': 0, 'You are Conventional': 0}

    for i in range(1, 31):
        answer = answers.get(f'q{i}')
        if answer == 'yes':
            scores[question_mapping[i]] += 2
        elif answer == 'maybe':
            scores[question_mapping[i]] += 1

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    total_score = sum(scores.values())
    slideshows = {
        'You are Realistic': ['assets/slideshows/doer1.png', 'assets/slideshows/doer2.png', 'assets/slideshows/doer3.png'],
        'You are Investigative': ['assets/slideshows/think1.png', 'assets/slideshows/think2.png', 'assets/slideshows/think3.png'],
        'You are Artistic': ['assets/slideshows/creator1.png', 'assets/slideshows/creator2.png', 'assets/slideshows/creator3.png'],
        'You are a Socializer': ['assets/slideshows/helpers1.png', 'assets/slideshows/helpers2.png', 'assets/slideshows/helpers3.png'],
        'You are Enterprising': ['assets/slideshows/persuaders1.png', 'assets/slideshows/persuaders2.png', 'assets/slideshows/persuaders3.png'],
        'You are Conventional': ['assets/slideshows/organizers1.png', 'assets/slideshows/organizers2.png', 'assets/slideshows/organizers3.png']
    }


    sorted_slideshows = {type_: slideshows[type_] for type_, _ in sorted_scores[:3]}

    return sorted_slideshows
