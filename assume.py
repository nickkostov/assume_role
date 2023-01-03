#!/usr/bin/env python3
import click
from src.automatic import table_org
import os

ASSUME_CONFIG_PATH = os.path.join(os.environ["HOME"], ".assume_config")


@click.command()
@click.option("--init", default=False, is_flag=True, help="Initialization of configuration directory")
@click.option("--gen-acc-list", default=False, is_flag=True, help="Generates list of AWS Organization Accounts if only you have admin permissions to your ORG account!")
def cli(init, gen_acc_list):
    """Run with init if you want to initialize"""
    if gen_acc_list:    
        table_org.table_list_as_json(os.path.join(ASSUME_CONFIG_PATH, "accounts.json"))
    if init: 
        from src.configuration import init
        click.echo("Initializing")
    from src.internals import core
cli()