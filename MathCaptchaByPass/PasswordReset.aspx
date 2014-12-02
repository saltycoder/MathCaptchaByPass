<%@ Page Language="C#" AutoEventWireup="true" CodeFile="PasswordReset.aspx.cs" Inherits="PasswordReset" %>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
    <title>Match Captcha By-Pass</title>
</head>
<body>
    <form id="form1" runat="server">

    <h2>
        Forgot your password?
    </h2>

    <div style="margin:25px;">

        <div style="margin:10px;">
            No problem! We'll email you instructions to reset it.
        </div>

        <div id="Message" runat="server" style="color:#f00;margin:10px"></div>
    
        <div style="margin:10px;">
            <label>User Name</label><br />
            <asp:TextBox id="UserName" runat="server" style="width:300px" />
        </div>

        <div style="margin:10px;">
            <label for="txtCaptcha" id="Captcha" runat="server" /> <br />
            <asp:TextBox id="txtCaptcha" runat="server" style="width:300px" />
        </div>

        <div style="margin:10px;">
            <asp:Button id="Reset" runat="server" Text="Reset Password" OnClick="btnReset_Click" />
        </div>

    </div>
    </form>
</body>
</html>
