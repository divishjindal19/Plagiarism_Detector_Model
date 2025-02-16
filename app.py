from flask import Flask, render_template, request
import pickle


app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))
tfidf_vectorizer = pickle.load(open('tfidf_vectorizer.pkl','rb'))

@app.route("/")
def indec():
    return render_template('index.html')

@app.route("/detect", methods = ['POST'])
def detect_plagiarism():
    input_text = request.form['text']

    vectorized_text = tfidf_vectorizer.transform([input_text])
    result = model.predict(vectorized_text)
    result = "Plagiarism has been detected" if result[0]==1 else "No plagiarism found"
    return render_template('index.html',result = result)

if __name__ == '__main__':
    app.run(debug=True)