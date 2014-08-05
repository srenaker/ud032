lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Add your function below!
def average(numbers):
    print "Got here"
    total = sum(numbers)
    total = float(total)
    avg = total / len(numbers)
    print "avg is %d" % avg
    return avg
    
def get_average(student):
	homework = average(student['homework'])
	quizzes = average(student['quizzes'])
	tests = average(student['tests'])    
	wavg = homework * .1 + quizzes * .3 + tests * .6    
	return wavg
    
def get_letter_grade(score):
	print "got here 1"
	if score >= 90:
		return "A"
	elif score >= 80:
		return "B"
	elif score >= 70:
		return "C"
	elif score >= 60:
		return "D"
	else:
		return "F"
aveg = get_average(lloyd)
print aveg
#print get_letter_grade(aveg)