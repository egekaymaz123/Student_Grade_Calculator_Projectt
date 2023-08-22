def calculate_grade(splitter):
    splitter = splitter[:-1]
    list = splitter.split(':')
    studentName = list[0]
    grades = list[1].split(',')
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])
    average = (grade1+grade2+grade3)/3

    if average >=90 and average <= 100:
        word ="AA"
    elif average>=85 and average<=89:
        word = "BA"
    elif average>=80 and average<=84:
        word ="BB"
    elif average>=75 and average<=79:
        word="CB"
    elif average>=70 and average <=74:
        word="CC"
    elif average>=65 and average <=69:
        word="DC"
    elif average>=60 and average <=64:
        word="DD"
    elif average>=50 and average <=59:
        word="FD"
    else:
        word="FF"
    return studentName + ": "+word+"\n"

def grade_avarage():
    with open("grades.txt","r",encoding="utf-8") as file:
        for satir in file:
            print(calculate_grade(satir))

def write_grade():
    name = input('Student Name: ')
    surname = input('Student Surname: ')
    not1 = input('Grade 1: ') 
    not2 = input('Grade 2: ')
    not3 = input('Grade 3: ')
    with open("grades.txt","a",encoding="utf-8") as file:
        file.write(name+ ' '+ surname+':'+not1+','+not2+','+not3+'\n')


def save_grades():
    with open('grades.txt',"r",encoding="utf-8") as file:
        liste = []
        for i in file:
            liste.append(calculate_grade(i))
        
        with open("grade.txt","w",encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)


while True:
    xx = input('1- Read Grades\n2- Write Grades\n3- Save Grade\n4-Exit\n')
    if xx == "1":
        grade_avarage()
    elif xx =="2":
        write_grade()
    elif xx =="3":
        save_grades()
    else:
        break