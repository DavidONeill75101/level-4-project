from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request


import json

from documents import Documents

import pyterrier as pt


if not pt.started():
    pt.init()

print("pyterrier initialised")


application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'

document_util = Documents()


@application.route("/search", methods=["GET"])
@cross_origin()
def search():
    """operator query returns json representing operators or an error if unsuccessful
    optional parameter filterString can be used to pass in id of operator to fetch
    """

    parameters = request.args

    if len(parameters) > 1:
        """too many parameters passed in"""
        return "bad input parameter", 400
    elif len(parameters) == 1 and request.args.get("query") is None:
        """name of parameter not query"""
        return "bad input parameter", 400
    else:
        query = request.args.get("query")
        maybe_documents = document_util.get_documents(query)
        if maybe_documents is None:
            """no result"""
            return "No results", 200

        return json.dumps(maybe_documents), 200


@application.route("/display", methods=["GET"])
@cross_origin()
def display():
    """operator query returns json representing operators or an error if unsuccessful
    optional parameter filterString can be used to pass in id of operator to fetch
    """

    parameters = request.args

    if len(parameters) > 1:
        """too many parameters passed in"""
        return "bad input parameter", 400
    elif len(parameters) == 1 and request.args.get("query") is None:
        """name of parameter not query"""
        return "bad input parameter", 400
    else:
        query = request.args.get("query")
        maybe_documents = document_util.get_documents(query)
        if maybe_documents is None:
            """no result"""
            return "No results", 200

        return render_template('display_docs.html', query=query, documents=maybe_documents[:10]), 200


if __name__ == "__main__":
    application.run()
