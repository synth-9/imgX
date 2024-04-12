"""Console script for imgx."""
import sys
import click
from .process_module import ProcessModule


@click.command()
@click.argument('task',type=str)
@click.argument('path',type=str)
def main(task:str,path:str):
    print(f"Task: {task}, in {path}")
    imgx_process = ProcessModule(path=path)
    if task  ==  'read':
        print('reading')
        imgx_process.read_metadata_and_write_to_file()
    if task == 'flat':
        print('flatting')
        imgx_process.flatten_directory()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
