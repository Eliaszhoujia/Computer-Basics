S = input("What is the score of the student (out of 100)")
A = input("How many classes attended the student?")
C = input("How many classes were in the course?")
def attendance_percentage():
  return  int(A)/int(C)*100
AP = attendance_percentage()


if int(S) >= 70 and float(AP) > 80:
    print("Student passed with ",str (S), "in their exam and a percentage of", str(AP), "attended classes")
else:
    print("Student failed with ",str (S), "in their exam and a percentage of", str(AP), "attended classes")