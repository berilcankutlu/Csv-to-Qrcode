import csv
import fileinput
import qrcode

def csv_reader(file):
    csv_file = csv.reader(file)
    csv_list = []
    csv_list.extend(csv_file)
    for line in csv_list:
        temp = []
        for data in line:
            temp.append(data)
            image = qrcode.make(temp)
            serino = temp[0]
            image.save(str(serino)+'.png')
    del temp
csv_reader(fileinput.input())