"""
Here's how to execute tasks in this file.

$ export TD_API_KEY="..." (get the key from http://console.treasuredata.com/users/current)
$ rm -fr tmp/;
$ python apps/examples/query_and_download_as_csv.py Task2 --local-scheduler
"""

import luigi
import luigi_td

# Issue Presto query
class Task1(luigi_td.Query):
    type = 'presto'
    database = 'sample_datasets'
    
    def query(self):
        return "SELECT path, COUNT(1) cnt FROM www_access GROUP BY path ORDER BY cnt"

    def output(self):
        # This line is required to save executed Job ID locally. By doing this,
        # the result of the query is cached locally, and you don't have to exec
        # another TD query when you invoke the Task2.
        #
        # This check-pointing mechanism is useful for your debubbing, and also
        # performance in produciton since you don't have to re-execute all the
        # jobs when the perticular job got failed.
        return luigi_td.ResultTarget('tmp/CSVDownloadTask1')

# Download the result, and format as CSV
class Task2(luigi.Task):
    def requires(self):
        return Task1()

    def output(self):
        return luigi.LocalTarget('tmp/CSVDownloadTask2.csv')

    def run(self):
        target = self.input()
        with self.output().open('w') as f:
            target.result.to_csv(f)

if __name__ == '__main__':
    luigi.run()
