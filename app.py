'''
Robert Davis
2024.05.19
'''

from quart import Quart, render_template, request

from rsa_encryption import generate_keys, encrypt_text


app = Quart(__name__)


@app.route('/', methods=['GET', 'POST'])
async def index():
    keys = ''
    encrypted_message = ''

    if request.method == 'POST' and (await request.form)['type'] == 'keys':
        bit_length = int((await request.form)['bit_length'])

        public, private, modulus = generate_keys(bit_length)
        keys = {
            'public': (public, modulus),
            'private': (private, modulus)
        }
    
    if request.method == 'POST' and (await request.form)['type'] == 'encrypt':
        message = (await request.form)['message']
        public = int((await request.form)['public_key'])
        modulus = int((await request.form)['modulus'])

        encrypted_message = encrypt_text(
            message, public, modulus
        )

    return await render_template(
        'index.html', keys=keys, encrypted_message=encrypted_message
    )


if __name__ == '__main__':
    app.run(debug=True)
