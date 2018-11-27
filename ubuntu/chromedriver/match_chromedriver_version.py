import sys
import argparse

import requests


parser = argparse.ArgumentParser(
    description="Match proper chromedriver version for google chrome"
)
parser.add_argument("chrome_version", type=str, help="google-chrome-stable --version")
namespace = parser.parse_known_args()[0]

latest_chromedriver_version = requests.get(
    "https://chromedriver.storage.googleapis.com/LATEST_RELEASE"
).text

notes = requests.get(
    "https://chromedriver.storage.googleapis.com/{}/notes.txt".format(
        latest_chromedriver_version
    )
).text


chrome_version_str = namespace.chrome_version
chrome_major_version = int(chrome_version_str.split()[2].split(".")[0])

for version in notes.split("\n\n"):
    lines = version.split("\n")
    if not (len(lines)):
        continue
    try:
        chromedriver_version = lines[0].split()[1][1:]
    except IndexError:
        continue
    try:
        min_chrome_str, max_chrome_str = lines[1].split()[2].strip("v").split("-")
        min_chrome = int(min_chrome_str)
        max_chrome = int(max_chrome_str)
        if min_chrome <= chrome_major_version <= max_chrome:
            print(chromedriver_version)
            sys.exit(0)
    except IndexError:
        continue
    # print(chromedriver_version, min_chrome, max_chrome)
sys.exit(1)
