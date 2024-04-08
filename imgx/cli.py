"""Console script for imgx."""
import sys
import click
from .process_module import ProcessModule


@click.command()
@click.argument('task',type=str)
def main(task:str):
    print(f"Task: {task}")
    imgx_process = ProcessModule()
    imgx_process.read_metadata_and_write_to_file()
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
