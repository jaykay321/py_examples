from csv import DictReader,DictWriter

def update_user(old_name, new_name, csv_path):
    with open(csv_path,"r") as file:
        data = list(DictReader(file))
        for row in data:
            if row["first_name"] == old_name:
                row["first_name"] == new_name
                count +=1
        with open(csv_path,"w",newline="") as file:
            headers = (first_name)
            csv_writer = DictWriter(file,fieldnames=headers)
            csv_writer.writeheader()
            for row in data:
                csv_writer.writerow({"first_name": row["first_name"]})
    return "Users update: {}".format(count)
