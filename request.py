import sys, getpass, requests
from bitbucket.bitbucket import bitbucket
# from flask import Flask
#
# app = Flask(__name__)

def main():

    #API Keys
    token =  "token"
    secret = "MzM1MzgzODcyNjM5OgmxWhNPVo389eF/m9edFkNwICPh"

     bitbucket = OAuth1Service(name='bitbucket',
                              consumer_key=token,
                              consumer_secret=secret,
                              request_token_url=REQUEST_TOKEN_URL,
                              access_token_url=ACCESS_TOKEN_URL,
                              authorize_url=AUTHORIZE_URL)
    headers = { token : secret }

    #Create Repo Api endpoint


    payload = {
                'name': 'newRepo',
                'scm': 'git',
                'is_private': 'true',
                'fork_policy': 'no_public_forks'
               }

    #Get the account username
    username = input("Enter your Bitbucket username: ")
    print ("Hi ",username, '\n')

    url = "https://api.bitbucket.org/2.0/repositories/" +  username
    #Get the users password
    password = getpass.getpass("Enter your Bitbucket Password: ")
    print( password )
    print( payload['name'] )


    r = requests.post(url, data = payload, headers = headers )


if __name__ == '__main__':
    main()
    #app.run(debug=True)
