## Version 3.1.0 (2024-11-05)

* [Enhancement] Install version 3.1.0 of ansible-role-enrollmentreports by default.

## Version 3.0.0 (2024-10-07)

* [Enhancement] Drop support for Python 3.8; update the Ubuntu base image to
  "Ubuntu Jammy" (22.04).

When updating your plugin to this version, you'll need to rebuild the image.

## Version 2.5.0 (2024-08-01)

* [Enhancement] Support Tutor 18 and Open edX Redwood.

## Version 2.4.0 (2024-04-05)
* [Enhancement] Support Python 3.12.

## Version 2.3.0 (2024-01-12)

* [Enhancement] Support Tutor 17 and Open edX Quince.

## Version 2.2.0 (2023-08-23)

* [Enhancement] Support Tutor 16, Open edX Palm and Python 3.11.

## Version 2.1.0 (2023-04-21)

* Clone a revision from the Ansible role repo that matches the plugin
  version. That is, for version 2.1.0 of the plugin, clone the
  `v2.1.0` tag of the Ansible role repo (unless overridden with
  `ENROLLMENTREPORTS_REVISION`).

## Version 2.0.0 (2023-03-15)

* Add support for Tutor 15 and Open edX Olive.
  Tutor version 15.0.0 includes changes to the implementation of
  custom commands and thus requires changes in this plugin as well
  that are not backwards compatible.
  From version 2.0.0 this plugin only supports Tutor versions
  from 15.0.0 and Open edX Olive release.

## Version 1.2.0 (2023-02-20)

* [feature] Add ability to enable and disable the Kubernetes CronJob
  by suspending them (with `ENROLLMENTREPORTS_K8S_CRONJOB_ENABLE`).

## Version 1.1.0 (2023-02-14)

* Add the ability to set the frequency with which enrollment reports are
  generated, with `ENROLLMENTREPORTS_FREQUENCY`. Default `monthly`, also
  supports `weekly`.
* Add the ability to fetch the Ansible role from a custom repo
  (with `ENROLLMENTREPORTS_REPOSITORY`) and/or custom branch/tag/commit
  (with `ENROLLMENTREPORTS_REVISION`).

## Version 1.0.0 (2022-08-08)

* [BREAKING CHANGE] Support Tutor 14 and Open edX Nutmeg. This entails
  a configuration format change from JSON to YAML, meaning that from
  version 1.0.0 this plugin only supports Tutor versions from 14.0.0
  (and with that, only Open edX versions from Nutmeg).

## Version 0.1.0 (2022-06-29)
￼
￼* [refactor] Use Tutor v1 plugin API

## Version 0.0.1 (2022-03-24)

**Experimental. Do not use in production.**

* Add `enrollmentreports` command to `tutor local` to run the
  enrollment reports Ansible playbook.
* Add enrollmentreports-job service for `tutor k8s`.

