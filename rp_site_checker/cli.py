import argparse

def read_user_cli_args():
    """
    handle CLI arguments and options
    """
    # build parser object
    parser = argparse.ArgumentParser(
        # program name
        prog="rp_site_checker",
        # text when called with --help option
        description="check the availability of a URL"
    )
    # add command line arguments for users to enter
    parser.add_argument(
        # -u and --urls switches
        "-u",
        "--urls",
        # name for argument
        metavar="URLs",
        # accept a list of command line arguments
        nargs="+",
        # data type of arguments
        type=str,
        # no default values
        default=[],
        # message for user
        help="enter one or more site URLs"
    )
    
    # add url from files
    parser.add_argument(
        # -f and --input-file are switches
        "-f",
        "--input-file",
        
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )
    # returns namespace object
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """
    display results of a connectivity check
    """
    print(f"the status of {url} is:", end=" ")
    if result:
        print("Online!")
    else:
        print(f"Offline?, \n Error: '{error}'")
    
    