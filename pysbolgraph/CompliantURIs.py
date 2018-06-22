
def getDisplayId(uri):
    tokens = uri.split('/')
    return tokens[-2]

def getVersion(uri):
    tokens = uri.split('/')
    return tokens[-1]

def getPersistentIdentity(uri):
    tokens = uri.split('/')
    return '/'.join(tokens[:-1])



