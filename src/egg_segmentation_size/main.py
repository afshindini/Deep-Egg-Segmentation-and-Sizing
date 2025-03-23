"""Run the main code for egg-segmentation-size"""

import logging

import click

from egg_segmentation_size import __version__
from egg_segmentation_size.logging import config_logger


logger = logging.getLogger(__name__)


@click.command()
@click.version_option(version=__version__)
@click.option("-v", "--verbose", count=True, help="Shorthand for info/debug/warning/error loglevel (-v/-vv/-vvv/-vvvv)")
def egg_segmentation_size_cli(verbose: int) -> None:
    """This repo segments the eggs in images and gives an estimation for their sizes """
    if verbose == 1:
        log_level = 10
    elif verbose == 2:
        log_level = 20
    elif verbose == 3:
        log_level = 30
    else:
        log_level = 40
    config_logger(log_level)

    click.echo("Run the main code.")
