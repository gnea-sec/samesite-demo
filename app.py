from flask import Flask, jsonify, request, make_response, send_file, send_from_directory, render_template
import random
import os.path

app = Flask(__name__)

STATIC_DIR = os.path.join(os.path.dirname(__file__), 'static')

# Home route
@app.route('/')
def home():
    return send_from_directory(STATIC_DIR, 'index.html', mimetype='text/html')

# Set the cookie value randomly
@app.route('/setcookie', methods=['GET'])
def set_cookie():
    cookieval = str(random.randint(100, 999))
    message = f"Cookie set: {cookieval}"
    response = make_response(render_template('display_message.html', message_value=message))
    response.set_cookie('samesitecookie', cookieval, path='/', httponly=True, samesite='Strict')
    response.headers['Content-Security-Policy'] = "script-src 'self'"

    return response

# Show the received cookie value
@app.route('/showcookie', methods=['GET'])
def show_cookie():
    cookie_value = request.cookies.get('samesitecookie')
    if cookie_value:
        message = f"Cookie: {cookie_value}"
    else:
        message = "No cookie received"
    return render_template('display_message.html', message_value=message)

@app.route('/pdflink')
def pdflink():
    response = send_from_directory(STATIC_DIR, 'link.pdf', mimetype='application/pdf')
    response.headers['Content-Security-Policy'] = "script-src 'self'"

    return response

@app.route('/frame')
def frame_page():
    response = send_from_directory(STATIC_DIR, 'frame.html', mimetype='text/html')
    response.headers['Content-Security-Policy'] = "script-src 'self'"

    return response

@app.route('/link')
def link_page():
    response = send_from_directory(STATIC_DIR, 'link.html', mimetype='text/html')
    response.headers['Content-Security-Policy'] = "script-src 'self'"

    return response

@app.route('/links')
def links_page():
    response = send_from_directory(STATIC_DIR, 'links.html', mimetype='text/html')
    response.headers['Content-Security-Policy'] = "script-src 'self'"

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181)
