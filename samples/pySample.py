# Sample 1 - Reading a CSV file and inserting data into a table
# before running this script, create a table in the database using CreateTable.sql
# before running this script, install psycopg2 using pip install psycopg2
# before running this script, install pandas using pip install pandas
import csv
import psycopg2
import pandas as pd
import json

#
# create a variable to hold the path to the input file
#
inputFile = '../resource/gdp-per-capita-penn-world-table.csv';

#
# how to read a csv file using python, and process each row
#
# open he file for reading
with open(inputFile, 'r') as file:
  csvreader = csv.reader(file)
  recordCount = 0;
  for row in csvreader:
    print(recordCount,row[0],row[1],row[2],row[3]);
    recordCount += 1;

print('Total number of records: ', recordCount);
      
# Another way to read a CSV and keep it for further processing 
# import pandas as pd
# data = pd.read_csv(inputFile)
# data

# Use your own dabaase name, user and password
conn = psycopg2.connect(database="worldfacts",
						user='postgres', password='top2gun6',
						host='127.0.0.1', port='5432'
)

conn.autocommit = True;
cursor          = conn.cursor()
#open the csv file using python standard file I/O
#copy file into the table just created 
with open(inputFile, 'r') as f:
    next(f);                             # Skip the header row.
    cursor.copy_from(f, 'gdp', sep=','); # Copy the CSV data into table.
    conn.commit();                       # Commit the changes.
    
#
# reading the data from the table
# 
sql_select_Query = "select * from gdp"
cursor = conn.cursor()
cursor.execute(sql_select_Query)
# get all records
records = cursor.fetchall()
print("Total number of rows in table: ", cursor.rowcount)
#
# printing each row
#
print("\nPrinting each row")
for row in records:
    print("country", row[0], "country code", row[1], "year", row[2],"gdp", row[3])

cursor.execute(sql_select_Query)
table_rows = cursor.fetchall()
df = pd.DataFrame(table_rows)
df.columns = ['Country', 'Country_Code','Year', 'GDP']
print(df.head)
result = df.to_json(orient="records")
parsed = json.loads(result)
json_object = json.dumps(parsed, indent=4)
with open("../Resource/gdp.json", "w") as outfile:
    outfile.write(json_object)