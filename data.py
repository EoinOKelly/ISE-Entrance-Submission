import csv

#The below code creates the csv file and writes all of the titles
def init():
    file = open("database.csv", "w")
    writer = csv.writer(file)
    writer.writerow(["Name", "Password", "Points", "Level", "Day", "Filler"])
    file.flush()
    file.close()
