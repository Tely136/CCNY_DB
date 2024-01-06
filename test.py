from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

def get_directory_content(directory_path):
    content = {'directories': [], 'files': []}

    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)

        if os.path.isdir(item_path):
            content['directories'].append(item)
        elif os.path.isfile(item_path):
            content['files'].append(item)

    return content

def walk_directory(root_path):
    content = {'root': root_path, 'items': []}

    for root, dirs, files in os.walk(root_path):
        rel_path = os.path.relpath(root, root_path)
        dir_content = get_directory_content(root)

        content['items'].append({
            'path': rel_path,
            'content': dir_content
        })

    return content

@app.route('/')
def index():
    directory_path = 'database/folder1'
    content = walk_directory(directory_path)
    return render_template('index.html', content=content)

@app.route('/files/<path:filepath>')
def serve_file(filepath):
    full_path = os.path.join('database/folder1', filepath)
    return send_from_directory(full_path, os.path.basename(filepath))

if __name__ == '__main__':
    app.run(debug=True)
