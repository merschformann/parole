import collections
from parole import generator
import string
import subprocess
import sys

# Test directly
def test_generate():
    length = 10
    alphabet = "abc"
    pw = generator.generate(length, alphabet)
    assert len(pw) == 10, ""
    for l in pw:
        assert l in alphabet


# Test CLI
def test_main():

    # Prepare
    base = [sys.executable, "../parole/generator.py"]
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
        cmd = [*base, "-s", *test.args]
        cmd_string = " ".join(test.args)
        print(f"Invoking: {cmd_string}")
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        assert result.returncode == 0
        pw = result.stdout.decode("utf-8").replace("\n", "").replace("\r", "")
        print(pw)
        if test.length > 0:
            assert len(pw) == test.length
        for l in pw:
            assert l in test.alphabet


if __name__ == "__main__":
    test_generate()
    test_main()
    print("Everything passed")
