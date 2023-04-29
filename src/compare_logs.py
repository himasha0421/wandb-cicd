import os

import wandb
import wandb.apis.reports as wr

# init the wandb client
wandb_client =  wandb.Api()

def get_baseline_run(entity, project, tag='baseline'):
    """this method for get the baseline run from wandb"""

    experiment_run = f'{entity}/{project}'
    tags= [tag]

    baseline_runs= wandb_client.runs( experiment_run, 
                                    {"tags": {"$in": tags}}
                                    ) # this is the Mongo Client
    #check on number of baseline runs
    assert len(baseline_runs) == 1 , 'Baseline Run only should associate with single experiment'
    return baseline_runs[0]


def compare_runs(entity= "himasha" ,
                 project= 'mnist-experiment', 
                 tag='baseline',
                 run_id=None
                 ):
    
    # get the entity / project / tag / run id from enviroment variables
    assert os.environ['WANDB_API_KEY'] , "You must set the wandb client api key !!!!"
    ENTITY = os.getenv('ENTITY') or entity
    PROJECT = os.getenv('PROJECT') or project
    TAG =  os.getenv('TAG') or tag
    RUN_ID = os.getenv('RUN_ID') or run_id

    # get the baseline run
    run_init =  get_baseline_run(entity=ENTITY , 
                                 project=PROJECT,
                                 tag=TAG )
    
    # get the reference run name from id
    reference_path = f'{ENTITY}/{PROJECT}/{RUN_ID}'
    run_reference = wandb_client.run(reference_path)

    #define the report
    report = wr.Report(
        entity=ENTITY,
        project=PROJECT,
        title='Compare Runs',
        description=f"A demo of comparing runs for experiment {PROJECT} \n Baseline run id : {run_init.name} Current run id : {run_reference.name}"
    )  

    # create the report
    pg = wr.PanelGrid(
        runsets=[
            wr.Runset(ENTITY, PROJECT, "Run Comparison").set_filters_with_python_expr(f"Name in [ '{run_init.name}', '{run_reference.name}' ]")
        ],
        panels=[
            wr.RunComparer(diff_only='split', layout={'w': 24, 'h': 15}),
        ]
    )
    
    # save report into wandb
    report.blocks = report.blocks[:1] + [pg] + report.blocks[1:]
    report.save()

    """
    to capture the report url into github action outputs we need to save that into special tmp file 
    captured inside GITHUB_OUTPUT enviroment variable
    """
    # open the file and write the report URL
    with open( os.environ['GITHUB_OUTPUT'] , 'a' ) as f:
        print( f'REPORT_URL={report.url}' , file=f )
    return report.url

if __name__=='__main__':
    # run the compre method
    url =  compare_runs()
    print(f"This is the Run Compre Report URL : {url}")
