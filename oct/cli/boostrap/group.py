import click
from cli.boostrap.host import host


@click.group(
    short_help='Get a machine ready to be an Ansible node or target host.',
    help='''
In order for Ansible to interact with a target host, or for a machine
to be used as a node that issues Ansible directives, specific dependencies
exist. These commands allow for a machine to be boot-strapped into an
Ansible target host or an Ansible node.
'''
)
def bootstrap():
    """
    Do nothing -- this group should never be called without a sub-command.
    """

    pass


bootstrap.add_command(host)