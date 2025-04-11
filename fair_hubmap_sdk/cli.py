import click
from .assessor import Assessor

@click.group()
def main():
    """fair-hubmap: Measure FAIR principles for HuBMAP datasets."""
    pass

@main.command()
@click.option("--dataset-id", required=True, help="HuBMAP dataset ID")
def assess(dataset_id: str):
    """Assess FAIRness of a HuBMAP dataset."""
    assessor = Assessor(dataset_id)
    report = assessor.evaluate()
    click.echo("FAIR Assessment Report:")
    click.echo(f"Findable: {report.findable:.2f}")
    click.echo(f"Accessible: {report.accessible:.2f}")
    click.echo(f"Interoperable: {report.interoperable:.2f}")
    click.echo(f"Reusable: {report.reusable:.2f}")
    click.echo("\nDetails:")
    for key, value in report.details.items():
        click.echo(f"{key.capitalize()}: {value}")

if __name__ == "__main__":
    main()
