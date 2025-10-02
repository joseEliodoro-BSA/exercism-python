# Instructions
# You're a teaching assistant correcting student exams. Keeping track of results manually is getting both tedious and mistake-prone. You decide to make things a little more interesting by putting together some functions to count and calculate results for the class.

# While you can give "partial credit" on exam questions, overall exam scores have to be ints. So before you can do anything else with the class scores, you need to go through the grades and turn any float scores into ints. Lucky for you, Python has the built-in round() function you can use.

# Create the function round_scores(student_scores) that takes a list of student_scores. This function should consume the input list and return a new list with all the scores converted to ints. The order of the scores in the resulting list is not important.

# >>> student_scores = [90.33, 40.5, 55.44, 70.05, 30.55, 25.45, 80.45, 95.3, 38.7, 40.3]
# >>> round_scores(student_scores)
# ...
# [40, 39, 95, 80, 25, 31, 70, 55, 40, 90]

# Stuck? Reveal Hints
# Opens in a modal
# As you were grading the exam, you noticed some students weren't performing as well as you had hoped. But you were distracted, and forgot to note exactly how many students.

# Create the function count_failed_students(student_scores) that takes a list of student_scores. This function should count up the number of students who don't have passing scores and return that count as an integer. A student needs a score greater than 40 to achieve a passing grade on the exam.

# >>> count_failed_students(student_scores=[90,40,55,70,30,25,80,95,38,40])
# 5

# Stuck? Reveal Hints
# Opens in a modal
# The teacher you're assisting wants to find the group of students who've performed "the best" on this exam. What qualifies as "the best" fluctuates, so you need to find the student scores that are greater than or equal to the current threshold.

# Create the function above_threshold(student_scores, threshold) taking student_scores (a list of grades), and threshold (the "top score" threshold) as parameters. This function should return a list of all scores that are >= to threshold.

# >>> above_threshold(student_scores=[90,40,55,70,30,68,70,75,83,96], threshold=75)
# [90,75,83,96]

# Stuck? Reveal Hints
# Opens in a modal
# The teacher you are assisting likes to assign letter grades as well as numeric scores. Since students rarely score 100 on an exam, the "letter grade" lower thresholds are calculated based on the highest score achieved, and increment evenly between the high score and the failing threshold of <= 40.

# Create the function letter_grades(highest) that takes the "highest" score on the exam as an argument, and returns a list of lower score thresholds for each "American style" grade interval: ["D", "C", "B", "A"].

# """Where the highest score is 100, and failing is <= 40.
#        "F" <= 40
#  41 <= "D" <= 55
#  56 <= "C" <= 70
#  71 <= "B" <= 85
#  86 <= "A" <= 100
# """

# >>> letter_grades(highest=100)
# [41, 56, 71, 86]


# """Where the highest score is 88, and failing is <= 40.
#        "F" <= 40
#  41 <= "D" <= 52
#  53 <= "C" <= 64
#  65 <= "B" <= 76
#  77 <= "A" <= 88
# """

# >>> letter_grades(highest=88)
# [41, 53, 65, 77]

# Stuck? Reveal Hints
# Opens in a modal
# You have a list of exam scores in descending order, and another list of student names also sorted in descending order by their exam scores. You would like to match each student name with their exam score and print out an overall class ranking.

# Create the function student_ranking(student_scores, student_names) with parameters student_scores and student_names. Match each student name on the student_names list with their score from the student_scores list. You can assume each argument list will be sorted from highest score(er) to lowest score(er). The function should return a list of strings with the format <rank>. <student name>: <student score>.

# >>> student_scores = [100, 99, 90, 84, 66, 53, 47]
# >>> student_names =  ['Joci', 'Sara','Kora','Jan','John','Bern', 'Fred']
# >>> student_ranking(student_scores, student_names)
# ...
# ['1. Joci: 100', '2. Sara: 99', '3. Kora: 90', '4. Jan: 84', '5. John: 66', '6. Bern: 53', '7. Fred: 47']

# Stuck? Reveal Hints
# Opens in a modal
# Although a "perfect" score of 100 is rare on an exam, it is interesting to know if at least one student has achieved it.

# Create the function perfect_score(student_info) with parameter student_info. student_info is a list of lists containing the name and score of each student: [["Charles", 90], ["Tony", 80]]. The function should return the first [<name>, <score>] pair of the student who scored 100 on the exam.

# If no 100 scores are found in student_info, an empty list [] should be returned.

# >>> perfect_score(student_info=[["Charles", 90], ["Tony", 80], ["Alex", 100]])
# ["Alex", 100]

# >>> perfect_score(student_info=[["Charles", 90], ["Tony", 80]])
# []

"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    new_scores = [round(score, 0) for score in student_scores]
    return new_scores


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """

    qtn_estudantes_reprovados = 0
    for item in student_scores:
        if item <= 40:
            qtn_estudantes_reprovados += 1
    return qtn_estudantes_reprovados


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    best_scores = []
    for item in student_scores:
        if item >= threshold:
            best_scores.append(item)
    return best_scores


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    step = (highest - 40)/4
    n2 = int(41 + step)
    n3 = int(n2 + step)
    n4 = int(n3 + step)

    return [41, n2, n3, n4]


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    new_list = []
    for i, name in enumerate(student_names):
        new_list.append(f"{i+1}. {name}: {student_scores[i]}")
    return new_list
    


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """

    for student in student_info:
        if(student[1] == 100):
            return student
    return []
