'''
Takes a few seconds to boot up due to the fact that it has to retrieve the MLP classification model
'''

from flask import Flask, render_template
from flask_cors import CORS, cross_origin
from flask import request

import json

from documents import Documents

application = Flask(__name__)
cors = CORS(application)
application.config["CORS_HEADERS"] = "Content-Type"

document_util = Documents()


@application.route("/search", methods=["GET"])
@cross_origin()
def search():
    """search query returns json respresting the documents or an error if unsuccessful"""

    parameters = request.args

    if len(parameters) > 1:
        """too many parameters passed in"""
        return "Too many parameters", 400
    elif len(parameters) == 1 and request.args.get("query") is None:
        """name of parameter not query"""
        return "Bad input parameter", 400
    else:
        query = request.args.get("query")
        maybe_documents = document_util.get_documents(query)
        if maybe_documents is None:
            """no result"""
            return "No results", 200

        return json.dumps(maybe_documents), 200


if __name__ == "__main__":
    application.run()
