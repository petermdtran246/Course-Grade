# Read the name of the input file
input_file = input().strip()

# Read file contents and calculate grades
with open(input_file, 'r') as file:
    lines = file.readlines()

grades = []
midterm1_total = 0
midterm2_total = 0
final_total = 0

for line in lines:
    data = line.strip().split('\t')
    last_name, first_name, midterm1, midterm2, final = data
    midterm1 = int(midterm1)
    midterm2 = int(midterm2)
    final = int(final)
    average = (midterm1 + midterm2 + final) / 3
    grades.append((last_name, first_name, midterm1, midterm2, final, average))
    midterm1_total += midterm1
    midterm2_total += midterm2
    final_total += final

# Calculate exam averages
num_students = len(grades)
midterm1_avg = midterm1_total / num_students
midterm2_avg = midterm2_total / num_students
final_avg = final_total / num_students

# Assign letter grades
def assign_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Write report to file
with open('report.txt', 'w') as report_file:
    for last_name, first_name, midterm1, midterm2, final, average in grades:
        letter_grade = assign_grade(average)
        report_file.write(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}\n")
    report_file.write(f"\nAverages: midterm1 {midterm1_avg:.2f}, midterm2 {midterm2_avg:.2f}, final {final_avg:.2f}\n")