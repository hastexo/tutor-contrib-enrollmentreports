# Enrollment reports plugin for [Tutor](https://docs.tutor.overhang.io)

This is an **experimental** plugin for
[Tutor](https://docs.tutor.overhang.io) that creates monthly
enrollment reports (in the
[`.tsv`](https://en.wikipedia.org/wiki/Tab-separated_values) format),
and emails them to a configurable address.

It is meant to be run once a month, and will produce enrollment
reports covering a period of one month.

Version compatibility matrix
----------------------------
￼
You must install a supported release of this plugin to match the Open
edX and Tutor version you are deploying. If you are installing this
plugin from a branch in this Git repository, you must select the
appropriate one:

| Open edX release | Tutor version     | Plugin branch | Plugin release |
|------------------|-------------------|---------------|----------------|
| Lilac            | `>=12.0, <13`     | Not supported | Not supported  |
| Maple            | `>=13.2, <14`[^1] | `maple`       | 0.1.x          |
| Nutmeg           | `>=14.0, <15`     | `nutmeg`      | 1.x.x          |
| Olive            | `>=15.0, <16`     | `main`        | 2.x.x          |
| Palm             | `>=16.0, <17`     | `main`        | 2.x.x          |

[^1]: For Open edX Maple and Tutor 13, you must run version 13.2.0 or
￼   later. That is because this plugin uses the Tutor v1 plugin API,
￼   [which was introduced with that
￼   release](https://github.com/overhangio/tutor/blob/master/CHANGELOG.md#v1320-2022-04-24).

## Installation

    pip install git+https://github.com/hastexo/tutor-contrib-enrollmentreports@v2.2.0

## Usage

To enable this plugin, run:

    tutor plugins enable enrollmentreports

Before starting Tutor, build the docker image:

    tutor images build enrollmentreports

To create enrollment reports in the Tutor local deployment, run:

    tutor local enrollmentreports

If you want to run this command periodically in a local deployment,
you can invoke this command from a cron job on your host.

For a Kubernetes deployment, this plugin defines a
[CronJob](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/)
which runs the report generation script according to the schedule
defined in the `ENROLLMENTREPORTS_K8S_CRONJOB_SCHEDULE` configuration
parameter.


## Configuration

The following values can all modified with the `tutor config save --set
PARAM_NAME=VALUE` commands, or your can edit your Tutor `config.yml`
file directly.

### Tutor configuration parameters

You must

* *either* set `RUN_SMTP: true` (so that Tutor configures an SMTP server
  for you),
* *or* configure your SMTP client credentials with
  * `SMTP_HOST`,
  * `SMTP_PORT`,
  * `SMTP_USERNAME`,
  * `SMTP_PASSWORD`, and
  * `SMTP_USE_TLS` or `SMTP_USE_SSL`.

### Plugin configuration parameters

* `ENROLLMENTREPORTS_MAIL_TO`: a list of addresses to send the
  enrollment reports to. Default `[]`.
* `ENROLLMENTREPORTS_MAIL_FROM`: the sender address to use on the
  enrollment reports. Defaults to the value of `SMTP_USERNAME`; you
  must override this if you want to use a different sender address.
* `ENROLLMENTREPORTS_DOCKER_IMAGE`: the Docker image used to spin up
  the job pod (set this to an image reference in your local registry,
  unless your Tutor configuration already sets `DOCKER_REGISTRY` to
  point to that)
* `ENROLLMENTREPORTS_FREQUENCY`: the frequency with which enrollment
  reports are generated (default `monthly`)
* `ENROLLMENTREPORTS_K8S_CRONJOB_SCHEDULE` (default `"0 0 1 * *"`,
  that is once a month at midnight, on the first day of the month)
* `ENROLLMENTREPORTS_K8S_CRONJOB_ENABLE` (default `true`). Set this to
  `false` to disable (suspend) the generation of enrollment reports.
* `ENROLLMENTREPORTS_K8S_CRONJOB_STARTING_DEADLINE_SECONDS` (default:
  `900`). See [the Kubernetes
  documentation](https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/#starting-deadline)
  for details on job start deadlines.


## License

This software is licensed under the terms of the AGPLv3.
