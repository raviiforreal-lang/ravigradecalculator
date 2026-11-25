def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"


def is_pass(marks):
    return all(m >= 40 for m in marks)


if __name__ == "__main__":
    n = int(input("Enter number of subjects: "))
    marks = [float(input(f"Enter marks of subject {i + 1}: ")) for i in range(n)]
    avg = average(marks)
    print("Average:", round(avg, 2))
    print("Grade:", grade(avg))
    print("Result:", "PASS" if is_pass(marks) else "FAIL")