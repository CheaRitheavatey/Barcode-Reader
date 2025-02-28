# QR code

1. install qrcode library
2. to use:
    - call constructor .QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

    - to add data to QR code: .add_data(data)

    - make img from QR code: .make_image(fill_color="black", back_color="white")

    - save img: .save(filename)

    -  # Format the Wi-Fi credentials for QR code
    wifi_string = f"WIFI:S:{ssid};T:WPA;P:{password};H:{str(hidden).lower()};;"