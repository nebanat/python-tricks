from context.manage_file import ManagedFile, managed_file


def open_write_file():
    with managed_file('pure.txt') as f:
        f.write('Hello Aaron')
        f.write('you will be great against all odds')


if __name__ == '__main__':
    open_write_file()
