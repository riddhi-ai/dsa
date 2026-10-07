students = {
    101: {"Name": "Riddhi", "Scores": [78, 90]},
    102: {"Name": "Siddhi", "Scores": [88, 70]}
}

for s_id, details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    passed = avg >= 50

    print("ID:", s_id)
    print("Name:", details["Name"])
    print("Average:", avg)
    print("Passed:", passed)