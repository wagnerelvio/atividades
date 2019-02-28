#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# -*- coding: ISO8859-1 -*-
import cgi
import cgitb
import locale
import time     # <1>
from datetime import datetime

today = datetime.now()
day = today.day
month = today.month
year = today.year

print "Content-type: text/html\n\n"
print "<meta http-equiv=\"refresh\" content=\"1\" >"
print "<html>\n<body>"
print "<div style=\"width: 100%; font-size: 40px; font-weight: bold; text-align: center;\">"
print "<h1>Curso Linux & Python</h1>"
print "<h2>Wagner Elvio</h2>"
print "<h3>Script em Python</h3>"
print "<h4>Atividades</h4>"
print "Data: ", time.strftime('%d %b %Y'),time.strftime ('%H:%M:%S'),  "|"
print "</div>\n</body>\n</html>"
