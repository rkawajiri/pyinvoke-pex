# pyinvoke pex file

## What is this?

TBA

## How To

```shell
$ cd path/to/your/project
$ wget https://github.com/rkawajiri/pyinvoke-pex/raw/master/invoke.pex
$ chmod +x invoke.pex
$ edit tasks.py
```

Add a task like below. If you have created `tasks/__init__.py`, add to the file.

```python
from invoke import task

@task
def pex(ctx):
    ctx.run('pex --python-shebang="#!/usr/bin/env python" -r requirements.txt -c invoke -o invoke.pex')
```

If you have not created `requirements.txt`, create the file and write required packages. Then rebuild invoke.pex file.

```shell
$ ./invoke.pex pex
```

That's it. When you call your task, use `./invoke.pex` instead of `invoke` command.

```shell
$ ./invoke.pex your_task
```

When you add packages, add the packages to requirements.txt and rebuild.


# Trouble Shootings

## pex.resolver.Untranslateable: *** is not translateable by ChainedTranslator(WheelTranslator, EggTransator, SourceTranslator)

Try add an option `--no-use-wheel`.

```python
@task
def pex(ctx):
    ctx.run('pex --python-shebang="#!/usr/bin/env python" --no-use-wheel -r requirements.txt -c invoke -o invoke.pex')
```

# LICENSE
TBA
