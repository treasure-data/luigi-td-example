"""
Here's how to execute tasks in this file.

$ export TD_API_KEY="..." (get the key from http://console.treasuredata.com/users/current)
$ python apps/examples/single_hive.py Task1 --local-scheduler
"""

import luigi
import luigi_td

class Task1(luigi_td.Query):
    type = 'hive'
    database = 'sample_datasets'
    
    def query(self):
        return "SELECT count(1) cnt FROM www_access"

if __name__ == '__main__':
    luigi.run()
