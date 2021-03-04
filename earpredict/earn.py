import schedule
import time
import web
import browsers


def job():
    time.sleep(45)
    print("im working ")
    predict,amount=web.webs()
    browsers.read(amount,predict)
    
    
    

schedule.every().minutes.at(":00").do(job)


while True:
   schedule.run_pending()
   
   
    