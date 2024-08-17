import lazy_import_plus

def test_lazy():
    import lazy_import_plus

    lazy_cls = lazy_import_plus.lazy_class("email.parser.BytesHeaderParser")
    import email.parser

    assert email.parser.BytesHeaderParser is lazy_cls
    class Example(email.parser.BytesHeaderParser):
        pass

    assert issubclass(Example, lazy_cls)
    example = Example()
    assert not issubclass(Example, lazy_cls)
    assert email.parser.BytesHeaderParser is not lazy_cls
    assert issubclass(Example, email.parser.BytesHeaderParser)
    assert isinstance(example, Example)

if __name__ == '__main__':
    test_lazy()
