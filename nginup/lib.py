from os import path, system, mkdir
from shutil import rmtree
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

def install_config(fname, data):
    outpath = path.join(config.SITES_ENABLED_DIR, fname)
    log.debug(f"saving config to {outpath}")

    with open(outpath, "w") as outfile:
        outfile.write(data)

def install_ssl(domain):
    log.info(f"Install TLS Certification for {domain}")
    system(f"certbot --nginx -d {domain}")

def init_root(root):
    log.debug(f"Creating Document root: {root}")
    ok = mkdir_confirm(root)
    
def mkdir_confirm(root):
    # p = path.join(config.WEB_ROOT, domain)
    if not path.exists(root):
        mkdir(root)
        return True
    else:
        confirm = input(f"{root} already exists. Overwite? (y/n): ")
        if config == "y":
            rmtree(root)
            mkdir(root)
            return True
        else:
            log.warn(f"Aborting.")
            return False