# template_gen.py
import os
from pwncli import *
from lianpwn import lg_err, lg_suc, lg_inf
import subprocess


def generate_template():
    if os.path.exists("exp.py"):
        lg_err("File 'exp.py' already exists.")
        subprocess.run(["mv", "exp.py", "exp.py.bak"])
    content = """#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#   expBy : @eastXueLian
#   Debug : ./exp.py debug  ./pwn -t -b b+0xabcd
#   Remote: ./exp.py remote ./pwn ip:port

from lianpwn import *
from pwncli import *

cli_script()
set_remote_libc("libc.so.6")

io: tube = gift.io
elf: ELF = gift.elf
libc: ELF = gift.libc

ia()
"""

    with open("exp.py", "w") as f:
        f.write(content)

    os.chmod("exp.py", 0o755)

    lg_inf("Template 'exp.py' created successfully!")
