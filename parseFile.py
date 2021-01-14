import xml.etree.ElementTree as ET
import base64
from html.parser import HTMLParser
import logging

class ParseLGmmFile:
  def __init__(self, dirName):
    self.dirName = dirName
    self.pathSaveItemInfo = dirName + '/SaveItemInfo.ini'
    self.pathSaveMemoItem = dirName + '/SaveMemoItem.xml'
    self.result = 0

  # SaveItemInfo 처리
  def parseSaveItemInfo(self):
    return None
  
  # SaveMemoItem 처리
  def parseSaveMemoItem(self):
    logging.debug(self.pathSaveMemoItem)
    try:
      # sample xml
      # <Title Encoding="base64"><![CDATA[]]></Title>
      # <Data Encoding="base64"><![CDATA[...]]></Data>
        # html <note><text></text></note>
      # <ModifiedTime>20160914092049</ModifiedTime>
      doc = ET.parse(self.pathSaveMemoItem)
      root = doc.getroot()

      # index
      idx = root.find("Id").text
      # data
      htmlContent = base64.b64decode(root.find("Data").text).decode('utf-8')
      data = htmlContent.split('<text>')[1].split('</text>')[0].strip()
      # modified time
      mtime = root.find("ModifiedTime").text
    except Exception as e:
      logging.error(e)
      raise e

    logging.debug("idx=%s,data=%s,mtime=%s" % (idx,data,mtime))
    return (idx,data,mtime)
  
  # XML 파싱 - 입력 자료 구성
  def parse(self):
    #self.parseSaveItemInfo()
    memoItem = self.parseSaveMemoItem()
    return memoItem