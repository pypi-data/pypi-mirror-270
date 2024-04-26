from dotenv import load_dotenv
import os
import logging
import uac_api
import click
from . import __version__
import json
from jsonpath_ng import jsonpath, parse

# Load environment variables from .env file
load_dotenv()

__output = None
__select = None
output_option = click.option('--output', '-o', type=click.File('w'))
select_option = click.option('--select', '-s', help="select which field to be returned. JSONPATH")

class UacCli:
    def __init__(self, log_level):
        self.log_level = log_level

    def main(self):
        logging.basicConfig(level=self.log_level)
        logging.info(f'UAC CLI is running... ({__version__})')
        self.log = logging
        self.config = self.get_config()
        self.uac = uac_api.UniversalController(base_url=self.config["uac_url"], token=self.config["token"], logger=self.log)
        self.log.info(f'UAC URL: {self.config["uac_url"]}')
        
        return self.uac

    def get_config(self):
        config = {
            "uac_url": os.getenv('UAC_URL'),
            "token": os.getenv('UAC_TOKEN'),
        }
        return config
    
@click.group()
@click.version_option(version=__version__)
@click.option('--log-level', '-l', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), default='INFO')
@click.pass_context
def main(ctx, log_level):
    cli = UacCli(log_level=log_level)
    ctx.obj = cli.main()

# Audits

@main.group()
def audit():
    pass

# - auditType: auditType 
# - source: source 
# - status: status 
# - createdBy: createdBy 
# - tableName: tableName 
# - tableRecordName: tableRecordName 
# - updatedTimeType: updatedTimeType 
# - updatedTime: updatedTime 
# - tableKey: tableKey 
# - includeChildAudits: includeChildAudits 
@audit.command('list', short_help='Get a list of audits')
@click.argument('args', nargs=-1, metavar="auditType=auditType source=source status=status createdBy=createdBy tableName=tableName tableRecordName=tableRecordName updatedTimeType=updatedTimeType updatedTime=updatedTime tableKey=tableKey includeChildAudits=includeChildAudits")
@click.pass_obj
@output_option
@select_option
def list(uac, args, output=None, select=None):
    click.echo(click.style(f"Listing Audits...", fg="green"))
    vars_dict = dict(var.split('=') for var in args)
    response = uac.audits.list_audit(**vars_dict)
    print(f"Found {len(response)} records.")
    if output:
        click.echo(click.style(f"Writing to {output.name}", fg="blue"))
        output.write(json.dumps(response, indent=4))
    
    if select:
        jsonpath_expr = parse(select)
        click.echo(click.style(f"Selecting {select}...", fg="blue"))
        click.echo(click.style(f"Found {jsonpath_expr} records.", fg="blue"))
        result = [match.value for match in jsonpath_expr.find(response)]
        click.echo("\n".join(result))
    else:
        if output is None:
            click.echo(json.dumps(response, indent=4))

def run():
    main()

if __name__ == '__main__':
    main()