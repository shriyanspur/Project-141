from flask import Flask, jsonify, request
import csv


all_articles = []

with open('articles.csv', encoding='utf8') as f:
  reader = csv.reader(f)
  data = list(reader)
  all_articles = data[1:]


liked_articles = []
not_liked_articles = []


app = Flask(__name__)

@app.route('/get-articles')
def get_articles():
  return jsonify({
    'data': all_articles[0],
    'status': 'Success'
  })


@app.route('/liked-articles', methods = ['POST'])
def liked_articles():
  article = all_articles[0]
  liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({
    'status': 'Success'
  }), 201


@app.route('/unliked-articles', methods = ['POST'])
def unliked_articles():
  article = all_articles[0]
  not_liked_articles.append(article)
  all_articles.pop(0)
  return jsonify({
    'status': 'Success'
  }), 201


if (__name__ == '__main__'):
  app.run(debug = True)