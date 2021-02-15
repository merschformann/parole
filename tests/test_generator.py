from parole import generator


def test_generate():
    length = 10
    alphabet = "abc"
    pw = generator.generate(length, alphabet)
    assert len(pw) == 10, ""
    for l in pw:
        assert l in alphabet


if __name__ == "__main__":
    test_generate()
    print("Everything passed")
