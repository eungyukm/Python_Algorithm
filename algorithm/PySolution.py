def generate_person_one(count) -> list:
    cnt = 0
    person_one = []
    while cnt < count:
        person_one.append(cnt % 5 + 1)
        cnt += 1

    return person_one

def generate_person_two(count) -> list:
    cnt = 0
    person_two = []
    number = 1
    while cnt < count:
        if cnt % 2 == 0:
            person_two.append(2)
        else:
            person_two.append(number % 5 + 1)
            number += 1

        cnt += 1

    return person_two

def generate_person_three(count) -> list:
    cnt = 0
    person_three = []
    person_three_pattern = [3, 1, 2, 4, 5]
    pattern_cnt = 0
    while cnt < count:
        person_three.append(person_three_pattern[pattern_cnt % 5])
        cnt += 1

        if cnt % 2 == 0:
            pattern_cnt += 1

    return person_three

def solution(answers):
    print(answers)
    person_one = generate_person_one(len(answers))
    print(person_one)

    person_two = generate_person_two(len(answers))
    print(person_two)

    person_three = generate_person_three(len(answers))
    print(person_three)

    person_one_score = 0
    person_two_score = 0
    person_three_score = 0
    for i in range(len(answers)):
        if person_one[i] == answers[i]:
            person_one_score += 1

        if person_two[i] == answers[i]:
            person_two_score += 1

        if person_three[i] == answers[i]:
            person_three_score += 1


    person_scores ={
        "1": person_one_score,
        "2": person_two_score,
        "3": person_three_score
    }

    sorted_dict = dict(sorted(person_scores.items(), reverse=True))
    print(sorted_dict)

    answer = []
    max_score = max(person_scores.values())
    for person, score in person_scores.items():
        if score == max_score:
            answer.append(int(person))
    print (answer)

solution([1, 3, 2, 4, 2])