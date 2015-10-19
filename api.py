#!flask/bin/python
import platform
from flask import Flask, jsonify, abort, request, make_response, url_for
from flask.ext.httpauth import HTTPBasicAuth
from flask.ext.cors import CORS 


the_architecture = platform.machine()
the_OS = platform.system()
the_name_of_the_computer = platform.uname()[1]

the_complete_package_info  = {"architecture": the_architecture, "os" : the_OS, "name": the_name_of_the_computer}

auth = HTTPBasicAuth()
app = Flask(__name__)
cors = CORS(app)

@auth.get_password
def get_password(username):
    if username == 'username':
        return 'password'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Forbidden'}), 403)

@app.route('/API/info', methods=['GET'])
#@auth.login_required
def get_tasks():
    return jsonify(the_complete_package_info)

if __name__ == '__main__':
    app.run(debug=True)
