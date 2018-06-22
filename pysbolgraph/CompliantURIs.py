def get_display_id(uri):
    tokens = uri.split('/')
    return tokens[-2]


def get_version(uri):
    tokens = uri.split('/')
    return tokens[-1]


def get_persistent_identity(uri):
    tokens = uri.split('/')
    return '/'.join(tokens[:-1])
