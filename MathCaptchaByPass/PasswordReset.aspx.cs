/* *****************************************************************************
 *  MathCaptchaByPass Project
 * 
 *  A web site for testing the by-passing of a math captcha
 * 
 *  Copyright (C) 2014 by Rich Grimes
 *
 *  This program is free software: you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation, either version 3 of the License, or
 *  (at your option) any later version.
 *  
 *  This program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *  
 * *****************************************************************************/

using System;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class PasswordReset : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {

        Message.Visible = false;

        if (!Page.IsPostBack)
        {
            CreateMatchCaptcha();
        }

    }

    protected void btnReset_Click(object sender, EventArgs e)
    {
        bool validCaptcha = false;

        try
        {
            Int32 captcha = Convert.ToInt32(txtCaptcha.Text);

            if ((Convert.ToInt32(Session.Contents["x"]) + Convert.ToInt32(Session.Contents["y"])) == captcha)
            {
                validCaptcha = true;
            }
        }
        catch
        {
            validCaptcha = false;
        }

        if (!validCaptcha)
        {
            Message.InnerText = "CAPTCHA is not correct!";
            CreateMatchCaptcha();
        }
        else
        {
            if (UserName.Text == "HappyGilmore")
            {
                Message.InnerText = "A temporary password has been sent to your e-mail on your account.";
            }
            else
            {
                Message.InnerText = "User name is invalid.  Please double check your user name.";
                CreateMatchCaptcha();
            }
        }

        Message.Visible = true;

    }

    private void CreateMatchCaptcha()
    {

        Random r = new Random();
        Int32 x = r.Next(0, 10);
        Int32 y = r.Next(0, 20);

        Captcha.InnerText = String.Format("What is {0} + {1}?", x, y);

        Session.Contents["x"] = x.ToString();
        Session.Contents["y"] = y.ToString();

    }
}