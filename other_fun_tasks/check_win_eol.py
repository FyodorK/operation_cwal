import os


def check_windows_eol(path_to, encoding_="utf-8"):
    """
    Check files for windows end of line 'CLRF'
    :param path_to: Path to file of folder as string
    :param encoding_: encoding as string
    :return: list of results if a file or files content 'CLRF';  0 if not or 1 if given path not exits as int
    """
    def _process_file(path, enc):
        info_line = "In file {} : line with number {} has windows EOL"
        if not path.startswith('.'):
            with open(path, encoding=str(enc), newline='\r\n') as file_object:
                count = 0
                for line in file_object:
                    if line.endswith('\r\n'):
                        info = info_line.format(path_to, count)
                        result.append(info)
                    count += 1
    result = []
    if not os.path.exists(path_to):
        return 1
    if os.path.isfile(path_to):
        _process_file(path_to, encoding_)
    elif os.path.isdir(path_to):
        for root, folders, files, in os.walk(path_to, topdown=False):
            for folder in [os.path.join(root, fld) for fld in folders]:
                check_windows_eol(folder)
            for file_ in [os.path.join(root, fl) for fl in files]:
                _process_file(file_, encoding_)
    return result if result else 0
