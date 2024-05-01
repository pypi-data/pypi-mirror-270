# [Mailme API](http://mailme-api.hive.pt)

API Python client for the Mailme service.

## Configuration

| Name                | Type  | Default                          | Description                                             |
| ------------------- | ----- | -------------------------------- | ------------------------------------------------------- |
| **MAILME_BASE_URL** | `str` | `https://mailme.bemisc.com/api/` | The base URL for the Mailme API requests.               |
| **MAILME_KEY**      | `str` | `None`                           | The secret key to be used to authenticate API requests. |

## Installation

```bash
pip install mailme-api
```

## Usage

```bash
RECEIVERS="receiver@domain.com" \
CONTENTS="Hello World" \
python -m mailme.scripts.sender
```

## License

Mailme API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://app.travis-ci.com/hivesolutions/mailme-api.svg?branch=master)](https://travis-ci.com/github/hivesolutions/mailme-api)
[![Build Status GitHub](https://github.com/hivesolutions/mailme-api/workflows/Main%20Workflow/badge.svg)](https://github.com/hivesolutions/mailme-api/actions)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/mailme-api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/mailme-api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/mailme-api.svg)](https://pypi.python.org/pypi/mailme-api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
