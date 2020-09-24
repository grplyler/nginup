import click
from .lib import *
from .log import log
from . import config


@click.group()
def cli():
    pass

# Create a Proxypass site
@click.command(help="Create an nginx reverse proxy site")
@click.option('-i', '--internal', help="url to internal http service (Example: localhost:3000)")
@click.option('-p', '--path', help="proxy path", default="/")
@click.option('-s', '--ssl', is_flag=True, help="Enable TLS with Lets Encrypt Certificates", default=False)
@click.option('-w', '--ws', is_flag=True, help="Support Websockets", default=False)
@click.option('-d', '--domain', help="Use domain for virtualhost routing")
def proxy(internal, path, ssl, ws, domain):
    log.info(f"Creating reverse proxy site: {domain} -> nginx -> {internal}")

    template = get_template('proxy')

    if ws:
        log.debug("with websockets")
    
    if ssl:
        log.debug("with SSL")

    config = template.render(internal=internal, domain=domain, ws=ws, ssl=ssl, path=path)
    print(config)
    install_config(domain, config)

    reload_nginx()

# Create a static site
@click.command(help="Create an nginx static site")
@click.argument('root', metavar='<root>')
@click.option('-p', '--path', help="proxy path", default="/")
@click.option('-s', '--ssl', is_flag=True, help="Enable TLS with Lets Encrypt Certificates", default=False)
@click.option('-d', '--domain', help="Use domain for virtualhost routing")
def static(root, path, ssl, domain):
    log.info(f"Creating static site: {domain} -> nginx -> {root}")
    template = get_template('static')

    if ssl:
        log.debug("with SSL")

    # Init root
    init_root(root)

    # Generate config
    config = template.render(root=root, path=path, ssl=ssl, domain=domain)

    # Install config
    install_config(domain, config)

    # Reload nginx
    reload_nginx()


cli.add_command(proxy)
cli.add_command(static)