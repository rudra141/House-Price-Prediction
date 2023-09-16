from flask import Flask

app = Flask(__name__)

@app.route('/age')
def hello_world():
    return '200'

def test_name():
    response = app.app.test_client().get('/age')
    assert response.status_code == 200
    assert response.data == b'RR'

@app.route('/name')
def name():
    return 'RUDRA'



if __name__ == '__main__':
    app.run()
