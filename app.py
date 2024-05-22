'''
Robert Davis
2024.05.19
'''

from quart import Quart, render_template, request

from rsa_encryption import generate_keys, encrypt_text, decrypt_text


app = Quart(__name__)


@app.route('/', methods=['GET', 'POST'])
async def index():
    public, private, modulus = [''] * 3
    message, encrypted, encrypted_message, decrypted_message = [''] * 4
    bit_length = 32

    if request.method == 'POST':
        form = await request.form

        public = int(form['public']) if form.get('public') else ''
        private = int(form['private']) if form.get('private') else ''
        modulus = int(form['modulus']) if form.get('modulus') else ''
        message = form['message'] if form.get('message') else ''
        encrypted = form['encrypted'] if form.get('encrypted') else ''
        encrypted_message = form['encrypted_message'] if form.get('encrypted_message') else ''
        decrypted_message = form['decrypted_message'] if form.get('decrypted_message') else ''
        bit_length = int(form['bit_length']) if form.get('bit_length') else bit_length

        post_type = form.get('type')

        if post_type == 'keys':
            public, private, modulus = generate_keys(bit_length)
    
        if post_type == 'encrypt':
            encrypted_message = encrypt_text(
                message, public, modulus
            )

        if post_type == 'decrypt':
            encrypted = [int(x) for x in encrypted.strip('[]').split(', ')]

            decrypted_message = decrypt_text(
                encrypted, private, modulus
            )

    return await render_template(
        'index.html', encrypted_message=encrypted_message,
        decrypted_message=decrypted_message, public=public,
        private=private, modulus=modulus, bit_length=bit_length,
        message=message, encrypted=encrypted
    )


if __name__ == '__main__':
    app.run(debug=True)
