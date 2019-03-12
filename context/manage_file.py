from contextlib import contextmanager

# write notes before push


class ManagedFile:
    """
    context managers are elegant to manage resource e.g.file ops, urlllib etc
    they provide a convenient way to simplify common resource management patterns
    by abstracting their functionality and allowing them to factored out and reused
    """
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


@contextmanager
def managed_file(file_name):
    try:
        f = open(file_name, 'w')
        yield f
    finally:
        f.close()
