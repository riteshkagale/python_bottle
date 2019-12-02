from bottle import route, post, run, template, request
@route('/')
def index():
    return "Done"

@post('/vivotekData')
def vivotek_data():
    fd = open("vivoCameraData.txt","a+")
    bodyData = request.body.read()
    print "BodyData:",bodyData
    fd.write(bodyData)
    fd.write("\n")
    fd.close()
    print "Received data from camera"
    return "Done"
    
run(host='0.0.0.0', port=8080, reload=True)
