# csv_file_handle
csv element access python

usage
<pre>
##make object
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

#write csv
msgManger.writeCSV("./data/write_test.csv", SomeRowCol)
</pre>
