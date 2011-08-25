# coding: utf-8

from prymatex.utils.i18n import ugettext as _

class AlreadyRunningError(Exception):
    pass

class UnsupportedPlatformError(Exception):
    pass

class APIUsageError(Exception):
    '''
    Thrown when something is violating the way Prymatex is meant to be
    used
    '''
    pass


class FileDoesNotExistError(Exception):
    def __init__(self, path):
        self.path = path
        super(FileDoesNotExistError, self).__init__(_("%s does not exist") % path)        

class InvalidField(APIUsageError):
    def __init__(self, name, valid_names):
        cad = "%s is not a valid name. Valid names are: %s" % (name, ", ".join(valid_names))
        super(InvalidField, self).__init__(cad)
        
class FileNotSupported(Exception):
    pass