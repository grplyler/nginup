from os import path, system
from jinja2 import Template
from . import config
from .log import log

print(__file__)

def get_template(name):

    template_path = path.join(path.dirname(__file__), 'templates/', name + ".jinja2")
    with open(template_path) as file_:
        template = Template(file_.read())
        return template

def reload_nginx():
    log.debug("Reloading nginx...")
    system('service nginx reload')
    log.debug("Reload complete.")

def save_config(fname, data):
    outpath = path.join(config.SITES_ENABLED_DIR, fname)
    log.debug(f"saving config to {outpath}")

    with open(outpath, "w") as outfile:
        outfile.write(data)
        