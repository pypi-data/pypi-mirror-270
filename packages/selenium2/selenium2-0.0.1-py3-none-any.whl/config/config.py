from pathlib import Path

# general purpose
DEBUG = True

# default timeout in seconds for explicit waits as an int
DEFAULT_TIMEOUT = 15

SCREENSHOT_ROOT_DIRECTORY = Path(__file__).parents[1] / 'screenshots'
# __file__ = 'C:/.../selenium2/config/config.py'
# parent => 'C:/.../selenium2/config/'
# parent => 'C:/.../selenium2/'
# screenshots => 'C:/.../selenium2/screenshots'
COOKIES_ROOT_DIRECTORY = Path(__file__).parents[1] / 'cookies'

# running speed of the script
DEFAULT_SPEED = 0.0