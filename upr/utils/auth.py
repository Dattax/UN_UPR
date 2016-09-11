'''
This is the authentication and authorization module for the United Nations
Universal Periodic Review web app.
'''
import re
import random
import bcrypt
import hmac
from string import letters
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError

__author__ = "Harry Staley <staleyh@craftedtech.net>"
__version__ = "0.01"


# TODO: at some point we need to store the cookie secret on the server in a
# file instead of adding it as text.
COOKIE_SECRET = 'secret'

# REGEX FOR SIGNUP FORM
# email validation regex from http://emailregex.com/ taken from hackernews
EMAIL_RE = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")


class EncryptHandler(object):
    """ handles basic encryption functions """
    def make_salt(self, salt_length=5):
        """
        Creates a salt for salting hashed values """
        return ''.join(random.choice(letters)
                       for x in xrange(salt_length))

    def hash_pass(self, password):
        """
        Takes in the password, hashes it using bcrypt and returns the hash
        """
        hashed_pass = bcrypt.hashpw(password, bcrypt.gensalt(14))
        return hashed_pass

    def valid_pass_hash(self, password, hashed_pass):
        """
        Checks to see if the password is valid by comparing it to a hash
        passed into the function.
        """
        return bcrypt.checkpw(password, hashed_pass)

    def make_secure_val(self, val):
        return '%s|%s' % (val, hmac.new(COOKIE_SECRET, val).hexdigest())

    def get_secure_val(self, secure_val):
        if secure_val:
            val = secure_val.split('|')[0]
        else:
            val = None
        if secure_val == self.make_secure_val(val):
            return val


class AuthHandler(EncryptHandler):
    """ Handles user authentication """
    def user_exists(self, username):
        """ validates that the user exists in the database """
        # TODO: update query to pull from model
        username_exists = db.GqlQuery("SELECT * "
                                      "FROM User "
                                      "WHERE username = :usernm",
                                      usernm=username).get()
        return username_exists

    def user_auth(self, username, password):
        """
        If the username exists it suthenticates the password of the user
        """
        # TODO: update query to pull from model
        user = db.GqlQuery("SELECT * "
                           "FROM User "
                           "WHERE username = :usernm",
                           usernm=username).get()
        if user:
            return self.valid_pass_hash(password,
                                        user.pass_hash)


class OauthHandler(object):
    '''
    Handles oauth functions including facebook and google.
    '''
    def fbconnect():
        """
        Handles authentication and authorization for facebook
        authentication.
        """
        # state token validation
        if request.args.get('state') != login_session['state']:
            response = make_response(json.dumps('Invalid state parameter'
                                                ), 401)
            response.headers['content-type'] = 'application/json'
            return response
        access_token = request.data
        print "access token received: %s" % access_token

        # exchange client token for server token
        app_id = json.loads(open('fb_client_secrets.json', 'r').read())['web'][
            'app_id']
        app_secret = json.loads(open('fb_client_secrets.json', 'r').read())['web'][
            'app_secret']
        url = ('https://graph.facebook.com/oauth/access_token?grant_type='
               'fb_exchange_token&client_id=%s&client_secret=%s&'
               'fb_exchange_token=%s'
               % (app_id, app_secret, access_token))
        http_ = httplib2.Http()
        result = http_.request(url, 'GET')[1]

        # use token to get info from fb api
        # userinfo_url = 'https://graph.facebook.com/v2.4/me'

        # Strip expire tag from access token
        token = result.split('&')[0]
        # The token must be stored in the login_session in order to properly
        # logout, let's strip out the information before the equals sign in
        # our token
        stored_token = token.split("=")[1]
        login_session['access_token'] = stored_token

        url = 'https://graph.facebook.com/v2.4/me?%s&fields=name,id,email' % token
        http_ = httplib2.Http()
        result = http_.request(url, 'GET')[1]
        print "url sent for API access: %s" % url
        print "API JSON result: %s" % result

        data = json.loads(result)

        # populate login session
        login_session['username'] = data['name']
        print login_session['username']
        login_session['email'] = data['email']
        print login_session['email']
        login_session['facebook_id'] = data['id']
        print login_session['facebook_id']
        login_session['provider'] = 'facebook'
        print login_session['provider']
        # get user profile pic
        url = ('https://graph.facebook.com/v2.4/me/picture?%s'
               '&redirect=0&height=200&width=200' % token)
        http_ = httplib2.Http()
        result = http_.request(url, 'GET')[1]
        data = json.loads(result)
        login_session['picture'] = data['data']['url']

        # if the user exists get their user id otherwise create new user
        user_id = get_user_id(login_session['email'])
        if not user_id:
            user_id = create_user(login_session)
        # store the user id in the login session
        login_session['user_id'] = user_id
        # display welcome message for user
        output = ''
        output += '<h1>Welcome, '
        output += login_session['username']
        output += '!</h1>'
        output += '<img src="'
        output += login_session['picture']
        output += ' " style = "width: 300px;'
        output += ' height: 300px;'
        output += 'border-radius: 150px;'
        output += '-webkit-border-radius: 150px;'
        output += '-moz-border-radius: 150px;"> '
        flash("you are now logged in as %s" % login_session['username'])
        print "done!"
        return output

    def fbdisconnect():
        """ Log out of facebook """
        facebook_id = login_session['facebook_id']
        access_token = login_session['access_token']
        url = ('https://graph.facebook.com/%s/'
               'permissions?access_token=%s'
               % (facebook_id, access_token))
        http_ = httplib2.Http()
        result = http_.request(url, 'DELETE')[1]
        return 'You have logged out.'

