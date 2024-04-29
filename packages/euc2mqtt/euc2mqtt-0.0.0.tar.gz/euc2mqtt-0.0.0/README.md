# euc2mqtt

[![License](https://img.shields.io/github/license/islandcontroller/euc2mqtt)](LICENSE) ![PyPI - Version](https://img.shields.io/pypi/v/euc2mqtt)

A tool for publishing status data from a local Eaton UPS Companion service to Homeassistant.

## Installation

A pre-built package is hosted on [PyPI](https://pypi.org/project/euc2mqtt/) and can be installed and updated using the [`pip`](https://pip.pypa.io/en/stable/getting-started/) utility:

    pip install -U euc2mqtt

Windows binaries are provided on the [GitHub Releases](https://github.com/islandcontroller/euc2mqtt/releases) page.


## Usage

    python -m euc2mqtt --mqtt <broker hostname> --username <user> --password <password>

> [!NOTE]
> This tool needs to run on the same host as Eaton UPS Companion, as EUC in its default configuration only accepts connections on `localhost:4679`.

