from functools import partial
import gc
import lazy_import_plus
import sys
import types


def is_lazy_class(cls):
    return cls.__bases__ == (LazyClass,)


def is_lazy_module(module):
    return isinstance(module, lazy_import_plus.LazyModule)


class LazyClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.__resolve__()
        return instance

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if is_lazy_class(cls):
            # Initial types.new_class creation
            return
        cls.subclasses.append(cls)

    @classmethod
    def real(cls):
        # TODO: do this in another place?
        lazy_import_plus.module_state[cls.module]['attrs'].pop(cls.name)
        return getattr(cls.module, cls.name)

    @classmethod
    def __resolve__(subcls):
        replaced = []
        bases = []
        for i, curr in enumerate(subcls.__bases__):
            if is_lazy_class(curr):
                bases.append(curr.real())
                replaced.append(i)
            else:
                bases.append(curr)
        subcls.__bases__ = tuple(bases)
        return replaced

    @classmethod
    def __resolve_all__(cls):
        for subcls in cls.subclasses:
            if subcls is cls:
                continue
            subcls.__resolve__()


def _lazy_body(ns, *, modname, name, module):
    ns["modname"] = modname
    ns["name"] = name
    ns["module"] = module
    ns["subclasses"] = []


def lazy_class(modname):
    modname, _, name = modname.rpartition(".")
    module = lazy_import_plus.lazy_module(modname)
    if is_lazy_module(module):
        cls = types.new_class(
            f"{modname}#lazy",
            bases=(LazyClass,),
            exec_body=partial(_lazy_body, modname=modname, name=name, module=module),
        )
        lazy_import_plus.module_state[module]['attrs'][name] = cls
    else:
        cls = getattr(module, name)
    return cls
