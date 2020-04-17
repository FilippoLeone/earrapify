from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse
import os
import shutil
import uuid 
import json
from tools import boost_track

@view_config(route_name='index', renderer='templates/index.pt')
def index(request):
    return {}

@view_config(route_name='process')
def process_file(request):
    input_file = request.POST['file'].file
    db = request.POST['volume']
    input_file.seek(0)
    filename = '%s.mp3' % uuid.uuid4()
    file_path = os.path.join('/tmp', filename)
    with open(file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)
    print(output_file)
    print(db)
    if boost_track(file_path, filename, db):
        return Response(json_body={'filename': filename})

@view_config(route_name='download')
def download_file(request):
    filename = request.GET['filename']
    file_path = os.path.join('/tmp', filename)
    f = open(file_path, 'rb')
    return Response(body_file=f, charset='UTF-8', content_type='application/download', content_disposition=f'attachment; filename="{filename}"')