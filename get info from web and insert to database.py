import requests #libray to need this project
from bs4 import BeautifulSoup
import mysql.connector
import re
conut = -1 
#connect and get data from website
x = requests.get('https://www.truecar.com/used-cars-for-sale/listings/audi/')
#from ths line to line 25 for sort data to get just price and function
soup = BeautifulSoup(x.text , "html.parser")
result = soup.find_all('div' , {'data-test' : "vehicleListingPriceAmount"}, {'class':"heading-3 my-1 font-bold"})
result_2 = soup.find_all('div', {'class' : "truncate text-xs"} , {'data-test': "vehicleMileage"})

finall_result = re.sub('<.*?>' , '' , str(result))
finall_result = re.sub('\s' , '\n' , finall_result)
finall_result = re.sub('[[]' , '' , finall_result)
finall_result = re.sub('[]]' , '' , finall_result)
finall_result = finall_result.split()

finall_result_2 = re.findall('svg>.*?<' , str(result_2))
finall_result_2 = re.sub('svg>' , '' , str(finall_result_2) )
finall_result_2 = re.sub('<' , '' , finall_result_2)
finall_result_2 = re.sub('\s' , '\n' , finall_result_2)
finall_result_2 = re.sub('[[]' , '' , finall_result_2)
finall_result_2 = re.sub('[]]' , '' , finall_result_2)
finall_result_2 = finall_result_2.split()


#connect to your database for insert data into
print('connecting to database...')
cnx = mysql.connector.connect(user = 'user' , password = 'password' 
                              , host = 'server host' , database = 'name database')
print('connected to database')
#a code to allow change codes from database
cursor = cnx.cursor()
# a code of mysql to insert data to database
add_info = """INSERT INTO information_table(
                  price , function )
                  VALUES (%s , %s)"""
#the important code to create correct form to sql can insert to your database
for word in finall_result:
    conut+=1
    val = [(word , finall_result_2[conut])]
    cursor.executemany(add_info, val)
#to commit codes in database
cnx.commit()

#close server of your database
cnx.close()

