# coding: utf-8

import nose
import pkgutil
import girlfriend.testing

excludes = {
    "girlfriend.testing.plugin.mail",
    "girlfriend.testing.runalltests",
    "girlfriend.testing.tools.test_workflow",
}


def main():
    test_modules = [""]
    for importer, modname, ispkg in pkgutil.walk_packages(
            path=girlfriend.testing.__path__,
            prefix="girlfriend.testing."):
        if ispkg:
            continue
        if modname in excludes:
            continue
        test_modules.append(modname)
    nose.run(argv=test_modules)

if __name__ == "__main__":
    main()
