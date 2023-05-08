# A1 :
- 


# A2 
-


# A3 - 
import os
    if os.path.exists(filename):
        os.remove(filename)
        
Le scheduler est programme pour s'executer chaque jour a minuit.
Changer 
scheduler = BackgroundScheduler(daemon=True)
scheduler.add_job(func=insert_data, trigger="cron", hour=0, minute=0)
scheduler.start()
# A4 - 

# A5

C1 - C2 - C3
D1 - D2

C 1 : infraction = id_poursuite