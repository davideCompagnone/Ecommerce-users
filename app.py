from flask import Flask, jsonify, request
from users import  UsersManager, initDb


app = Flask(__name__)
usersManager = initDb()



@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        
        #UPDATE Users
        return jsonify(request.json), 201
    return jsonify(usersManager.get_all_users().to_dict(orient='records'))



@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True, port=5002)