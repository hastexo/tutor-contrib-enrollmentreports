from .__about__ import __version__
from glob import glob
import os
# When Tutor drops support for Python 3.8, we'll need to update this to:
# from importlib import resources as importlib_resources
# See: https://github.com/overhangio/tutor/issues/966#issuecomment-1938681102
import importlib_resources
import click
from tutor import hooks
from tutor import config as tutor_config
from tutor.commands.local import local as local_command_group


config = {
    "unique": {
        "MAIL_TO": [],
    },
    "defaults": {
        "VERSION": __version__,
        "BASE_IMAGE": "docker.io/ubuntu:22.04",
        "DOCKER_IMAGE": "{{ DOCKER_REGISTRY }}enrollmentreports:{{ ENROLLMENTREPORTS_VERSION }}",  # noqa: E501
        "REPOSITORY": "https://github.com/hastexo/ansible-role-enrollmentreports.git",  # noqa: E501
        "REVISION": f"v{__version__}",
        "MAIL_FROM": "{{ SMTP_USERNAME }}",
        "FREQUENCY": "monthly",
        "K8S_CRONJOB_ENABLE": True,
        "K8S_CRONJOB_SCHEDULE": "0 0 1 * *",
        "K8S_CRONJOB_STARTING_DEADLINE_SECONDS": 900,
    },
}


hooks.Filters.IMAGES_BUILD.add_item((
    "enrollmentreports",
    ("plugins", "enrollmentreports", "build", "enrollmentreports"),
    "{{ ENROLLMENTREPORTS_DOCKER_IMAGE }}",
    (),
))

hooks.Filters.IMAGES_PULL.add_item((
    "enrollmentreports",
    "{{ ENROLLMENTREPORTS_DOCKER_IMAGE }}",
))
hooks.Filters.IMAGES_PUSH.add_item((
    "enrollmentreports",
    "{{ ENROLLMENTREPORTS_DOCKER_IMAGE }}",
))


@local_command_group.command(help="Run the enrollment reports script")
@click.pass_obj
def enrollmentreports(context):
    config = tutor_config.load(context.root)
    job_runner = context.job_runner(config)
    job_runner.run_task(
        service="enrollmentreports",
        command="ansible-playbook enrollment-report.yml"
    )


# Add the "templates" folder as a template root
hooks.Filters.ENV_TEMPLATE_ROOTS.add_item(
    str(importlib_resources.files("tutorenrollmentreports") / "templates")
)
# Render the "build" and "apps" folders
hooks.Filters.ENV_TEMPLATE_TARGETS.add_items(
    [
        ("enrollmentreports/build", "plugins"),
        ("enrollmentreports/apps", "plugins"),
    ],
)
# Load patches from files
for path in glob(str(importlib_resources.files(
        "tutorenrollmentreports") / "patches" / "*")):

    with open(path, encoding="utf-8") as patch_file:
        hooks.Filters.ENV_PATCHES.add_item(
            (os.path.basename(path), patch_file.read())
        )
# Add configuration entries
hooks.Filters.CONFIG_DEFAULTS.add_items(
    [
        (f"ENROLLMENTREPORTS_{key}", value)
        for key, value in config.get("defaults", {}).items()
    ]
)
hooks.Filters.CONFIG_UNIQUE.add_items(
    [
        (f"ENROLLMENTREPORTS_{key}", value)
        for key, value in config.get("unique", {}).items()
    ]
)
hooks.Filters.CONFIG_OVERRIDES.add_items(
    list(config.get("overrides", {}).items())
)
