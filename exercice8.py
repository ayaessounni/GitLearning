score = input("Please enter your score: ")

try:
    score = float(score)
    if 100 >= score >= 90:
        print("Excellent")
    elif 90 > score >= 80:
        print("good")
    elif 80 > score >= 60:
        print("medium")
    elif 60 > score >= 0:
        print("bad")
    else:
        raise
except Exception:
    print("Enter a correct score.")