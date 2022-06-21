student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades={}

for x,y in student_scores.items():
	if y>=91 and y<=100:
		student_grades[x]="Outstanding"
	elif y>=81 and y<=90:
		student_grades[x]="Exceeds Expectations"
	elif y>=71 and y<=80:
		student_grades[x]="Acceptable"
	elif y<=70:
		student_grades[x]="Fail"
	

print(student_grades)