def gconnect():
    """ handles authentication and authorization for google authentication """
    # state token validation
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter'
                                            ), 401)
        response.headers['content-type'] = 'application/json'
        return response
    code = request.data
    try:
        # try to upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        # exchanges the code for oauth credentials
        credentials = oauth_flow.step2_exchange(code)
    # if a flow exchange error exists dump to json and return error msg
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    http_ = httplib2.Http()
    result = json.loads(http_.request(url, 'GET')[1])
    # If an error exists in the access token info, abort operation.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify current app level access token validity.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    # if stored credentials exist and user ids match respond that user is
    # already logged in
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get google user data json
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)
    data = answer.json()

    # access user data json for display
    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    # if the user exists get their user id otherwise create new user
    user_id = get_user_id(login_session['email'])
    if not user_id:
        user_id = create_user(login_session)
    # store the user id in the login session
    login_session['user_id'] = user_id
    # display welcome message for user
    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px;'
    output += ' height: 300px;'
    output += 'border-radius: 150px;'
    output += '-webkit-border-radius: 150px;'
    output += '-moz-border-radius: 150px;"> '
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

    def gdisconnect():
        """ handles the log out functions of the google acccount """
        # gets and displays the acccess token data in the console
        access_token = login_session['access_token']
        print 'In gdisconnect access token is %s' % access_token
        print 'User name is: ' + login_session['username']
        if access_token is None:
            print 'Access Token is None'
            response = make_response(json.dumps('Current user not connected.'
                                                ), 401)
            response.headers['Content-Type'] = 'application/json'
            return response
        # gets the url to revoke the access token
        url = ('https://accounts.google.com/o/oauth2/revoke?token=%s'
               % login_session['access_token'])
        h = httplib2.Http()
        # gets the result of the url and displays it in the concole
        result = h.request(url, 'GET')[0]
        print result['status']
        # if the result status is confirmed then delete all session
        # data otherwise send error to jsaon
        if result['status'] == '200':
            response = make_response(json.dumps('Successfully disconnected.'), 200)
            response.headers['Content-Type'] = 'application/json'
            return response
        else:
            response = make_response(json.dumps(
                'Failed to revoke token for given user.', 400))
            response.headers['Content-Type'] = 'application/json'
            return response

    def disconnect():
        """ Handles the disconnection of all accounts """
        if 'provider' in login_session:
            if login_session['provider'] == 'google':
                gdisconnect()
                del login_session['gplus_id']
            if login_session['provider'] == 'facebook':
                fbdisconnect()
                del login_session['facebook_id']
            del login_session['access_token']
            del login_session['username']
            del login_session['email']
            del login_session['picture']
            del login_session['user_id']
            del login_session['provider']
            flash('You have been successfully logged out.')
            return redirect(url_for('get_restaurants'))
        else:
            flash('You never logged in.')
            return redirect(url_for('get_restaurants'))
