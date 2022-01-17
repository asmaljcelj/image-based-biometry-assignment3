import csv
import shutil
import os

if __name__ == "__main__":
    file = open('annotations/recognition/ids.csv')
    csvreader = csv.reader(file)
    origpath = os.path.dirname(os.path.abspath(__file__))
    for row in csvreader:
        filepath = row[0]
        clazz = row[1]
        originalpath = origpath + "/" + filepath
        newpath = origpath + "/" + filepath.split('/')[0] + "_razdeljeni" + "/" + clazz
        if not os.path.isdir(newpath):
            os.mkdir(newpath)
        shutil.copyfile(originalpath, newpath + "/" + filepath.split('/')[1])

