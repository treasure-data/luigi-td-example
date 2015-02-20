"""
Here's how to execute tasks in this file.

$ export TD_API_KEY="..." (get the key from http://console.treasuredata.com/users/current)
$ python tasks/hourly_hive.py Task1 --local-scheduler
"""

import luigi
import luigi_td
import datetime

class Task1(luigi_td.Query):
    scheduled_time = luigi.DateParameter(default=datetime.datetime.now().replace(minute=0, second=0, microsecond=0))

    type = 'hive'
    database = 'sample_datasets'
    
    def query(self):
        return """\
-- Hourly Job from Luigi-TD ({scheduled_time})
SELECT
  code,
  count(1) AS cnt
FROM
  www_access
WHERE
  TD_TIME_RANGE(time,
  TD_TIME_ADD("{scheduled_time}", "-1y"),
  "{scheduled_time}",
  "UTC")
GROUP BY code
""".format(scheduled_time = self.scheduled_time)

if __name__ == '__main__':
    luigi.run()
