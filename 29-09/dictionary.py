#Dictionaries
students{
    101 :{"Name":"Riddhi", "Scores":[78,90]},
    102 :{"Name":"Siddhi", "Scores":[88,70]},

}

for sid, details in students.items():
    avg =sum (details["Scores"])/len(details["Scores"])
    passed = avg > = 50

    #5 string functions and list functions make a grp of 5 students