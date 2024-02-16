from flask import Flask, jsonify, request
from users import  UserManager, initDb


app = Flask(__name__)
usersManager = initDb()



@app.route('/users', methods=['GET', 'POST'])
def manage_users():
    if request.method == 'POST':
        
        #UPDATE Users
        data = request.json
        user_id = data['id']
        name = data['name']
        email = data['email']
        usersManager.insert_user(user_id, name, email)
        return jsonify({"message": "User added successfully"}), 201
       
    return jsonify(usersManager.get_all_users().to_dict(orient='records'))



@app.route('/')
def hello_world():
    return '¡Hola, mundo!'

if __name__ == '__main__':
    app.run(debug=True)