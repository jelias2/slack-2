#!flask/bin/python
from flask import Flask, jsonify, make_response, abort, request
import requests, json

app = Flask(__name__)


tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/', methods=['GET'])
def hello_world():
    return jsonify({'Text':"Hello World"})



@app.route('/todo/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json:
        abort(400)
    if not 'username' in request.json:
        abort(400)
    #Form a new task from posted JSON
    task = {
        #Gets the last ID in task list, and adds one to index
        'id': tasks[-1]['id'] + 1,
        #Gets the title attribute from the posted json
        'username': request.json['username'],
        #Get the source control version
        'scm': request.json['scm'],
        #Get the name of the new repo from json
        'name': request.json['repo-name'],
        #Get the name of the project that repo will be create in
        'project': request.json['project'],
        #Get the description from the posted json
        #'description': request.json.get('description', ""),
        'website': request.json['website']
        #'done': False
        }
    #tasks.append(task)

    #Get the Bitbcket Response
    bitbucket_json = send_to_bitbucket( task )
    #Return both task json and bb json to user
    return jsonify({'task': task, 'Bitbucket JSON': bitbucket_json}), 201

def send_to_bitbucket( jason ):
    print('\n' + "Sending Json to Bitbucket" + '\n')
    project = jason['project']
    print('Project Name:' + project )
    url = "https://bitbucket-emea.aws.lmig.com/rest/api/1.0/projects/IN/repos/"
    #Create the API endpoint with proper project
    splice_url = "https://bitbucket-emea.aws.lmig.com/rest/api/1.0/projects/" + project + "/repos/"

    print( "URL        : " + url )
    print("Spliced URL: " + splice_url + '\n')

    #Form Bitbucket payload using json sent by client
    payload = {
            "scm": jason['scm'],
            "name": jason['name'],
            "has_wiki":"",
            "website": jason['website']
            }

    json_payload = json.dumps(payload)
    print(json_payload + '\n')


    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic YTAzNDI5NDI6MnUmdzQleERt",
        'Cache-Control': "no-cache",
        'Postman-Token': "6e3cb027-b4d1-4bf4-98c0-e6a028b9d90c"
        }

    response = requests.request("POST", url, data=json_payload, headers=headers)
    response_text = response.text
    print(response.text)
    return response_text

@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
