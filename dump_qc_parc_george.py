import csv
import mysql.connector

mydb = mysql.connector.connect(user='root', password='',
                            host='localhost',
                            database='weather')
source = 'qc_parc_george.csv'
cursor = mydb.cursor()
try:
    with open(source) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        base_sql = "INSERT INTO qc_parc_george (timestamp, Label, value) VALUES "
        items = []
        counter = 0
        for row in csv_reader:
            if counter < 10000:
                items.append("('" + row[0] + "','" + row[1] + "',"+ row[2] + ")")
                counter = counter + 1
            else:
                delimiter = ","
                insert_sql = base_sql + delimiter.join(items)
                items = []
                print(insert_sql)
                cursor.execute(insert_sql)
                mydb.commit()
                counter = 0

        if counter>0:
            delimiter = ","
            insert_sql = base_sql + delimiter.join(items)
            items = []
            print(insert_sql)
            cursor.execute(insert_sql)
            mydb.commit()
            counter = 0

except TypeError as e:
    print(e)
    mydb.rollback()
finally:
    mydb.close()