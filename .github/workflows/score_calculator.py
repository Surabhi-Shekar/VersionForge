def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"

#  Input: Enter scores (comma-separated)
input_scores = input("Enter marks (comma-separated): ")

try:
    marks = [float(score.strip()) for score in input_scores.split(",")]
    avg = calculate_average(marks)
    grade = get_grade(avg)

    print(f"\n Average Score: {avg:.2f}")
    print(f"🎓 Grade: {grade}")

except ValueError:
    print(" Please enter only numbers, separated by commas.")
