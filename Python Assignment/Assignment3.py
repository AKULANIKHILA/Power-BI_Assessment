#########################ASSIGNMNET###############################
university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#Print all student names and their majors

for student_id, student_info in university_data.items():
    print(f"Student ID: {student_id}, Name: {student_info['name']}, Major: {student_info['major']}")
print()

#Average score per course per student

Course_total = {}
Course_count = {}
for student_info in university_data.values():
    for course, scores in student_info["courses"].items():
        if course not in Course_total:
            Course_total[course] = 0
            Course_count[course] = 0
        Course_total[course] += sum(scores.values())
        Course_count[course] += len(scores)
print("Average score per course:")
for course, total_score in Course_total.items():
    average_score = total_score / Course_count[course]
    print(f"{course}: {average_score}")
print()

#Find students who scored >90 in final of Python101 

for student_id, student_info in university_data.items():
    if "Python101" in student_info["courses"]:
        final_score = student_info["courses"]["Python101"]["final"]
        if final_score > 90:
            print(f"Student ID: {student_id}, Name: {student_info['name']}, Final Score in Python101: {final_score}")

#Add new course AI101 for student S101 

university_data["S101"]["courses"]["AI101"] = {"midterm": 95, "final": 98, "project": 97}
print("Updated course data for S101:")
print(university_data["S101"]["courses"]["AI101"])
print() 

#Print average for each course

for course, scores in Course_total.items():
    average_score = scores / Course_count[course]
    print(f"Average score for {course}: {average_score}")
print()

#3.dictionary comprehension
#mapping student names to marks(>=50)
marks = {"Alice": 82, "Bob" : 43, "Charlie": 55}
passed = {name: score for name,score in marks.items() if score >=50}
print(passed)
#without comprehension
passed = {}
for name,score in marks.items():
    if score >=50:
        passed[name] = score

print(passed)