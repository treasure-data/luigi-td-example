import datetime

import luigi
luigi.interface.setup_interface_logging()

from apscheduler.schedulers.blocking import BlockingScheduler
sched = BlockingScheduler()

import apps.examples.hourly_hive
import apps.examples.daily_hive

@sched.scheduled_job('cron', minute=20)
def hourly_scheduled_job():
    dt = datetime.datetime.now().replace(minute=0, second=0, microsecond=0)
    w = luigi.worker.Worker(worker_processes=1)
    w.add(apps.examples.hourly_hive.Task1(scheduled_time=dt))

@sched.scheduled_job('cron', hour=0, minute=50)
def daily_scheduled_job():
    dt = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    w = luigi.worker.Worker(worker_processes=1)
    w.add(apps.examples.daily_hive.Task1(scheduled_time=dt))

sched.start()
