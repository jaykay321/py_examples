from csv import reader

def find_user(name,age,csv_path):
    with open(csv_path) as file:
        csv_content = reader(file)
        content = list(csv_content)
        for row in content:
            if row[0] == name and row[1] == age:
                return l.index(row)
        return "Not found"
    
