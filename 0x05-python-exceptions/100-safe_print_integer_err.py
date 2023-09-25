#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        err_msg = "Exception: "
        sys.stderr.write("{}{}\n".format(err_msg, err))
        return (False)
    return (True)
