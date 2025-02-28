import qrcode
import os
from dotenv import load_dotenv

load_dotenv()
ssid = "MTQ"

hidden = False
password = os.getenv('password')
wifi_string = f"WIFI:S:{ssid};T:WPA;P:{password};H:{str(hidden).lower()};;"

# check password
if password is None:
    raise ValueError("no password found")
# generate qr code
qr = qrcode.QRCode( version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,)

qr.add_data(wifi_string)
qr.make(fit=True)

# make img from qr code instance
img = qr.make_image(color="black",bg="white")

# save img
img.save(f"{ssid}_wifi_qr.png")
print(f"QR code generated and saved as {ssid}_wifi_qr.png")