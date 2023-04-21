import wandb


if __name__=='__main__':
    print(f'The version of wandb is : {wandb.__version__}')
    assert wandb.__version__ == '2.01.1' , f"expected wandb 2.01.1 but got {wandb.__version__}"