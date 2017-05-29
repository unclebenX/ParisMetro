import requests, json
import xml.etree.ElementTree as ET

class RATP:
    url="http://opendata-tr.ratp.fr/wsiv/services/Wsiv?wsdl="
    #headers = {'content-type': 'application/soap+xml'}
    proxies = {
      'http': 'http://kuzh.polytechnique.fr:8080',
      'https': 'http://kuzh.polytechnique.fr:8080',
    }

    def __init__(self):
        return

    def getStations(self, idLine):
        headers = {'content-type': 'text/xml', 'SOAPAction': 'urn:getStations'}
        body = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://wsiv.ratp.fr/xsd" xmlns:wsiv="http://wsiv.ratp.fr"><soapenv:Header/><soapenv:Body><wsiv:getStations><wsiv:station><xsd:line><xsd:id>' + str(idLine) + '</xsd:id></xsd:line></wsiv:station></wsiv:getStations></soapenv:Body></soapenv:Envelope>'
        response = requests.post(self.url,data=body,headers=headers, proxies=self.proxies)
        data = response.content
        xml = ET.fromstring(data)
        stationsElements = xml.findall(".//{http://wsiv.ratp.fr/xsd}stations/{http://wsiv.ratp.fr/xsd}name")
        stations = [e.text.encode("utf-8") for e in stationsElements]
        return stations

    def getStationsByID(self, idStation, idLine):
        headers = {'content-type': 'text/xml', 'SOAPAction': 'urn:getStations'}
        body = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://wsiv.ratp.fr/xsd" xmlns:wsiv="http://wsiv.ratp.fr"><soapenv:Header/><soapenv:Body><wsiv:getStations><wsiv:station><xsd:id>' + str(idStation) + '</xsd:id><xsd:line><xsd:id>' + str(idLine) + '</xsd:id></xsd:line></wsiv:station></wsiv:getStations></soapenv:Body></soapenv:Envelope>'
        response = requests.post(self.url,data=body,headers=headers, proxies=self.proxies)
        data = response.content
        xml = ET.fromstring(data)
        stationsElements = xml.findall(".//{http://wsiv.ratp.fr/xsd}stations/{http://wsiv.ratp.fr/xsd}name")
        stations = [e.text.encode("utf-8") for e in stationsElements]
        return stations

    def getMissionsNext(self, idLine, stationName, directionSens):
        headers = {'content-type': 'text/xml', 'SOAPAction': 'urn:getMissionsNext'}
        body = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://wsiv.ratp.fr/xsd" xmlns:wsiv="http://wsiv.ratp.fr"><soapenv:Header/><soapenv:Body><wsiv:getMissionsNext><wsiv:station><xsd:line><xsd:id>' + idLine + '</xsd:id></xsd:line><xsd:name>' + stationName + '</xsd:name></wsiv:station><wsiv:direction><xsd:sens>' + directionSens + '</xsd:sens></wsiv:direction></wsiv:getMissionsNext></soapenv:Body></soapenv:Envelope>'
        response = requests.post(self.url,data=body,headers=headers, proxies=self.proxies)
        data = response.content
        xml = ET.fromstring(data)
        x = xml.findall(".//{http://wsiv.ratp.fr/xsd}stationsDates")
        nextTrains = [e.text for e in x]
        return nextTrains

    def getMission(self, idLine):
        headers = {'content-type': 'text/xml', 'SOAPAction': 'urn:getMission'}
        body = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsd="http://wsiv.ratp.fr/xsd" xmlns:wsiv="http://wsiv.ratp.fr"><soapenv:Header/><soapenv:Body><wsiv:getMission><wsiv:mission><xsd:id>EPOL</xsd:id><xsd:line><xsd:id>RB</xsd:id></xsd:line></wsiv:mission></wsiv:getMission></soapenv:Body></soapenv:Envelope>'
        response = requests.post(self.url,data=body,headers=headers, proxies=self.proxies)
        data = response.content
        print data

idLine = "RB"
stationName = "Lozere"
directionSens = "A"

R = RATP()
#nextTrains = R.getMissionsNext(idLine, stationName, directionSens)
#print nextTrain

M1Stations = R.getStations("M1")
for station in M1Stations:
    print station, R.getMissionsNext("M1", station, "A")

#R.getMission("M1")
print R.getStationsByID(29, "RB")
