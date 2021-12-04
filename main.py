import psycopg2
from datetime import datetime, timedelta, date, time
dbname = 'testdb'
user= 'postgres'
password= 'postgres'
host='localhost'
port= 5432
con = psycopg2.connect(database=dbname,user=user,password=password,host=host,port=port)
cur = con.cursor()
day = datetime.now().strftime('%d-%m-%Y')
xday = (datetime.strptime(day, '%d-%m-%Y') + timedelta(days=-1)).strftime(format='%d%m%Y')
# f = open('/home/deepak/PycharmProjects/postgreedbconnection/tefile.csv')
# cur.copy_from(f, 'testtwo', columns=('us', 'yu', 'tyy'), sep=",")
with open('/home/deepak/PycharmProjects/postgreedbconnection/Neon_dx_Data_{}.csv'.format(xday)) as f:
    cur.copy_expert('COPY testthree(us, yu, tyy) FROM STDIN WITH HEADER CSV', f)
con.commit()
con.close()