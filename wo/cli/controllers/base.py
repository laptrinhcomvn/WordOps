"""WordOps base controller."""

from cement.core.controller import CementBaseController, expose
from wo.core.variables import WOVariables
VERSION = WOVariables.wo_version

BANNER = """
WordOps v%s
Copyright (c) 2019 WordOps.
""" % VERSION


class WOBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = ("An essential toolset that eases WordPress "
                       "site and server administration with Nginx")
        arguments = [
            (['-v', '--version'], dict(action='version', version=BANNER)),
        ]

    @expose(hide=True)
    def default(self):
        self.app.args.print_help()
