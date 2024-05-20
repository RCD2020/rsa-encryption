'''
Robert Davis
2024.05.19
'''

from quart import Quart, render_template, request
from json import loads as json_loads

from rsa_encryption import generate_keys, encrypt_text, decrypt_text


app = Quart(__name__)


@app.route('/', methods=['GET', 'POST'])
async def index():
    keys = ''
    encrypted_message = ''
    decrypted_message = ''

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

    if request.method == 'POST' and (await request.form)['type'] == 'decrypt':
        encrypted: str = (await request.form)['encrypted']
        private = int((await request.form)['private_key'])
        modulus = int((await request.form)['modulus'])

        encrypted = [int(x) for x in encrypted.strip('[]').split(', ')]

        decrypted_message = decrypt_text(
            encrypted, private, modulus
        )

    return await render_template(
        'index.html', keys=keys, encrypted_message=encrypted_message,
        decrypted_message=decrypted_message
    )


if __name__ == '__main__':
    app.run(debug=True)
