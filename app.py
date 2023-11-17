from flask import Flask, render_template, request
import nltk

app = Flask(__name__)

def build_syntax_tree(sentence, custom_grammar):
    tokens = nltk.word_tokenize(sentence)
    tagged_tokens = [(word, tag) for word, tag in input("Enter part-of-speech tags (word/TAG): ").split()]
    cp = nltk.RegexpParser(custom_grammar)
    parsed_tree = cp.parse(tagged_tokens)
    return parsed_tree

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/syntax-tree', methods=['GET', 'POST'])
def syntax_tree():
    if request.method == 'POST':
        user_input = request.form['sentence']
        custom_grammar = request.form['custom_grammar']
        syntax_tree = build_syntax_tree(user_input, custom_grammar)
        return render_template('index.html', syntax_tree=syntax_tree)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
