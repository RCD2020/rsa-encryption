var generate_btn = document.getElementById('generate');
var bit_length_field = document.getElementById('bit_length');
var output_field = document.getElementById('output');

generate_btn.addEventListener('submit', function(event) {
    event.preventDefault();

    generate_btn.hidden = true;

    var bit_length = bit_length_field.value;
    var url = '/get_keys';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"bit_length": bit_length})
    })
        .then(response => response.json())
        .then(data => {
            output_field.innerText = data.response;
        })
        .catch(error => {
            console.error('Error:', error);
        });

        generate_btn.hidden = false;
});