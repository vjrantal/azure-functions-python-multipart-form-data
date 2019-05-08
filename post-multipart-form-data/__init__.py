import logging
import os

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request')
    if req.method == 'GET':
        index_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'index.html')
        with open(index_path, 'r') as index:
            return func.HttpResponse(body=index.read(), mimetype='text/html')
    if req.method == 'POST':
        try:
            file = req.files['name_attribute_value_in_html']
            return func.HttpResponse('Processed file with filename: %s' % (file.filename))
        except:
            return func.HttpResponse('Something went wrong when processing the file', status_code=400)
    return func.HttpResponse('Unsupported operation', status_code=400)
