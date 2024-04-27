"""Console script for rstms_mailgun."""

import json
import sys
import shlex
from subprocess import check_call

import click
import click.core
import requests
from requests.auth import HTTPBasicAuth

from .exception_handler import ExceptionHandler
from .shell import _shell_completion
from .version import __timestamp__, __version__

header = f"{__name__.split('.')[0]} v{__version__} {__timestamp__}"


def _ehandler(ctx, option, debug):
    ctx.obj = dict(ehandler=ExceptionHandler(debug))
    ctx.obj["debug"] = debug


class Context:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.mailgun.net"
        self.auth = HTTPBasicAuth("api", api_key)

    def _request(self, func, path, **kwargs):
        url = f"{self.base_url}/{path}"
        kwargs["auth"] = self.auth
        response = func(url, **kwargs)
        response.raise_for_status()
        return response.json()

    def get(self, path, **kwargs):
        return self._request(requests.get, path, **kwargs)

    def put(self, path, **kwargs):
        return self._request(requests.put, path, **kwargs)

    def delete(self, path, **kwargs):
        return self._request(requests.delete, path, **kwargs)

    def post(self, path, **kwargs):
        return self._request(requests.post, path, **kwargs)


@click.group("mailgun", context_settings={"auto_envvar_prefix": "MAILGUN"})
@click.version_option(message=header)
@click.option("-k", "--api-key", envvar="MAILGUN_API_KEY", show_envvar=True, help="mailgun API key")
@click.option("-d", "--debug", is_eager=True, is_flag=True, callback=_ehandler, help="debug mode")
@click.option("-v", "--verbose", is_flag=True, help="enable verbose output")
@click.option(
    "--shell-completion",
    is_flag=False,
    flag_value="[auto]",
    callback=_shell_completion,
    help="configure shell completion",
)
@click.pass_context
def cli(ctx, api_key, verbose, debug, shell_completion):
    """rstms_mailgun top-level help"""
    ctx.obj = Context(api_key)
    ctx.obj.verbose = verbose


@cli.command
@click.pass_obj
def domains(ctx):
    """domain list"""

    result = ctx.get("v4/domains")
    if ctx.verbose:
        click.echo(json.dumps(result, indent=2))
    else:
        for item in result["items"]:
            click.echo(item["name"])


@cli.command
@click.argument("domain-name")
@click.pass_obj
def domain(ctx, domain_name):
    """details for named domain"""

    result = ctx.get(f"v4/domains/{domain_name}")
    click.echo(json.dumps(result, indent=2))


@cli.command
@click.argument("domain-name")
@click.pass_obj
def delete(ctx, domain_name):
    """delete a domain"""

    click.confirm(f"Confirm DELETE mailgun domain {domain_name}?", abort=True)
    result = ctx.delete(f"v3/domains/{domain_name}")
    click.echo(json.dumps(result, indent=2))


@cli.command
@click.argument("domain-name")
@click.option("-w", "--wildcard", is_flag=True, help="accept email from subdomains when sending")
@click.option("-d", "--dkim-key-size", type=click.Choice(["1024", "2048"]), default=None, help="set DKIM key size")
@click.option("-P", "--smtp-password", help="SMTP authentication password")
@click.option("-A", "--force-dkim-authority", is_flag=True, help="DKIM authority will be the created domain")
@click.option("-R", "--force-root-dkim-host", is_flag=True, help="DKIM authority will be the root domain")
@click.option("-h", "--dkim-host-name", help="DKIM host name")
@click.option("-s", "--dkim-selector", help="set DKIM selector for created domain")
@click.option("-p", "--pool-id", help="request IP Pool")
@click.option("-i", "--assign-ip", help="comma separated list of IP addresses assigned to new domain")
@click.option("-W", "--web-scheme", type=click.Choice(["http", "https"]), default=None, help="domain web scheme")
@click.pass_obj
def create(  # noqa: C901
    ctx,
    domain_name,
    wildcard,
    dkim_key_size,
    smtp_password,
    force_dkim_authority,
    force_root_dkim_host,
    dkim_host_name,
    dkim_selector,
    pool_id,
    assign_ip,
    web_scheme,
):
    """create domain"""

    params = dict(name=domain_name)
    if wildcard:
        params["wildcard"] = True
    if dkim_key_size:
        params["dkim_key_size"] = dkim_key_size
    if smtp_password:
        params["smtp_password"] = smtp_password
    if force_dkim_authority:
        params["force_dkim_authority"] = True
    if force_root_dkim_host:
        params["force_root_dkim_host"] = True
    if dkim_host_name:
        params["dkim_host_name"] = dkim_host_name
    if dkim_selector:
        params["dkim_selector"] = dkim_selector
    if pool_id:
        params["pool_id"] = pool_id
    if assign_ip:
        params["ips"] = assign_ip
    if web_scheme:
        params["web_scheme"] = web_scheme
    click.echo("Creating domain {domain_name}:")
    click.echo(json.dumps(params, indent=2))
    click.confirm("Confirm?", abort=True)
    result = ctx.post("v4/domains", params=params)
    click.echo(json.dumps(result, indent=2))


