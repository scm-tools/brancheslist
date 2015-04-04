from mercurial import hg, node

def identify(originalIdentify, ui, repo, *pats, **opts):
    if not opts["list"]:
        return originalIdentify(ui, repo, *pats, **opts)
    else:
        peer = hg.peer(ui, {}, pats[0])
        for name, rev in peer.branchmap().items():
            info = name
            for r in rev:
                info += ' ' + node.short(r)
            print(info)
