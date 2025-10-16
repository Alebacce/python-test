import pyqrcode 
from pyqrcode import QRCode 

site = "https://www.youtube.com/watch?v=_fDhiLnyFoo"

url = pyqrcode.create(site)

url.svg("gilmour_test.svg", scale = 8)