@cli.command
@click.argument("domain-name")
@click.option("-P", "--smtp-password", help="SMTP authentication password")
@click.option("-w", "--wildcard", is_flag=True, help="accept email from subdomains when sending")
@click.option("-W", "--web-scheme", type=click.Choice(["http", "https"]), default=None, help="domain web scheme")
@click.option("-f", "--mail-from", help="MAILFROM hostname for outbound email")
@click.option(
    "-s", "--spam-action", type=click.Choice(["disabled", "tag", "block"]), default=None, help="domain web scheme"
)
@click.pass_obj
def update(ctx, domain_name, smtp_password, wildcard, web_scheme, spam_action, mail_from):
    """update domain configuration"""

    if mail_from:
        result = ctx.put(f"v3/domains/{domain_name}/mailfrom_host", params=dict(mailfrom_host=mail_from))
        click.echo(json.dumps(result, indent=2))

    params = dict(name=domain_name)
    if wildcard:
        params["wildcard"] = True
    if smtp_password:
        params["smtp_password"] = smtp_password
    if web_scheme:
        params["web_scheme"] = web_scheme
    if spam_action:
        params["spam_action"] = spam_action

    if len(params.keys()) > 1:
        result = ctx.put(f"v4/domains/{domain_name}", params=params)
        click.echo(json.dumps(result, indent=2))


@cli.command
@click.argument("domain-name")
@click.pass_obj
def verify(ctx, domain_name):
    """request domain verification"""

    result = ctx.put(f"v4/domains/{domain_name}/verify")
    click.echo(json.dumps(result, indent=2))


def get_dns_records(result):
    ret = {}
    for record in result["sending_dns_records"]:
        _type = record["record_type"]
        value = record["value"]
        name = record["name"]
        if _type == "TXT" and "spf" in value:
            ret["SPF"] = record
        elif _type == "TXT" and "domainkey" in name:
            ret["DKIM"] = record
        elif _type == "CNAME":
            ret["CNAME"] = record
    return ret


@cli.command
@click.argument("domain-name")
@click.pass_obj
def status(ctx, domain_name):
    """output verification state"""

    result = ctx.get(f"v4/domains/{domain_name}")
    dns_records = get_dns_records(result)
    output = {
        domain_name: dict(
            state=result["domain"]["state"],
            spf=dns_records["SPF"]["valid"],
            dkim=dns_records["DKIM"]["valid"],
        )
    }
    click.echo(json.dumps(output, indent=2))

@cli.command
@click.argument("domain-name")
@click.option('-e', '--exec', "dns_exec", help='execute dns update command')
@click.option('--dry-run', is_flag=True, help='output dns-exec command line to stdout')
@click.pass_obj
def dns(ctx, domain_name, dns_exec, dry_run):
    """required DNS records"""
    result = ctx.get(f"v4/domains/{domain_name}")
    dns_records = get_dns_records(result)
    # domain type name content
    dlen = len(domain_name) + 1
    for record in dns_records.values():
        if record['record_type'] != 'TXT':
            continue
        name = record['name'][:-dlen]
        if not name:
            name = '@'
        value = record['value']
        if dns_exec:
            cmd = shlex.split(dns_exec) + [domain_name, record['record_type'], name, value]
            if dry_run:
                click.echo(shlex.join(cmd))
            else:
                check_call(cmd)
        else:
            click.echo(f"{domain_name} {record['record_type']} {name} '{value}'")


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
