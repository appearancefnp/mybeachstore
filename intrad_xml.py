import os
import glob
import requests
import xml.etree.ElementTree as ET

XML_URL = "http://intrad.lv/xml/?get&key=MyBeachStore&pass=rinald2021"


if __name__ == "__main__":
    # get response from intrad server
    response = requests.get(XML_URL)
    # print(xml.content)
    xml = ET.fromstring(response.content)

    print(xml)