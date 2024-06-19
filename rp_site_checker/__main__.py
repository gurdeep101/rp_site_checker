import pathlib
import sys

from rp_site_checker.checker import site_is_online
from rp_site_checker.cli import display_check_result, read_user_cli_args

# import from cli module
# from rp_site_checker import read_user_cli_args

def main():
    """
    run rp checker
    """
    # call function to parse command line arguments
    # stored as user_args
    user_args = read_user_cli_args()
    # list of target urls from helper function
    urls = _get_websites_urls(user_args)
    # check if list empty
    if not urls:
        # print error message and exit
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)
    # run conectivity checks synchronously
    _synchronous_check(urls)
    
def _get_websites_urls(user_args):
    """
    extract urls from cli input stored as user_args above
    1st from command line and then from file
    """
    # store list of variables provided at command line
    # return empty list if no input
    urls = user_args.urls
    # check for url input from files
    # if input received then call helper function to parse inputs
    if user_args.input_file:
        urls += _read_urls_from_file(user_args.input_file)
    # return list of URLs
    return urls

def _read_urls_from_file(file):
    # turn file into pathlib.Path object for processing
    file_path = pathlib.Path(file)
    # if input is a file then open and store each url as a separate file
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            # exit if URLs present
            if urls:
                return urls
            # else print error message
            print(f"Error: Empty input file, {file}", file=sys.stderr)
    else:
        print("Error: input file not found", file=sys.stderr)
    return []

def _synchronous_check(urls):
    """
    check each url and loop over them
    """
    for url in urls:
        # empty variable for error message
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        # display results on screen
        display_check_result(result, url, error)
        
if __name__ == "__main__":
    main()