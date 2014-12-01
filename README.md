Author:  Rich Grimes
Twitter:  @saltyCoder

Copyright (C) 2014 by Rich Grimes

---------------------------------------------------------------------------

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.

---------------------------------------------------------------------------

MathCaptchaByPass is a Proof of Concept Python script to test the bypassing of a HTML-based math CAPTCHA.  Along with this script you will find an ASP .NET Web Forms site to test the script against.

The proof of concept is a password reset form.  The goal of this exercise is to by-pass the Math CAPTCHA so we can harvest user names.  Here is a quick overview of what the Python script does in the proof of concept:

  * Get user name from list
  * Make a HTTP GET Request to the web site to establish a session
  * Retrieve the HTTP Response and scrap the HTML for the CAPTCHA question
  * Extract the numbers from the CAPTCHA question and perform the math calculation
  * Create an HTTP POST Request to submit the web form with the user name and answer to the math calculation
  * Retrieve the HTTP Response from the POST Request and scrap the HTML for the error message.  If the error message is for a failed user name check the next user name.

---------------------------------------------------------------------------

Technical Details

MathCaptchaByPass.py

  * Python 3
  * http://www.python.org

MathCaptchaByPass  Web Site

  * .NET 4.5
  * ASP.NET Web Forms
  * Visual Studio Express 2013
  * http://www.visualstudio.com/free

