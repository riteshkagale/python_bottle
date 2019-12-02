import json
from bottle import route, post, run, template, request
@route('/')
def index():
    return "Done"

@post('/vivotekData')
def vivotek_data():
    fd = open("vivoCameraData.txt","a+")
    bodyData = request.body.read()
    #print bodyData
    fd.write(bodyData)
    fd.write("\n")
    data=json.loads(bodyData)
    #print data
    macaddress=data['Source']['MacAddress']
    print macaddress
    modelname=data['Source']['ModelName']
    print modelname
    ipaddress=data['Source']['IPAddress']
    print ipaddress
    jsonData={}
    for val in data['Data']:
        for countInfo in val['CountingInfo']:
            iSide=countInfo['In']
            print iSide
            oSide=countInfo['Out']
            print oSide
            sTime=countInfo['StartTime']
            print sTime
            eTime=countInfo['EndTime']
            print eTime
            jsonData['iSide']=iSide
            jsonData['oSide']=oSide
            jsonData['sTime']=sTime
            jsonData['eTime']=eTime
            
    jsonData['macaddress']=macaddress
    jsonData['modelname']=modelname
    jsonData['ipaddress']=ipaddress
    fd1=open("vivoCameraData.json","a+")
    json.dump(jsonData,fd1)
    fd1.write("\n")
    fd1.close()
    fd.close()
    
    print "Received data from camera"
    return "Done"

run(host='0.0.0.0', port=8080, reload=True)
