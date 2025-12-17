from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__, static_folder='.', static_url_path='')

# Все файлы будут доступны как статические
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

# Явные маршруты для HTML файлов
@app.route('/<filename>.html')
def html_files(filename):
    if filename in ['index', 'customers', 'orders', 'products']:
        return send_from_directory('.', f'{filename}.html')
    abort(404)

# Альтернативные маршруты без .html
@app.route('/customers')
def customers():
    return send_from_directory('.', 'customers.html')

@app.route('/orders')
def orders():
    return send_from_directory('.', 'orders.html')

@app.route('/products')
def products():
    return send_from_directory('.', 'products.html')

# CSS файл
@app.route('/style.css')
def css():
    return send_from_directory('.', 'style.css')

# Любые другие статические файлы
@app.route('/<path:filename>')
def static_files(filename):
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    abort(404)

# Специальный обработчик для корня
@app.route('/index.html')
def index_html():
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)