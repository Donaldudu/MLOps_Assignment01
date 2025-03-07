from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Deploying Flask App at Vercel now 1122"

if __name__ == '__main__':
    app.run(debug=True)
