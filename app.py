from flask import Flask,request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return "add a text in a url to get your own qr code"


@app.route('/<string:data>')
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


if __name__ == '__main__':
    app.run(debug=True)