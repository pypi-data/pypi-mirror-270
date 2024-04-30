'''Generate port numbers for tests.'''


class BasePort():
    '''Generate unique port numbers for a test file.'''
    _base_port: int

    def __init__(self, base_port: int) -> None:
        self._base_port = base_port

    def next(self) -> int:
        '''Return the next port number.'''
        retval = self._base_port
        self._base_port += 1
        return retval
