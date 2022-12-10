# QR Code generator website using Python and Flask
This website is use to Generate qr code accroding to the text enter by the user in the url end point.

## Code requirements
Flask `pip install flask`

qrcode `pip install qrcode`


## Description about the project
~The flows of the project goes like, First it will take the text by the user from the url end point.


~Then it will start creating a qr code by the help of "qrcode" which i installed before.


```
def generate(data):
    qr = qrcode.QRCode(
        version=None,
        box_size=10,
        border=2   
    )
    qr.add_data(data)
    qr.make(fit=True)
    fill = request.args.get("fill") or 'black'
    back_color = request.args.get("back_color") or 'white'
    image = qr.make_image(fill_color = fill, back_color=back_color)
    img_io = BytesIO()
    image.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
    
```
    
    
~ I used "qrcode" package to make a qrcode.It is very straight forward and easy to work with so i used this.

~ Imported BYTESIO to convert the image in to bytes.

~ Then BYTESIO will convert that image into bytes and will save that image by calling a save() method

## To Run the Project
This project contains only one file.

You can run this project by:-
`python3 app.py`

`localhost/(text)`
