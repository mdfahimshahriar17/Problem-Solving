name_and_score = []

while True:
    student = []
    name = input("Enter name : ").strip()

    if name.lower() == "stop":
        break

    score = int(input("Enter score : "))

    student.append(name)
    student.append(score)

    name_and_score.append(student)

if name_and_score:
    print("NO. Name Score")
    for idx in range(0, len(name_and_score)):
        print(f"{idx+1}. {name_and_score[idx][0]} {name_and_score[idx][1]}")





name_and_score = []

while True:
    student = {}
    name = input("Enter name : ").strip()

    if name.lower() == "stop":
        break

    score = int(input("Enter score : "))

    student[name] = score
    

    name_and_score.append(student)

print(name_and_score)
if name_and_score:
    count = 1
    print("NO. Name Score")
    for student in name_and_score:
        for name, score in student.items():
            print(f"{count} {name} {score}")
            count +=1
