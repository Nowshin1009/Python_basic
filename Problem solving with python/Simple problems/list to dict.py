# Organize Data Using a Dictionary
def organize_scores(data):
    """
    Converting list of tuples into a dictionary where: 
    - Keys are student names.
    - Values are dictionaries with subjects as keys and scores as values.
    """
    organized_data = {}  # an empty dictionary to store student data
    for name, subject, score in data:
        if name not in organized_data:
            organized_data[name] = {}  # Create an empty dictionary for the student if not exists
        organized_data[name][subject] = score  # Assign the subject and score to the student
    return organized_data

# Calculate Average Scores
def calculate_average_scores(student_scores):
    """
    Calculates the average score for each student.
    Returns a dictionary with student names as keys and average scores as values.
    """
    averages = {}  # Initialize an empty dictionary for storing averages
    for student, subjects in student_scores.items():
        total_score = sum(subjects.values())  # Sum all scores of the student
        num_subjects = len(subjects)  # Count the number of subjects
        averages[student] = round(total_score / num_subjects, 2)  # Compute and round the average score
    return averages

# Identify Top Scorer
def top_scorer(average_scores):
    """
    Finds the student with the highest average score.
    """
    return max(average_scores, key=average_scores.get)  # Get the student with the highest average score

# Find Unique Subjects
def unique_subjects(data):
    """
    Extracts all unique subjects from the dataset using a set.
    """
    return {subject for _, subject, _ in data}  # Use a set comprehension to store unique subjects

# Sample Data
students_data = [
    ("Alice", "Math", 85),
    ("Bob", "Math", 78),
    ("Alice", "Science", 90),
    ("Bob", "Science", 88),
    ("Charlie", "Math", 92),
    ("Charlie", "Science", 85),
    ("Alice", "History", 88),
    ("Bob", "History", 76),
    ("Charlie", "History", 89)
]

# Running the functions
organized_data = organize_scores(students_data)
print("Organized Data:", organized_data)  # Print the structured dictionary format of student data

average_scores = calculate_average_scores(organized_data)
print("Average Scores:", average_scores)  # Print the computed average scores per student

best_student = top_scorer(average_scores)
print("Top Scorer:", best_student)  # Print the name of the highest scoring student

subjects = unique_subjects(students_data)
print("Unique Subjects:", subjects)  # Print all unique subjects in the dataset