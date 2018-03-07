from app import app
from flask import render_template,redirect,url_for,request,jsonify
import jieba
import operator
import json

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname':'david'}
    posts = [{'author':{'nickname':'john'},'body':'this is one'}
             ,{'author':{'nickname':'jim'},'body':'this is two'}]
    return render_template('index.html',title='my web',user=user,posts=posts)


@app.route("/submit", methods=['POST'])
def handleAnalytic():
    if request.method == 'POST':
        ret = request.form['content']
        seglist = jieba.cut(ret, cut_all=False)
        hash = {}
        with open('stopwords.txt', 'r') as file:
            stopwords = file.readlines()
        stopwords = [stopword.strip('\n') for stopword in stopwords]
        stopwords.append('\n');
        stopwords.append('\r\n');
        stopwords.append(' ');

        for item in seglist:
            if item in stopwords:
                continue
            else:
                if item in hash:
                    hash[item] += 1
                else:
                    hash[item] = 1

        hash = sorted(hash.items(), key=operator.itemgetter(1), reverse=True)
        print(hash)
        json.dump(hash, open('count.json', 'w'))
        #return redirect(url_for('getResults'))
        return jsonify(hash)

@app.route("/jieba", methods=['POST'])
def handleAnalytic2():
    if request.method == 'POST':
        ret = request.form['content']
        seglist = jieba.cut(ret, cut_all=False)
        hash = {}
        with open('stopwords.txt', 'r') as file:
            stopwords = file.readlines()
        stopwords = [stopword.strip('\n') for stopword in stopwords]
        stopwords.append('\n');
        stopwords.append('\r\n');
        stopwords.append(' ');

        for item in seglist:
            if item in stopwords:
                continue
            else:
                if item in hash:
                    hash[item] += 1
                else:
                    hash[item] = 1

        hash = sorted(hash.items(), key=operator.itemgetter(1), reverse=True)
        print(hash)
        json.dump(hash, open('count.json', 'w'))
        #return redirect(url_for('getResults'))
        return jsonify(hash)