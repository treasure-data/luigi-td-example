# Luigi + Treasure Data Workflow Example

Building the complex data pipeline on [Treasure Data](http://www.treasuredata.com/)? Don't write adhoc scripts. This repository contains the example data workflow examples using [Luigi](http://luigi.readthedocs.org/en/latest/), a Python-based robust workflow engine.

![Sample Workflow](http://i.gyazo.com/ccdea082b7f011b961d10a0b043618d5.png)

## List of Example Tasks

[./apps/examples/](https://github.com/treasure-data/luigi-td-example/tree/master/apps/examples) directory contain a couple of basic workflow tasks, you can use as building blocks. All examples use [Luigi-TD](https://github.com/treasure-data/luigi-td), a library to make it easier to use TD from Luigi.

Filename  | Description
------------- | -------------
[single_hive.py](https://github.com/treasure-data/luigi-td-example/blob/master/apps/examples/single_hive.py)|Execute a Hive query, and waits for the completion.
[single_presto.py](https://github.com/treasure-data/luigi-td-example/blob/master/apps/examples/single_presto.py)|Execute a Presto query, and waits for the completion.
[query_and_download_as_csv.py](https://github.com/treasure-data/luigi-td-example/blob/master/apps/examples/query_and_download_as_csv.py)|Execute a Presto query, download the query result, and convert and store it as CSV file on local dir.
[result_output.py](https://github.com/treasure-data/luigi-td-example/blob/master/apps/examples/result_output.py)|Execute Hive query, write the results into the table in TD. Then execute Presto query to use the generated Table. Finally, download 2nd query result and store it as CSV on local dir.
[hourly_hive.py](https://github.com/treasure-data/luigi-td-example/blob/master/apps/examples/hourly_hive.py)|This represents the hourly execusion of a Hive query. This script is supposed to be called by [cron.py](https://github.com/treasure-data/luigi-td-example/blob/master/cron.py).
[daily_hive.py](https://github.com/treasure-data/luigi-td-example/blob/master/apps/examples/daily_hive.py)|This represents the daily execusion of a Hive query. This script is supposed to be called by [cron.py](https://github.com/treasure-data/luigi-td-example/blob/master/cron.py).

## How to Develop My Tasks?

You can of course add your own workflow.


    # Create your app directory
    $ mkdir -p ./apps/yours
    
    # Copy from examples
    $ cp ./apps/examples/single_hive.py ./apps/yours
    
    # Modify (Yes, emacs)
    $ emacs -nw ./apps/yours/single_hive.py
    
    # Test
    $ python ./tasks/single_hive.py YourTaskX --local-scheduler
    
    # Commit
    $ git add ./apps/yours
    $ git commit -a -m 'add new task'

[Luigi Documentation](http://luigi.readthedocs.org/en/latest/) is the great place to start learning the basics of Luigi. After that, [Luigi-TD Documentation](http://luigi-td.readthedocs.org/en/latest/gettingstarted.html) will give you the specifics about how to use TD + Luigi.

## How to Deploy?

Ready to deploy your first workflow? Here's a couple of ways to get started.

#### Deploy on Heroku

This repository is ready to deploy on [Heroku](http://www.heroku.com/) PaaS. Please just hit the button below, and will create Heroku app running [cron.py](https://github.com/treasure-data/luigi-td-example/blob/master/cron.py) who kicks workflows in hourly / daily basis.

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

#### Deploy on Your Machine

To run this repository, you need to install `python` on your machine.

    # Install required libraries
    $ pip install -r ./requirements.txt
    
    # Set your TD API Key (http://console.treasuredata.com/users/current)
    $ export TD_API_KEY="..."
    
    # Run specific Task
    $ python ./tasks/sinble_hive.py TaskXXX --local-scheduler
    
    # Remove intermediate results, and execute from scratch
    $ rm -fr ./tmp/
    $ python ./tasks/sinble_hive.py TaskXXX --local-scheduler
    
    # Run periodic Task
    $ python ./cron.py --local-scheduler

# Resources

- [Luigi Documentation](http://luigi.readthedocs.org/en/latest/)
- [Luigi-TD Documentation](http://luigi-td.readthedocs.org/en/latest/gettingstarted.html)

# Support

Need a hand with something? Send us an email to support@treasure-data.com and we'll get back to you right away! For technical questions, use the treasure-data tag on Stack Overflow.
