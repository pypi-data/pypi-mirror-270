from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from pprint import pprint
from tempfile import NamedTemporaryFile
from threading import Thread
from typing import Any
from typing import IO

import click


def dict2conf(outfile: str, dictionary: dict[str, Any]) -> None:
    with open(outfile, "w", encoding="utf8") as fp:
        dict2conffp(fp, dictionary)


def dict2conffp(fp: IO, dictionary: dict[str, Any]) -> None:
    for k, v in dictionary.items():
        print(k, " = ", file=fp, end="")
        pprint(v, stream=fp)


@dataclass
class Runner:
    name: str
    cmd: list[str]
    directory: str = "."
    env: dict[str, str] | None = None
    showcmd: bool = False
    shell: bool = False

    def getenv(self) -> dict[str, str] | None:
        if not self.env:
            return None
        return {**os.environ, **self.env}

    def start(self) -> subprocess.Popen[bytes]:
        if self.showcmd:
            click.secho(" ".join(str(s) for s in self.cmd), fg="blue")
        ret = subprocess.Popen(
            self.cmd,
            cwd=self.directory,
            env=self.getenv(),
            shell=self.shell,
        )
        return ret


def browser(url: str = "http://127.0.0.1:8000", sleep: float = 2.0) -> Thread:
    import time
    import webbrowser

    def run() -> None:
        time.sleep(sleep)
        webbrowser.open_new_tab(url)

    tr = Thread(target=run)
    tr.start()
    return tr


def has_package(package: str) -> bool:
    import importlib

    try:
        importlib.import_module(package)
        return True
    except ModuleNotFoundError:
        return False


def default_conf() -> dict[str, Any]:
    # from tempfile import gettempdir

    conf = {
        "MOUNTPOINTS": [
            ("~", "HOME"),
        ],
        "JOBSDIR": "./turnover_jobs",
        "CACHEDIR": "./turnover_cache",
        "WEBSITE_STATE": "single_user",
    }
    return conf


def instance_conf(config: str) -> dict[str, Any]:
    """We *must* have flask in our environment by now"""
    from flask import Config  # pylint: disable=import-error

    conf = Config(".")
    conf.from_pyfile(config)
    return conf


def webrunner(
    browse: bool,
    workers: int,
    web_config: str | None,
    gunicorn: bool = False,
    *,
    view_only: bool = True,
    configfile: str | None = None,  # turnover config file
    defaults: dict[str, Any] | None = None,
    port: int = 8000,
    extra: tuple[str, ...] = (),
) -> None:
    """Run full website."""

    import sys

    if not has_package("protein_turnover_website"):
        click.secho(
            "Please install protein_turnover_website [pip install protein-turnover-website]!",
            fg="red",
            err=True,
        )
        raise click.Abort()
    if gunicorn and not has_package("gunicorn"):
        click.secho(
            "Please install gunicorn [pip install gunicorn]!",
            fg="red",
            err=True,
        )
        raise click.Abort()

    fp = None
    web_conf = default_conf()
    if web_config:
        # just need JOBSDIR
        web_conf.update(instance_conf(web_config))

    if defaults is not None:
        web_conf.update(defaults)

    # need to read config file just for jobsdir
    jobsdir = Path(web_conf["JOBSDIR"]).expanduser()
    if not jobsdir.exists():
        jobsdir.mkdir(parents=True, exist_ok=True)

    cfg = [f"--config={configfile}"] if configfile is not None else []
    if not view_only:
        background = Runner(
            "background",
            [
                sys.executable,
                "-m",
                "protein_turnover",
                *cfg,
                "--level=info",
                "background",
                f"--workers={workers}",
                "--no-email",
                str(jobsdir),
            ],
            directory=".",
        )
    flask_app = "protein_turnover_website.wsgi"

    with NamedTemporaryFile("w+t") as fp:
        dict2conffp(fp, web_conf)
        fp.flush()

        if not gunicorn:
            website = Runner(
                "flask",
                [
                    sys.executable,
                    "-m",
                    "flask",
                    "--app",
                    flask_app,
                    "run",
                    f"--port={port}",
                    *extra,
                ],
                env={
                    "TURNOVER_SETTINGS": fp.name,
                },
            )
        else:
            website = Runner(
                "gunicorn",
                [
                    sys.executable,
                    "-m",
                    "gunicorn",
                    f"--bind=127.0.0.1:{port}",
                    *extra,
                    flask_app,
                ],
                env={"TURNOVER_SETTINGS": fp.name},
            )
        if view_only:
            procs = [website]
        else:
            procs = [background, website]
        try:
            threads = [(p.name, p.start()) for p in procs]
            bthread = None
            if browse:
                bthread = browser(sleep=5.0)
            for name, tr in threads:
                returncode = tr.wait()
                click.secho(
                    f"{name} done",
                    fg="green" if returncode == 0 else "red",
                )

            if bthread is not None:
                bthread.join()
        except KeyboardInterrupt:
            for name, tr in threads:
                try:
                    click.secho(f"terminating...{name}", fg="blue")
                    tr.terminate()
                except OSError:
                    tr.wait()
        finally:
            pass
            # os.system("stty sane")
