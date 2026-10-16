import csv

def get_test_data():
    test_data = []

    with open("data/test_users.csv", "r") as users_csv:
        reader = csv.DictReader(users_csv)

        for row in reader:
            test_data.append((row["username"],row["password"],row["expected"]))

    return test_data


def get_successful_users():
    test_data = []
    with open("data/test_users.csv","r") as users_csv:
        reader = csv.DictReader(users_csv)
        for row in reader:
            if row["expected"] == "success":
                test_data.append((row["username"],row["password"],row["expected"]))

    return test_data