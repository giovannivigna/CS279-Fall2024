import random

from flask import Flask, request, make_response, render_template_string

app = Flask(__name__)

# List of random cat emojis
cat_emojis = ['😺', '😸', '😹', '😻', '😼', '😽', '🙀', '😿', '😾']

style = ''' body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
    }
    h1 {
        text-align: center;
    }'''

flag = '''FLAG{cookie_is_10}'''


@app.route('/')
def check_cookie():
    # Check if 'my_cookie' exists in the request
    cookie_value = request.cookies.get('my_cookie')

    if cookie_value == '10':
        # If cookie value is '10', show the flag page
        flag_page = f'''
        <html>
        <head><title>Flag</title></head>
        <style>
        {style}
        </style>
        <body>
            <h1 style="text-align: center;">🎉 Congratulations! Here is your 🚩: {flag}</h1>
        </body>
        </html>
        '''
        return render_template_string(flag_page)
    else:
        # Otherwise, send a random cat emoji
        random_cat = random.choice(cat_emojis)
        response = make_response(f'''
          <html>
        <head><title>Random Cat</title></head>
        <style>
        {style}
        </style>
        <body>
            <h1>{random_cat} Meow! Your 🍪 is not 10.</h1>
        </body>
        </html>
        ''')

        # Optionally, set a cookie if not already set
        if not cookie_value:
            response.set_cookie('my_cookie', str(random.randint(1, 20)))

        return response


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
