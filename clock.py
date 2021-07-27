from datetime import datetime
from msj import mesaj
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()
# Schedule job_function to be called every two hours
sched.add_job(mesaj, 'interval', hours=0.5)
sched.start()