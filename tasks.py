from invoke import task

@task
def pex(ctx):
    ctx.run('pex  --python-shebang="#!/usr/bin/env python" -r requirements.txt -c invoke -o invoke.pex')
