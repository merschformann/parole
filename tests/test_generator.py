import collections
from parole import generator
import pathlib
import string
import subprocess
import sys


# Test directly
def test_generate():
    length = 10
    alphabet = "abc"
    pw = generator.generate(length, alphabet)
    assert len(pw) == 10, ""
    for letter in pw:
        assert letter in alphabet


# Test CLI
def test_main():

    # Prepare
    gen_path = str(
        pathlib.Path(__file__)
        .parent.joinpath("../parole/generator.py")
        .resolve(strict=True)
    )
    base = [sys.executable, gen_path]
    CliTest = collections.namedtuple("Test", ["args", "alphabet", "length"])

    # Define test cases
    tests = [
        CliTest(["--digits"], string.digits, -1),
        CliTest(["--letters"], string.ascii_letters, -1),
        CliTest(["--upper"], string.ascii_uppercase, -1),
        CliTest(["--lower"], string.ascii_lowercase, -1),
        CliTest(
            ["-l", "50"],
            string.ascii_letters + string.digits + generator.SPECIAL_CHARACTERS,
            50,
        ),
        CliTest(["-a", "abc", "--digits", "-l", "5"], string.digits + "abc", 5),
        CliTest(["--alphabet", "a", "--length", "20"], "a", 20),
    ]

    # Run all test cases
    for test in tests:
        cmd = [*base, "-s", "--no-clipboard", *test.args]
        cmd_string = " ".join(test.args)
        print(f"Invoking: {cmd_string}")
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        assert result.returncode == 0
        pw = result.stdout.decode("utf-8").replace("\n", "").replace("\r", "")
        print(pw)
        if test.length > 0:
            assert len(pw) == test.length
        for letter in pw:
            assert letter in test.alphabet


if __name__ == "__main__":
    test_generate()
    test_main()
    print("Everything passed")
