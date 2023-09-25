#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        err_msg = "Exception: Unknown format code 'd' for object of type 'str'\n"
        sys.stderr.write(err_msg)
        return (False)
    return (True)
