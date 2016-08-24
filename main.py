#!/usr/bin/env python

form = """
<!DOCTYPE html><html><head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>
    <form method="post">
        <div>
            <label for="rot">Rotate by:</label>
            <input type="text" name="rot" value="0">
            <p class="error"></p>
        </div>
      <textarea name="text" style="height: 100px; width: 400px;">%(value)s</textarea>
      <br>
      <input type="submit">
    </form>


</body></html>
"""

import webapp2
from caesar import encrypt
import cgi

class MainHandler(webapp2.RequestHandler):
    def write_form(self, value=""):
        self.response.out.write(form % {"value":value})\

    def get(self):
        self.write_form()

    def post(self):
        userNumber = self.request.get('rot')
        userNumber = int(userNumber)
        userText = self.request.get('text')
        userText = encrypt(userText, userNumber)
        userText = cgi.escape(userText, quote = True)
        self.write_form(userText)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

#caesar stuff:
#answer = encrypt("Hello, Zach!", 2)
#print(answer)
# => prints Jgnnq, Bcej!
