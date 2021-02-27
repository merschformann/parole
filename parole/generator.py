import argparse
import pyperclip
import secrets
import string

# ==================== Constants

SPECIAL_CHARACTERS = "@%$#+-*/=!?_()[]:;"

DEFAULT_ALPHABET = string.ascii_letters + string.digits + SPECIAL_CHARACTERS

# ==================== PW generation


def generate(length, alphabet):
    """
    Generates a password of the given length using the given alphabet.
    Any duplicates will be removed from the alphabet to ensure equal probabilities.
    """
    # Use only unique values
    alphabet = list(set(alphabet))
    # Generate password
    return "".join(secrets.choice(alphabet) for _ in range(length))


# ==================== Argument handling


def setup_args():
    parser = argparse.ArgumentParser(description="password generator")

    # Define alphabet control flags
    parser.add_argument(
        "--alphabet",
        "-a",
        type=str,
        nargs="?",
        default=None,
        help="list of characters to be used for generating the password",
    )
    parser.add_argument(
        "--digits",
        dest="digits",
        action="store_true",
        default=False,
        help="adds digits [0-9] to a custom alphabet",
    )
    parser.add_argument(
        "--letters",
        dest="letters",
        action="store_true",
        default=False,
        help="adds latin letters [a-z,A-Z] to a custom alphabet",
    )
    parser.add_argument(
        "--lowercase",
        dest="lowercase",
        action="store_true",
        default=False,
        help="adds lowercase latin letters [a-z] to a custom alphabet",
    )
    parser.add_argument(
        "--uppercase",
        dest="uppercase",
        action="store_true",
        default=False,
        help="adds uppercase latin letters [A-Z] to a custom alphabet",
    )

    # Define further options
    parser.add_argument(
        "--length",
        "-l",
        type=int,
        default=20,
        help="length of the password",
    )
    parser.add_argument(
        "--show",
        "-s",
        dest="show",
        action="store_true",
        default=False,
        help="indicates whether to show the password",
    )

    parser.add_argument(
        "--no-clipboard",
        dest="no_clipboard",
        action="store_true",
        default=False,
        help="indicates whether copying the password will be skipped",
    )

    return parser


# ==================== Entry point


def main():
    # Read arguments
    parser = setup_args()
    args = parser.parse_args()

    # Some sanity checks
    if args.length <= 0:
        print(f"Error: invalid password length: {args.length}")
        return

    # Determine alphabet (any duplicates will be removed by generation procedure)
    # Use default alphabet, if no options are present
    if (
        args.alphabet is not None
        or args.digits
        or args.lowercase
        or args.uppercase
        or args.letters
    ):
        if args.alphabet is None:
            alphabet = ""
        else:
            alphabet = args.alphabet
    else:
        alphabet = DEFAULT_ALPHABET
    # Extend alphabet according to options
    if args.digits:
        alphabet = alphabet + string.digits
    if args.lowercase:
        alphabet = alphabet + string.ascii_lowercase
    if args.uppercase:
        alphabet = alphabet + string.ascii_uppercase
    if args.letters:
        alphabet = alphabet + string.ascii_letters

    # Another sanity check
    if len(alphabet) <= 0:
        print(f"Error: empty alphabet given")
        return

    # Generate password
    pw = generate(args.length, alphabet)

    # Print and copy
    if args.show:
        print(pw)
    if not args.no_clipboard:
        try:
            pyperclip.copy(pw)
        except:
            print(
                "Error: no copy/paste mechanisms found for your system."
                + " See https://pyperclip.readthedocs.io/en/latest/index.html#not-implemented-error for help"
            )


if __name__ == "__main__":
    main()
