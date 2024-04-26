import sys

import click

from mlsteam_model_sdk.utils.config import get_config_path
from mlsteam_model_sdk.core.exceptions import MissingConfigException


@click.command(
    help='test whether the model SDK has been initialized (whether an SDK configuration path is discovered)'
)
def cmd():
    try:
        cfg_path = get_config_path(check=True)
        click.echo('[' + click.style('v', fg='green') + '] ', nl=False)
        click.echo('SDK has been initialized.')
        click.echo('Configuration file: ' + str(cfg_path))
    except MissingConfigException:
        click.echo('[' + click.style('x', fg='red') + '] ', nl=False)
        click.echo('Failed to discover SDK configuration file.')
        click.echo('Hint: Run `' + click.style('mlsteam-model-cli init -i', fg='cyan') + '` to initialize SDK.')
        sys.exit(1)
