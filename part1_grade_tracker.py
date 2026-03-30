
#--------TASK-1---------#

# raw_students = [
#     {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
#     {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
#     {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
#     {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
#     {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
# ]


# for student in raw_students:
#     name = student["name"].strip().title()
#     roll = int(student["roll"])
#     marks = list(map(int,student["marks_str"].split(", ")))

#     is_valid = all(word.isalpha() for word in name.split())
#     validity = "✓ Valid name" if is_valid else "✗ Invalid name"

#     print("================================")
#     print(f"Student : {name} {validity}" )
#     print(f"Roll No : {roll}")
#     print(f"Marks : {marks}")
#     print("================================")
    
#     if roll == 103:
#         print(name.upper())
#         print(name.lower())


#  #--------TASK-2---------#  

# student_name  = "Ayesha Sharma"
# subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
# marks = [88,72,95,60,78]

# print("\n--- Subject Wise Performace---")
# for i in range(len(subjects)):
#     subject = subjects[i]
#     mark = marks[i]

#     if mark >= 90:
#         grade = "A+"
#     elif mark >= 80:
#         grade = "A"
#     elif mark >= 70:
#         grade = "B"
#     elif mark >= 60:
#         grade = "C"
#     else :
#         grade = "F"
#     print (f"{subject}: {mark} -> {grade}")

# total_marks = sum(marks)
# average_marks = round(total_marks / len(marks),2)

# print("\n--- Summary ---")
# print(f"Total Marks: {total_marks}")
# print(f"Average Marks: {average_marks}")

# max_mark = max(marks)
# min_mark= min(marks)

# max_index = marks.index(max_mark)
# min_index = marks.index(min_mark)

# print(f"Highest Scoring Subjects: {subjects[max_index]} ({max_mark})")
# print(f"Lowest Scoring Subjects: {subjects[min_index]} ({min_mark})")
# print("\n--- Add New Subjects ---")
# new_count = 0 

# while True:
#     subject_input = input("Enter subject name (or 'done' to stop):")
#     if subject_input.lower()=="done":
#         break
#     mark_input = input("Enter marks (0-100):")

#     if not mark_input.isdigit():
#         print("Invalid input ! Marks must be a number.")
#         continue 
#     mark_input = int(mark_input)
#     if  mark_input < 0 or mark_input > 100:
#         print("Marks should be between 0 and 100.")
#         continue
#     subjects.append(subject_input)
#     marks.append(mark_input)
#     new_count+=1

#     print("\n--- Updated Summary ---")
#     updated_avg = round(sum(marks)/len(marks),2)
#     print(f"Updated Average Marks: {updated_avg}")

 #--------TASK-3---------#  

class_data = [
     
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

print("\n--- Class Performance Report ---")
print("Name              | Average | Status")
print("----------------------------------------")

pass_count=0
fail_count=0
total_class_avg=0

topper_name=""
topper_avg=0
for name ,marks in class_data:
    avg=round(sum(marks)/len(marks),2)
    if avg>=60:
        status = "pass"
        pass_count+=1
    else:
        status="fail"
        fail_count+=1
    if avg>topper_avg:
        topper_avg = avg
        topper_name=name
    total_class_avg+=avg

    print(f"{name:<18} | {avg:6} | {status}")

print("\n--- Summary ---")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")


print(f"Topper: {topper_name} ({topper_avg})")

class_average = round(total_class_avg / len(class_data), 2)
print(f"Class Average: {class_average}") 

#--------TASK-4---------#  

# essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# clean_essay = essay.strip()
# print("\n1.clean essay:")
# print(clean_essay)

# title_case = clean_essay.title()
# print("\n2. Title Case:")
# print(title_case)

# python_count = clean_essay.count("python")
# print("\n3. 'python' count:")
# print(python_count)

# replaced_text = clean_essay.replace("python", "Python 🐍")
# print("\n4. Replaced Text:")
# print(replaced_text)

# sentences = clean_essay.split(".")
# print("\n5.Sentence List:")
# print(sentences)

# print("\n6. Numbered Sentences:")
# for i, sentence in enumerate(sentences, start=1):
#     if not sentence.endswith("."):
#         sentence +="."
#     print(f"{i}. {sentence}")