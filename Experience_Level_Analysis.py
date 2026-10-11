import sqlite3
import csv


# Function to classify an employee by total working years
def classify_experience(total_working_years):
    if total_working_years < 5:
        return "Junior"
    elif total_working_years < 10:
        return "Mid"
    else:
        return "Senior"


# Connect to the existing SQLite database
connection = sqlite3.connect("HR_Attrition.db")
cursor = connection.cursor()


# Retrieve the years of experience for every employee
cursor.execute("""
    SELECT TotalWorkingYears
    FROM FactEmployee
""")


employee_records = cursor.fetchall()


# Create counters for the three experience levels
experience_counts = {
    "Junior": 0,
    "Mid": 0,
    "Senior": 0
}


# Classify every employee using the Python function
for employee_record in employee_records:
    total_working_years = employee_record[0]

    experience_level = classify_experience(
        total_working_years
    )

    experience_counts[experience_level] += 1


# Create the final summary
experience_summary = [
    ["Junior", experience_counts["Junior"]],
    ["Mid", experience_counts["Mid"]],
    ["Senior", experience_counts["Senior"]]
]


# Display the summary in the terminal
print()
print("Experience Level Summary")
print("--------------------------------------")
print("ExperienceLevel     EmployeeCount")
print("--------------------------------------")

for experience_level, employee_count in experience_summary:
    print(experience_level, employee_count)


# Export the summary to a CSV file
with open(
    "Experience_Level_Summary.csv",
    "w",
    newline="",
    encoding="utf-8"
) as output_file:

    writer = csv.writer(output_file)

    writer.writerow([
        "ExperienceLevel",
        "EmployeeCount"
    ])

    writer.writerows(experience_summary)


# Close the database connection
connection.close()


print()
print("Summary exported successfully.")