# qr_generator.py

#Run with: 
#pip install qrcode[pil]
#python qr_generator.py

import qrcode

 

data = "https://mountaingoat.notion.site/32fb86050ca58047a788e781ad8764a5"  # Replace with your URL or text

 

qr = qrcode.QRCode(

    version=1,  # 1–40, controls size; 1 is smallest

    error_correction=qrcode.constants.ERROR_CORRECT_M,

    box_size=10,

    border=4,

)

qr.add_data(data)

qr.make(fit=True)

 

img = qr.make_image(fill_color="black", back_color="white")

img.save("TestForm.png")