# /// pyproject
# [project]
# dependencies = [
#     "rst-to-myst"
# ]

import inspect
from numpydoc.docscrape import NumpyDocString, Parameter
import sys
import types

import rst_to_myst


modname = sys.argv[1]
mod = __import__(modname)


def is_submodule(child: types.ModuleType, parent: types.ModuleType) -> bool:
    return child.__name__.startswith(parent.__name__ + ".")


def rst2myst(rst: str | list) -> str:
    if isinstance(rst, list):
        rst = "\n".join(rst)

    return rst_to_myst.mdformat_render.rst_to_myst(rst).text.strip()


def walk_mod(mod: types.ModuleType, path: str = "") -> dict:
    members_names = mod.__all__
    out = {}

    for member_name in members_names:
        member = getattr(mod, member_name)

        if inspect.isfunction(member):
            if member.__doc__:
                out[member_name] = dict(NumpyDocString(member.__doc__))
                npdoc = out[member_name]

                rst_fields = ["Extended Summary", "Notes"]
                for field in rst_fields:
                    if npdoc.get(field):
                        npdoc[field] = rst2myst(npdoc[field])

                for key, val in npdoc.items():
                    if isinstance(val, list) and len(val) > 0:
                        # Unpack parameter list
                        if isinstance(val[0], Parameter):
                            npdoc[key] = [
                                {
                                    "name": el.name,
                                    "type": el.type,
                                    "desc": rst2myst(el.desc),
                                }
                                for el in val
                            ]

        if inspect.ismodule(member) and is_submodule(member, mod):
            out[member_name] = walk_mod(member, path=path + "." + member_name)

    return out


print(walk_mod(mod, path="skimage"))
