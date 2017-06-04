# read the names and marks of at least 4 students
# rank the top 3 students with highest marks
# give cash rewards: 1st $500, 2nd $300, 3rd $100. (non modified value)
# appreciate students who scored 950 or above

# {"John": 875,"Laureen": 924,"Sarah": 983,"Smith": 952}

import operator

def readStudentDetails():
    print("Enter the number of the students: ")
    numberOfStudents = int(input())
    studentRecord = {}
    for student in range(0, numberOfStudents):
        print("Enter the name of the student: ")
        name = input()
        print ("Ener the marks: ")
        marks = int(input())
        studentRecord[name] = marks
    return studentRecord

def rankStudents(studentRecord):
    # print()
    sortedStudentRecord = sorted(studentRecord.items(), key = operator.itemgetter(1), reverse = True)
    print(sortedStudentRecord)
    print("{} has ranked first with {} grade!!".format(sortedStudentRecord[0][0], sortedStudentRecord[0][1]))
    print("{} has ranked second with {} grade!".format(sortedStudentRecord[1][0], sortedStudentRecord[1][1]))
    print("{} has ranked third with {} grade".format(sortedStudentRecord[2][0], sortedStudentRecord[2][1]))
    # print()
    return sortedStudentRecord

def rewardStudents(sortedStudentRecord, reward):
    # print()
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[0][0], reward[0]))
    print("{} has received a cash reward of ${}".format(sortedStudentRecord[1][0], reward[1]))
    print ("{} has received a cash reward of ${}".format(sortedStudentRecord[2][0], reward[2]))
    # print()

def appreciateStudents(sortedStudentRecord):
    for record in sortedStudentRecord:
        if record[1] >= 950:
            print("Congratulations on scoring {} grade, {}".format(record[1], record[0]))
        else:
            break
    # print()

studentRecord = readStudentDetails()
sortedStudentRecord = rankStudents(studentRecord)
reward = (500, 300, 100)
rewardStudents(sortedStudentRecord, reward)
appreciateStudents(sortedStudentRecord)
