import urllib
import random
import json
import MySQLdb 
db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="root",  # your password
                     db="news")

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM info_news")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row              
   
source={1:"bbc-news",2:"techcrunch",3:"bbc-sport",4:"the-hindu",5:"cnn",6:"espn"}
s=source[random.randint(1,6)]
url="https://newsapi.org/v1/articles?source="+s+"&apiKey=74da5482c5fa4de690959100081eb0db"
file=open("article1.txt","w")
testfile = urllib.URLopener()
testfile.retrieve(url,"article1.txt")
file.close()
fo=open("article1.txt","r")
list_data=json.loads(fo.read())
fo.close()
z=1
for i in list_data["articles"]:
	
	t=i["title"] 
	d=i["description"]
	u=i["url"]
	a=i["author"]
	try:
     		cur.execute("""INSERT INTO info_news VALUES (%s,%s,%s,%s,%s)""",(z,t,d,u,a))
     		db.commit()
		z=z+1
 	except:     
     		db.rollback()

