from flask import Flask, render_template
import os
import random

app = Flask(__name__)

@app.route('/')
def gallery():
    image_folder = os.path.join('static', 'images')
    image_files = [file for file in os.listdir(image_folder) if file.endswith(('png', 'jpg', 'jpeg', 'gif'))]
    images = ['images/' + file for file in image_files]
    random.shuffle(images)
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)

