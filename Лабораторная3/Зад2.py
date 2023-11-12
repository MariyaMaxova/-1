def find_common_participants(people1, people2, zapyataya=','):
    participants1 = people1.split(zapyataya)
    participants2 = people2.split(zapyataya)
    set1 = set(participants1)
    set2 = set(participants2)
    common_participants = set1.intersection(set2)
    return sorted(list(common_participants))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group)
print("Общие участники:", participants)