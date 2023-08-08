# import required libraries
import csv;
import psycopg2;
import pandas as pd;
import json;
from   colorama import Fore;
from   colorama import Style;
import datetime;

# create variables to hold the path to the input files
beginTime = datetime.datetime.now();
inputFileGDP = 'input/gdp-per-capita-penn-world-table.csv';
inputFileBRT = 'input/crude-birth-rate.csv';
inputFilePOP = 'input/population-and-demography.csv';

print("");
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED + " ALL - DATA PREPARATION======================");
print("");

print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED + " PRE - DATABASE CONNECTION===================");
# Connect to the database
conn = psycopg2.connect(database="worldfacts",
						user='postgres', password='top2gun6',
						host='127.0.0.1', port='5432');
conn.autocommit = True;
cursor          = conn.cursor();
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED  + " PRE - DATABASE CONNECTION================" + Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL+ Fore.RED + "=");
print("")

print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED + " ALL - DATABASE LOAD BLOCK===================");
print("")

# open he GDP file for reading and insert into the table
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + " GDP - DATABASE LOAD-------------------------");
with open(inputFileGDP, 'r') as file:
    truncateCommand = "TRUNCATE TABLE GDP";
    cursor.execute(truncateCommand);
    csvreader = csv.reader(file);
    readRecordCount   = 0;
    insertRecordCount = 0;
    for row in csvreader:
        if (readRecordCount > 0):
            row[0] = row[0].replace("'","_");
            row[0] = row[0].replace(" ","_");
            if (row[1] != ""):
                insertCommand = "INSERT INTO GDP (Country_Name, Country_Code, Year, GPD) \
                                 VALUES('" + row[0] + "','" + row[1] + "'," + row[2] + "," + row[3] + ")";
                cursor.execute(insertCommand);
                insertRecordCount += 1;
        readRecordCount += 1; 
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + ' GDP - READ - Total number of records: ', readRecordCount);
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + ' GDP - INSR - Total number of records: ', insertRecordCount);
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + " GDP - DATABASE LOAD----------------------" + Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL + Fore.BLUE + "-");
    print("");
# open he BIRTH RATE file for reading and insert into the table
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + " BRT - DATABASE LOAD-------------------------");
with open(inputFileBRT, 'r') as file:
    truncateCommand = "TRUNCATE TABLE BIRTH_RATE";
    cursor.execute(truncateCommand);
    csvreader = csv.reader(file)
    readRecordCount   = 0;
    insertRecordCount = 0;
    for row in csvreader:
        #print(recordCount,row[0],row[1],row[2],row[3]);
        if (readRecordCount > 0):
            row[0] = row[0].replace("'","_");
            row[0] = row[0].replace(" ","_");
            if (row[1] != ""):
                insertCommand = "INSERT INTO BIRTH_RATE (Country_Name, Country_Code, Year, Birth_Rate) \
                                 VALUES('" + row[0] + "','" + row[1] + "'," + row[2] + "," + row[3] + ")"
                cursor.execute(insertCommand);
                insertRecordCount += 1;
        readRecordCount += 1;
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + ' BRT - READ - Total number of records: ', readRecordCount);
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + ' BRT - INSR - Total number of records: ', insertRecordCount);
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + ' BRT - DATABASE LOAD----------------------' + Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL + Fore.CYAN + "-");
    print("");
    
# open he POPULATION file for reading and insert into the table
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + " POP - DATABASE LOAD-------------------------");
with open(inputFilePOP, 'r') as file:
    truncateCommand = "TRUNCATE TABLE POPULATION";
    cursor.execute(truncateCommand);
    csvreader = csv.reader(file)
    readRecordCount   = 0;
    insertRecordCount = 0;
    for row in csvreader:
        #print(recordCount,row[0],row[1],row[2],row[3]);
        if (readRecordCount > 0):
            row[0] = row[0].replace("'","_");
            row[0] = row[0].replace(" ","_");
            if (row[1] != ""):
                insertCommand = "INSERT INTO POPULATION (Country_Name, \
                                                         Year, \
                                                         pop, pop_l01, \
                                                         pop_l05, \
                                                         pop_l15, \
                                                         pop_l25, \
                                                         pop_f15_t64, \
                                                         pop_g15, \
                                                         pop_g18,\
                                                         pop_e01,\
                                                         pop_f01_t04, \
                                                         pop_f05_t09,\
                                                         pop_f10_t14, \
                                                         pop_f15_t19, \
                                                         pop_f20_t29, \
                                                         pop_f30_t39, \
                                                         pop_f40_t49, \
                                                         pop_f50_t59, \
                                                         pop_f60_t69, \
                                                         pop_f70_t79, \
                                                         pop_f80_t89, \
                                                         pop_f90_t99, \
                                                         pop_g100 ) \
                                VALUES('" + row[0] + "'," +  \
                                            row[1] + "," + \
                                            row[2] + "," + \
                                            row[3] + "," + \
                                            row[4] + "," + \
                                            row[5] + "," + \
                                            row[6] + "," + \
                                            row[7] + "," + \
                                            row[8] + "," + \
                                            row[9] + "," + \
                                            row[10] + "," + \
                                            row[11] + "," + \
                                            row[12] + "," + \
                                            row[13] + "," + \
                                            row[14] + "," + \
                                            row[15] + "," + \
                                            row[16] + "," + \
                                            row[17] + "," + \
                                            row[18] + "," + \
                                            row[19] + "," + \
                                            row[20] + "," + \
                                            row[21] + "," + \
                                            row[22] + "," + \
                                            row[23] + ")";
                cursor.execute(insertCommand);
                insertRecordCount += 1;
        readRecordCount += 1;
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + ' POP - READ - Total number of records: ', readRecordCount);
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + ' POP - INSR - Total number of records: ', insertRecordCount);
    print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + " POP - DATABASE LOAD----------------------" + Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL + Fore.MAGENTA + "-");
    print("");
    
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED  + " ALL - DATABASE LOAD BLOCK================" + Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL + Fore.MAGENTA + "=");
print("");

