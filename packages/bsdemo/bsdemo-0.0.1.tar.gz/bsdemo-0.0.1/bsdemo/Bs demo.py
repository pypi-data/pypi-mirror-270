# 使用 Flask 框架创建一个简单的书籍搜索网站

from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# 连接到 SQLite 数据库
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# 创建书籍表
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        publication_date TEXT,
        isbn TEXT
    )
''')
conn.commit()

# 添加一些示例书籍数据
cursor.execute('INSERT INTO books (title, author, publication_date, isbn) VALUES (?, ?, ?, ?)',
               ('Python入门教程', 'John Doe', '2022-01-01', '1234567890'))
conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    keyword = request.form.get('keyword')
    cursor.execute('SELECT * FROM books WHERE title LIKE ? OR author LIKE ?', ('%' + keyword + '%', '%' + keyword + '%'))
    books = cursor.fetchall()
    return render_template('search_results.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
