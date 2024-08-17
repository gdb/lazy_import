import lazy_import_plus
import importlib
from contextlib import contextmanager


def test_lazy_class():
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


def test_on_import():
    before = False
    after = False

    @contextmanager
    def on_import():
        nonlocal before, after
        before = True
        yield
        after = True

    modname = "sched"
    lazy_import_plus.lazy_module(modname, on_import=on_import())
    mod = importlib.import_module(modname)
    mod.__doc__

    assert before
    assert after


if __name__ == "__main__":
    test_lazy_class()
    test_on_import()
