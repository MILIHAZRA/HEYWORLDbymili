import qrcode
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,
                 border=4)

qr.add_data("https://github.com/MILIHAZRA/HEYWORLDbymili")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
img.save("MILIHAZRA_github.png")
print("QR Code generated and saved as 'my_qrcode.png'")
