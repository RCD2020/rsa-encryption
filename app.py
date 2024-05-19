'''
Robert Davis
2024.05.19
'''

from quart import Quart, render_template, request, jsonify

from rsa_encryption import generate_keys


app = Quart(__name__)


@app.route('/')
async def index():
    return await render_template('index.html')


@app.route('/get_keys', methods=['POST'])
async def get_keys():
    data = request.json
    public, private, modulus = generate_keys(data['bit_length'])

    return await jsonify({
        'public': public,
        'private': private,
        'modulus': modulus
    })


if __name__ == '__main__':
    app.run(debug=True)
