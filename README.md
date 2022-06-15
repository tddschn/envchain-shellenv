# envchain shellenv

`envchain-shellenv` - prints export statements for your secrets in the keychain

so that you can do `eval "$(envchain-shellenv)"`.

Use with [`envchain`](https://github.com/sorah/envchain) for maximum convenience.

- [envchain shellenv](#envchain-shellenv)
  - [Quick Start](#quick-start)
  - [Installation](#installation)
    - [Prerequisites](#prerequisites)
    - [pipx](#pipx)
    - [pip](#pip)
  - [Usage:](#usage)
  - [Example](#example)
    - [Example config file](#example-config-file)
  - [Develop](#develop)

## Quick Start
```bash
# install envchain first, and add your secrets to your keychain app via envchain
# for macOS with Homebrew, run `brew install envchain'.
# see https://github.com/sorah/envchain for more details.

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

```yaml
test:
  TEST: TEST_SEC
  MULTILINE:
aws: # the envchain namespace
  AWS_SECRET_KEY:
  AWS_ROOT_PW: envchain-aws-root-pw
  # sets AWS_ROOT_PW env var to envchain-aws-root-pw in the aws namespace of envchain
no-item:
  # this will be skipped

```


## Develop

```
$ git clone https://github.com/tddschn/envchain-shellenv.git
$ cd envchain-shellenv
$ poetry install
```