# coding:utf-8

import os
import requests
from urllib.parse import urlparse

from xarg import argp
from xarg import add_command
from xarg import commands
from xarg import run_command
import favicon


def save_icon(icon: favicon.Icon, directory: str = "/tmp"):
    response = requests.get(icon.url, stream=True, timeout=15)
    name: str = os.path.basename(icon.url)
    path = os.path.join(directory, name)
    with open(path, "wb") as image:
        for chunk in response.iter_content(1024):
            image.write(chunk)


@add_command("download", help="download the favicon of a website")
def add_cmd_download(_arg: argp):
    _arg.add_argument("--output", type=str, nargs=1, metavar="DIR",
                      default=["tmp"], help="the directory to save the icon")
    _arg.add_argument(dest="urls", type=str, nargs="+", metavar="URL",
                      help="the url of a website")


@run_command(add_cmd_download)
def run_cmd_download(cmds: commands) -> int:  # pylint: disable=unused-argument
    output: str = cmds.args.output[0]
    for url in cmds.args.urls:
        domain: str = urlparse(url).netloc
        directory: str = os.path.join(output, domain)
        if not os.path.exists(directory):
            os.makedirs(directory)
        for icon in favicon.get(url):
            cmds.logger.info(f"download '{domain}' {icon} to {directory}")
            save_icon(icon, directory)
    return 0
