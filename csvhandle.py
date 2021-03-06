#description
#http://study.marearts.com/2018/02/python-csv-file-data-simple-handler.html
    
import csv

class CSV_managerSimple:

    def getFirstRow(self, csv_file_name):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            FirstRow = next(csvPoint)
        return FirstRow

    def getFirstCol(self, csv_file_name):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            FirstCol =[]
            for FirstRow in csvPoint:
                FirstCol = FirstCol+ [FirstRow[0]]
            return FirstCol

    def get_ItoJ_Row(self, csv_file_name,i,j):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            for skip_loop in range(i):
                FirstRow = next(csvPoint)
            ItoJRow = []
            for add_loop in range(j-i):
                ItoJRow = ItoJRow + [next(csvPoint)]

            return ItoJRow

    def get_ItoJ_Col(self, csv_file_name,i,j):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            ItoJCol =[]
            for FirstRow in csvPoint:
                ItoJCol = ItoJCol+ [FirstRow[i:j]]
            return ItoJCol

    def get_ItoJ_Row_and_KtoL_Col(self, csv_file_name,i,j,k,l):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            for skip_loop in range(i):
                next(csvPoint)
            IJ_row_KL_col=[]
            for add_loop in range(j - i):
                oneRow = next(csvPoint)
                IJ_row_KL_col = IJ_row_KL_col + [oneRow[k:l]]
            return IJ_row_KL_col

    def getLengh_of_RowCol(self, csv_file_name):
        firstCol = self.getFirstRow(csv_file_name)
        firstRow = self.getFirstCol(csv_file_name)
        return [len(firstRow), len(firstCol)]

    def writeCSV(self, csv_file_name, data):
        with open(csv_file_name, 'w') as csvfile:
            csvPoint = csv.writer(csvfile)
            for it in range(len(data)):
                csvPoint.writerow(data[it])

    def writeCSV_add(self, csv_file_name, data):
        with open(csv_file_name, 'a') as csvfile:
            csvPoint = csv.writer(csvfile)
            for it in range(len(data)):
                csvPoint.writerow(data[it])


    def divideAllElementByFloat_listsOfList(self, inlist, f):
        outlist = [[float(num/f) for num in sub] for sub in inlist]
        return outlist

    def convertStrToInt_listsOfList(self, inlist):
        outlist = [[int(num) for num in sub] for sub in inlist]
        return outlist

    def convertStrToFloat_listsOfList(self, inlist):
        outlist = [[float(num) for num in sub] for sub in inlist]
        return outlist

    def getWholeData_i(self, csv_file_name):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            output =[]
            for line in csvPoint:
                line = list(map(int, line))
                output = output + [line]
        return output

    def getWholeData_s(self, csv_file_name):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            output =[]
            for line in csvPoint:
                line = list(line)
                output = output + [line]
        return output

    def getWholeData_f(self, csv_file_name):
        with open(csv_file_name, 'r') as csvfile:
            csvPoint = csv.reader(csvfile)
            output =[]
            for line in csvPoint:
                line = list(map(float, line))
                output = output + [line]
        return output




'''
##usage example!

##Test
msgManger = CSV_managerSimple()

#get First Row
FirstRow = msgManger.getFirstRow('./data/csvTest.csv')
print(FirstRow)

#get First col
FirstCol = msgManger.getFirstCol('./data/csvTest.csv')
print(FirstCol)

#get i~j col
SomeCol = msgManger.get_ItoJ_Col('./data/csvTest.csv', 0,2)
print(SomeCol)

#get i~j row
SomeRow = msgManger.get_ItoJ_Row('./data/csvTest.csv', 1,3)
print(SomeRow)

#get i~j Row, k~l col
SomeRowCol = msgManger.get_ItoJ_Row_and_KtoL_Col('./data/csvTest.csv', 1,3,1,3)
print(SomeRowCol)

#count of line in row, col
RowColLength = msgManger.getLengh_of_RowCol('./data/csvTest.csv')
print(RowColLength)

#write csv
msgManger.writeCSV("./data/write_test.csv", SomeRowCol)

'''


