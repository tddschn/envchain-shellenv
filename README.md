# envchain shellenv

`envchain-shellenv` - prints export statements for your secrets in the keychain

- [envchain shellenv](#envchain-shellenv)
  - [Quick Start](#quick-start)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage:](#usage)
  - [Example](#example)
    - [Example config file](#example-config-file)
    - [Example output](#example-output)
  - [Develop](#develop)

## Quick Start
```bash
# install envchain first
# for macOS with Homebrew, run `brew install envchain'.
# see https://github.com/sorah/envchain for instructions for your OS.

# install envchain-shellenv
pipx install envchain-shellenv || pip install envchain-shellenv

# creates an example config at ~/.config/envchain-shellenv/keychain.ini
envchain-shellenv --create-example-config
# edit config file with your favorite editor
vim ~/.config/envchain-shellenv/keychain.ini

# export your envchain secrets in the current shell
eval "$(envchain-shellenv)"
# optionally add this line to your shell startup file
```

## Installation

### Prerequisites
- Required:
  - [`envchain`](https://github.com/sorah/envchain)
- Optional:
  - [`keyring`](https://github.com/jaraco/keyring)

    `keyring` is installed by default if you install `envchain-shellenv` with pipx.

    To use keyring when installing with `pip`, do `pip install 'envchain-shellenv[keyring]'`.

### pipx

This is the recommended installation method.

```
$ pipx install envchain-shellenv
```

### [pip](https://pypi.org/project/envchain-shellenv/)

```
$ pip install envchain-shellenv
```

## Usage:

`envchain-shellenv` prints export statements for your secrets in the keychain,

when you need your secrets in your shell env, just do `eval "$(envchain-shellenv)"`.

```
$ eesh -h # `eesh' is just an alias for `envchain-shellenv', you can use either.

usage: envchain-shellenv [-h] [-c CONFIG] [--create-example-config] [-u {envchain,keyring}] [--version]

envchain shellenv - prints export statements for your secrets in the keychain

options:
  -h, --help            show this help message and exit
  -c CONFIG, --config CONFIG
                        config file (default: /Users/tscp/.config/envchain-shellenv/keychain.ini)
  --create-example-config
                        create example config file (default: False)
  -u {envchain,keyring}, --use {envchain,keyring}
                        What to use to extract secrets (default: envchain)
  --version, -V         show program's version number and exit

Created by Teddy Xinyuan Chen || Homepage: https://github.com/tddschn/envchain-shellenv
```

## Example

### Example config file

```ini
[envchain]
; TEST = test TEST_SEC
; this set env var TEST to the TEST_SEC secret in envchain's test namespace,
; or the password of account TEST_SEC of test in your keychain app, e.g. Keychain Access.app on macOS.

; see envchain: https://github.com/sorah/envchain for more details.



; MULTILINE = test
; this shorthand is equivalent to MULTILINE = test MULTILINE

GH_API_TOKEN = github github-api-token
MY_SERVICE_API_KEY = my_service
```

### Example output

```bash
export GH_API_TOKEN='***'
export MY_SERVICE_API_KEY='***'
```


## Develop

```
$ git clone https://github.com/tddschn/envchain-shellenv.git
$ cd envchain-shellenv
$ poetry install
```