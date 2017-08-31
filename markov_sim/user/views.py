import json
from flask import request, jsonify, Blueprint, abort
from flask.views import MethodView
from markov_sim import firebase, app
 
nabs = Blueprint('nabs', __name__)
 
@nabs.route('/')
@nabs.route('/home')
def home():
    return "Welcome to Nabs."
 
 
class NabsView(MethodView):
 
    def get(self, id=None, page=1):
        if not id:
            res = {'response': 'get with no id'}
        else:
            res = {
                'response': id
            }
        return jsonify(res)
 
nabs_view =  NabsView.as_view('nabs_view')
app.add_url_rule(
    '/nabs/', view_func=nabs_view, methods=['GET', 'POST']
)
app.add_url_rule(
    '/nabs/<string:id>', view_func=nabs_view, methods=['GET']
)