# parole

Very simply CLI password generator. This has probably been done a trillion times
already. However, here's the one I occasionally use.

## What it does

Generates a password by invoking `parole` and copies it to the clipboard (if
supported on your system).

## Installation

Install via pypi:

```bash
pip install parole --upgrade
```

Simply install from Github itself via:

```bash
pip install "git+ssh://git@github.com/merschformann/parole.git" --upgrade
```

## Usage

Get a password with default characteristics via:

```bash
parole
```

Display help:

```bash
parole --help
```

Get a password of specific length and alphabet via:

```bash
parole --alphabet "a!" --uppercase --digits --length 10
```

Resulting alphabet of this example is `aABCDEFGHIJKLMNOPQERSTUVWXYZ1234567890!`.
This is the result of combining the explicitly given symbols 'a' & '!', all
uppercase latin letters [A-Z] and all digits [0-9].

## Copy to clipboard

The generator uses `pyperclip` for copying the password to the clipboard. The
authors of `pyperclip` did great work of supporting multiple platforms. However,
if you run into problems, please consult the docs of the package:
https://pypi.org/project/pyperclip/

On Linux a package to support terminal copy to clipboard is needed. I usually
install `xsel`, e.g.:

```bash
sudo apt install xsel
```

## Why?

I use it for quickly generating a password while on the terminal (potentially
using a custom alphabet). Furthermore, for myself it was a similar effort as
googling a reliable and somewhat cryptographically secure solution. I am no
expert on the latter, but I trust the authors of the `secrets` module (see
https://docs.python.org/3/library/secrets.html#module-secrets).
