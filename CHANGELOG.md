## Unreleased

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

