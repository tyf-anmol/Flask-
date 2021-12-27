# import main Flask class and request object
from flask import Flask, request, jsonify,render_template
import os
# create the Flask app
app = Flask(__name__)

businessdetails = [
    {
        'businessid':'abc1',
        'client_name':'qwerty',
        'contantno':123456789,
        'address':'BANGALORE'
        },
    {
        'businessid':'abc2',
        'client_name':'uop',
        'contantno':12345678,
        'address':'Delhi'
        },
    {
        'businessid':'abc3',
        'client_name':'asdfgh',
        'contantno':1234567,
        'address':'Mumbai'
        },
    ]

        
@app.route('/home')
def query_example():
    # if key doesn't exist, returns None
    client = request.args.get('client')
    return '''<h1>Hello!{}</h1>'''.format(client)


@app.route('/json', methods=['POST'])
def json_example():
    request_data = request.get_json()

    buisness = None
    banking = None
    Fname = None

    if request_data:
        if 'buisness' in request_data:
            buisness = request_data['buisness']

        if 'banking' in request_data:
            banking = request_data['banking']

        if 'name' in request_data:
            if 'Fname' in request_data['name']:
                Fname_version = request_data['name']['Fname']

    return '''
           The buisness value is: {}
           The banking service is: {}
           The Fname  is: {}'''.format(buisness, banking, Fname)

@app.route('/business')
def get_all():
    return jsonify({'business':businessdetails})

@app.route('/business/businessid')
def get_business():
    businessid = request.args.get('businessid')
    for business in businessdetails:
        if business['businessid'] == businessid:
            return jsonify(business)
    return jsonify({'message':'details not found'})

@app.route('/uploadfile',methods = ['GET','POST'])
def file():
    if request.method=="POST":
        file = request.files["file"]
        file.save(os.path.join("uploads",file.filename))
        return render_template("index.html",message="0:	Successful transaction.")
    return render_template("index.html",message="choose file")
        
    

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
