#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        err_msg = "Exception: Unknown format code 'd' for object of type 'str'"
        sys.stderr.write(err_msg + "\n")
        return (False)
    else:
        return (True)
