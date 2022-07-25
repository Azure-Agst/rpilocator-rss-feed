import os
import sys

# there is definitely a better solution, but this works for now :)

def main():

    # get user driver
    driver = os.getenv('DRIVER') \
        if os.getenv('DRIVER') is not None else ""
    driverfile = f"rpilocator-rss-{driver.lower()}.py"
    
    # see if driver exists
    if not os.path.exists(driverfile):
        raise Exception(
            f"\"{driver}\" is not a valid option! " +\
            f"Make sure DRIVER is set and {driverfile} exists!"
        )
    
    # call that file
    # sys.executable contains path of running Python interpreter
    os.system(f"{sys.executable} {driverfile}")

    # return ok
    return 0

if __name__ == "__main__":
    exit(main())