print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED  + " ALL - JSON LOAD BLOCK=======================");
print("")
# reading the data from the GDP table and preparing the json file
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + " GDP - JSON LOAD-----------------------------");
sql_select_Query = "select * from gdp";
cursor = conn.cursor();
cursor.execute(sql_select_Query);
# get all records
records = cursor.fetchall();
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE +" GDP - READ - JSON preparation       : ", cursor.rowcount);
cursor.execute(sql_select_Query);
table_rows = cursor.fetchall();
df = pd.DataFrame(table_rows);
df.columns = ['Country', 'Country_Code','Year', 'GDP'];
result = df.to_json(orient="records");
parsed = json.loads(result);
json_object = json.dumps(parsed, indent=4);
with open("Resource/gdp.json", "w") as outfile:
    outfile.write(json_object);
with open("Resource/gdp.json", encoding='utf8') as JSONFile:
    data = json.load(JSONFile);
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + " GDP - CHK  - JSON preparation       : ", len(data));
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.BLUE + " GDP - JSON LOAD--------------------------" + Fore.GREEN + Style.BRIGHT + "OK-" + Fore.RESET + Style.RESET_ALL);
print("");

# reading the data from the Birth_Rate table and preparing the json file
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + " BRT - JSON LOAD-----------------------------");
sql_select_Query = "select * from birth_rate";
cursor = conn.cursor();
cursor.execute(sql_select_Query);
# get all records
records = cursor.fetchall();
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + " BRT - READ - JSON preparation       : ", cursor.rowcount);
cursor.execute(sql_select_Query);
table_rows = cursor.fetchall();
df = pd.DataFrame(table_rows);
df.columns = ['Country', 'Country_Code','Year', 'Birth_Rate'];
result = df.to_json(orient="records");
parsed = json.loads(result);
json_object = json.dumps(parsed, indent=4);
with open("Resource/birth_rate.json", "w") as outfile:
    outfile.write(json_object);
with open("Resource/birth_rate.json", encoding='utf8') as JSONFile:
    data = json.load(JSONFile);
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + " BRT - CHK  - JSON preparation       : ", len(data));
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.CYAN + " BRT - JSON LOAD--------------------------"+ Fore.GREEN + Style.BRIGHT + "OK-" + Fore.RESET + Style.RESET_ALL);
print("");

# reading the data from the population table and preparing the json file
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + " POP - JSON LOAD-----------------------------");

sql_select_Query = "select * from population";
cursor = conn.cursor();
cursor.execute(sql_select_Query);
# get all records
records = cursor.fetchall();
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + " POP - READ - JSON preparation       : ", cursor.rowcount);
cursor.execute(sql_select_Query);
table_rows = cursor.fetchall();
df = pd.DataFrame(table_rows);
df.columns = ['Country'    , 'Year'       , 'pop'        , 'pop_l01'    , 'pop_l05'    , 'pop_l15'    , 'pop_l25'    , 'pop_f15_t64', 
              'pop_g15'    , 'pop_g18'    , 'pop_e01'    , 'pop_f01_t04', 'pop_f05_t09', 'pop_f10_t14', 'pop_f15_t19', 'pop_f20_t29', 
              'pop_f30_t39', 'pop_f40_t49', 'pop_f50_t59', 'pop_f60_t69', 'pop_f70_t79', 'pop_f80_t89', 'pop_f90_t99', 'pop_g100' ];
result = df.to_json(orient="records");
parsed = json.loads(result);
json_object = json.dumps(parsed, indent=4);
with open("Resource/population.json", "w") as outfile:
    outfile.write(json_object);
with open("Resource/population.json", encoding='utf8') as JSONFile:
    data = json.load(JSONFile);
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + " POP - CHK  - JSON preparation       : ", len(data));
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.MAGENTA + " POP - JSON LOAD--------------------------" + Fore.GREEN + Style.BRIGHT + "OK-" + Fore.RESET + Style.RESET_ALL);
print("");
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED  + " ALL - JSON LOAD BLOCK===================="+ Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL + Fore.RED + "=");
print("");
print(Fore.WHITE + str(datetime.datetime.now()) + Fore.RED  + " ALL - DATA IS READY======================"+ Fore.GREEN + Style.BRIGHT + "OK" + Fore.RESET + Style.RESET_ALL + Fore.RED + "=");
endTime = datetime.datetime.now();
print("");
print(Fore.WHITE + "EXECUTION STATS>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
print("");
print(Fore.WHITE + str(beginTime)           + ' BEGIN TIME');
print(Fore.WHITE + str(endTime)             + ' END TIME');
print("")
print(Fore.WHITE + f"{(endTime - beginTime).total_seconds()} ELAPSED TIME IN SECONDS");
print(Fore.WHITE + ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>");
