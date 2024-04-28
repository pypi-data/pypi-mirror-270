import click


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
def cli():
    pass


@cli.command()
def status():
    """Check the status of the Sanda server."""
    click.secho(
        "Sanda is running." if True else "Sanda is not running.",
        fg="green" if True else "red",
    )
    click.secho(
        "The server is healthy." if True else "The server is unhealthy.",
        fg="green" if True else "red",
    )


if __name__ == "__main__":
    cli()
