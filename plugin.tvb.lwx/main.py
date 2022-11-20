import sys
from lib import router
# initialize
from controllers import main_controller as _


def main():
    print(sys.argv)
    if sys.argv[2] != '':
        router.handle(sys.argv[2])
    else:
        router.routes['landing_screen']()


main()
