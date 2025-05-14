import inspect
from numpydoc.docscrape import NumpyDocString, Parameter
import sys


modname = sys.argv[1]
mod = __import__(modname)


def is_submodule(child, parent):
        return child.__name__.startswith(parent.__name__ + ".")



def walk_mod(mod, path=''):
    members_names = mod.__all__
    out = {}

    for member_name in members_names:
        member = getattr(mod, member_name)

        if inspect.isfunction(member):
            if member.__doc__:
                out[member_name] = dict(NumpyDocString(member.__doc__))
                npdoc = out[member_name]
                for key, val in npdoc.items():
                    if isinstance(val, list) and len(val) > 0:
                        # Unpack parameter list
                        if isinstance(val[0], Parameter):
                            npdoc[key] = [
                                {
                                    'name': el.name,
                                    'type': el.type,
                                    'desc': el.desc
                                }
                                for el in val
                            ]

        if inspect.ismodule(member) and is_submodule(member, mod):
            out[member_name] = walk_mod(member, path=path + '.' + member_name)

    return out


print(walk_mod(mod, path='skimage'))
#print(walk_mod(mod))
