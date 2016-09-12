#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>User Signup</title>
    </head>
    <body>
        <h1>User Signup</h1>
"""
page_footer = """
</body>
</html>
"""

form = """
<form method="post">
    <div>
        <label for="username">Username:</label>
            <input type="text" name="username" value="{username}">
            <p class="error">{error_username}</p>
        <label for="password">Password:</label>
            <input type="password" name="password" value="">
            <p class="error">{error_password}</p>
        <label for="verify">Verify:</label>
            <input type="password" name="verify" value="">
            <p class="error">{error_verify}</p>
        <label for"email">Email(optional):</label>
            <input type="text" name="email" value="{email}">
            <p class="error">{error_email}</p>
    </div>
    <br>
    <input type="submit" name="submit">
</form>
"""

def valid_username(username):
    if len(username)<3 or len(username)>20 or username.isalpha() == False:
        return False
    else:
        return True

def valid_password(password):
    if len(password)<3 or len(password)>20 or password.isalpha() == False:
        return False
    else:
        return True

def valid_verify(valid_password,verify):
    if valid_password != verify:
        return False
    else:
        return True

def valid_email(email):
    if email != "":
        if '@' not in email:
            return False
    return True
# # {0} can also be "%s"
#

class MainHandler(webapp2.RequestHandler):
    def get(self):
        response = page_header + form.format(username = "", email = "", error_username = "", error_password = "", error_verify="", error_email="")+ page_footer
        self.response.write(response)

    def post(self):
        have_error = False
        username = self.request.get("username")
        password = self.request.get("password")
        verify= self.request.get("verify")
        email = self.request.get("email")
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""

        if valid_username(username) == False:
            error_username = "This is not a valid username. The username must be between 3 and 20 characters."
            have_error = True

        if valid_password(password) == False:
            error_password = "This is not a valid password."
            have_error = True

        if valid_verify(password,verify) == False:
            error_verify = "The passwords do not match."
            have_error = True

        if valid_email(email) == False:
            error_email = "This is not a valid email."
            have_error = True

        if have_error == False:
            self.redirect("/Welcome")


        response = page_header + form.format(username = username,
                                                error_username = error_username,
                                                email = email,
                                                error_email = error_email,
                                                error_password = error_password,
                                                error_verify = error_verify) + page_footer
        self.response.write(response)

class Welcome(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/Welcome', Welcome)
], debug=True)
