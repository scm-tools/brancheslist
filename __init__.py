from mercurial import commands, extensions

import wrappers

wrapcmds = { # cmd: generic, target, fixdoc, opts
    'identify': (False, None, False, [
        ('l', 'list', None, 'List remote branches'),
    ]),
}

def extsetup(ui):
    """insert command wrappers for a bunch of commands"""

    docvals = {'extension': 'brancheslist'}
    for cmd, (generic, target, fixdoc, opts) in wrapcmds.iteritems():

        if fixdoc and wrappers.generic.__doc__:
            docvals['command'] = cmd
            docvals['Command'] = cmd.capitalize()
            docvals['target'] = target
            doc = wrappers.generic.__doc__.strip() % docvals
            fn = getattr(commands, cmd)
            fn.__doc__ = fn.__doc__.rstrip() + '\n\n    ' + doc

        wrapped = generic and wrappers.generic or getattr(wrappers, cmd)
        entry = extensions.wrapcommand(commands.table, cmd, wrapped)
        if opts:
            entry[1].extend(opts)