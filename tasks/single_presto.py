"""
Here's how to execute tasks in this file.

$ export TD_API_KEY="..." (get the key from http://console.treasuredata.com/users/current)
$ rm -fr tmp/;
$ python tasks/single_presto.py Task1 --local-scheduler
"""

import luigi
import luigi_td

class Task1(luigi_td.Query):
    type = 'presto'
    database = 'sample_datasets'
    
    def query(self):
        return "SELECT count(1) cnt FROM www_access"

if __name__ == '__main__':
    luigi.run()
