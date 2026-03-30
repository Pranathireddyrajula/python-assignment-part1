
#--------TASK-1---------#
# raw data given with messy names and marks as string
raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

# looping through each student to clean data
for student in raw_students:

# converting marks string into list of integers
    name = student["name"].strip().title()

# converting roll number from string to integer
    roll = int(student["roll"])

# converting marks string into list of integers
    marks = list(map(int,student["marks_str"].split(", ")))

# checking if name contains only alphabets
    is_valid = all(word.isalpha() for word in name.split())
    validity = "✓ Valid name" if is_valid else "✗ Invalid name"

# printing student details in clean format
    print("================================")
    print(f"Student : {name} {validity}" )
    print(f"Roll No : {roll}")
    print(f"Marks : {marks}")
    print("================================")

# special check for roll number 103 
    if roll == 103:
        print(name.upper())
        print(name.lower())


 #--------TASK-2---------#  

# storing student details
student_name  = "Ayesha Sharma"
subjects = ["Math", "Physics", "CS", "English", "Chemistry"]
marks = [88,72,95,60,78]

# printing subject with marks and grade
print("\n--- Subject Wise Performace---")
for i in range(len(subjects)):
    subject = subjects[i]
    mark = marks[i]

# deciding grade based on marks
    if mark >= 90:
        grade = "A+"
    elif mark >= 80:
        grade = "A"
    elif mark >= 70:
        grade = "B"
    elif mark >= 60:
        grade = "C"
    else :
        grade = "F"
    print (f"{subject}: {mark} -> {grade}")

# calculating total and average marks
total_marks = sum(marks)
average_marks = round(total_marks / len(marks),2)

print("\n--- Summary ---")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")

# finding highest and lowest scoring subjects
max_mark = max(marks)
min_mark= min(marks)

max_index = marks.index(max_mark)
min_index = marks.index(min_mark)

print(f"Highest Scoring Subjects: {subjects[max_index]} ({max_mark})")
print(f"Lowest Scoring Subjects: {subjects[min_index]} ({min_mark})")
print("\n--- Add New Subjects ---")
new_count = 0 

# taking user input to add new subjects
while True:
    subject_input = input("Enter subject name (or 'done' to stop):")
    if subject_input.lower()=="done":
        break
    mark_input = input("Enter marks (0-100):")

# validating marks input
    if not mark_input.isdigit():
        print("Invalid input ! Marks must be a number.")
        continue 
    mark_input = int(mark_input)
    if  mark_input < 0 or mark_input > 100:
        print("Marks should be between 0 and 100.")
        continue

# adding new subject and marks to list
    subjects.append(subject_input)
    marks.append(mark_input)
    new_count+=1

# printing updated average after adding subjects
    print("\n--- Updated Summary ---")
    updated_avg = round(sum(marks)/len(marks),2)
    print(f"Updated Average Marks: {updated_avg}")

 #--------TASK-3---------#  

# class data with student names and marks
class_data = [
     
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

# printing table header
print("\n--- Class Performance Report ---")
print("Name              | Average | Status")
print("----------------------------------------")

# counters for pass and fail students
pass_count=0
fail_count=0
total_class_avg=0

# looping through each student
topper_name=""
topper_avg=0
for name ,marks in class_data:
# calculating average marks
    avg=round(sum(marks)/len(marks),2)
# checking pass or fail
    if avg>=60:
        status = "pass"
        pass_count+=1
    else:
        status="fail"
        fail_count+=1

# tracking topper
    if avg>topper_avg:
        topper_avg = avg
        topper_name=name
    total_class_avg+=avg

# printing each row in table format
    print(f"{name:<18} | {avg:6} | {status}")


# final summary of class performance
print("\n--- Summary ---")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")


print(f"Topper: {topper_name} ({topper_avg})")

class_average = round(total_class_avg / len(class_data), 2)
print(f"Class Average: {class_average}") 

#--------TASK-4---------#  

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "

# Step 1: removing unwanted spaces
clean_essay = essay.strip()
print("\n1.clean essay:")
print(clean_essay)

# Step 2: converting to title Case
title_case = clean_essay.title()
print("\n2. Title Case:")
print(title_case)

# Step 3: Counting how many times 'python' appears
python_count = clean_essay.count("python")
print("\n3. 'python' count:")
print(python_count)

# Step 4: Replace 'python' with given text
replaced_text = clean_essay.replace("python", "Python 🐍")
print("\n4. Replaced Text:")
print(replaced_text)

# Step 5: Split essay into sentences
sentences = clean_essay.split(".")
print("\n5.Sentence List:")
print(sentences)

# Step 6: Print numbered sentences
print("\n6. Numbered Sentences:")
for i, sentence in enumerate(sentences, start=1):
    if not sentence.endswith("."):
        sentence +="."
    print(f"{i}. {sentence}")