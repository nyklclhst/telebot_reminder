import mysql.connector
import requests
import schedule
import time
from datetime import datetime


mydb = mysql.connector.connect(
    host="localhost",
    user="xxx",
<<<<<<< HEAD
    passwd="xxx",
=======
    passwd="xxxx",
>>>>>>> 32f27829c0d0af6fa1d05144d1c46d90785555c0
    database="xxxxxxx"
)

sts = 0
mycursor = mydb.cursor()
myc = mydb.cursor()
mycursor.execute("Select * from xxxxx")
myresult = mycursor.fetchall()
<<<<<<< HEAD
bot_token = 'xxxxxxxxxxxxx'
=======
bot_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
>>>>>>> 32f27829c0d0af6fa1d05144d1c46d90785555c0


def telegram_bot_sendtext():
    for x in myresult:
        msg1 = "Hallo "+str(x[2])+". Jadwal jaga anda hari ini ada di shift:\n"
        # print(send_text)
        # requests.get(send_text)
        myc.execute("select * from jadwal where chat_id="+str(x[1]))
        res = myc.fetchall()
        for y in res:
            if y[1] == datetime.today().strftime('%A') and y[4] == sts:
                if int(y[2]) != 0:
                    msg = str(y[2])+"\n"
                    send_text1 = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(x[1]) + '&parse_mode=Markdown&text='+msg
                    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + str(x[1]) + '&parse_mode=Markdown&text='+msg1        
                    print(send_text)
                    print(send_text1)
                    requests.get(send_text)
                    time.sleep(1)
                    requests.get(send_text1)


def check_sts():
    global sts
    if sts % 2 == 0:
        print('minggu 1')
        print(sts)
    else:
        print('minggu 2')
        print(sts)
    if sts == 1:
        sts = 0
    else:
        sts+=1

schedule.every().day.at("16:40").do(telegram_bot_sendtext)
schedule.every().monday.do(check_sts)

while True:
    schedule.run_pending()
    time.sleep(1)
