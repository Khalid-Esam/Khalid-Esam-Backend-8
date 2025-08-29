students={
    "Khalid":46,
    "Ali":73,
    "Mohamed":89,
    "Ahmed":66,
    "jamal":92
}

for key,value in students.items():
    if value >= 90 :
        grade="A"
    elif value >= 80:
        grade="B"
    elif value >= 70:
        grade="c"
    elif value >= 60:
        grade="D"
    else:
        grade="F"
    print(f"the student {key} have got: {grade}")