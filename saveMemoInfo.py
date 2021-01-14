import xml.etree.ElementTree as ET
import logging

# SaveMemoInfo 처리
class SaveMemoInfo:
  def __init__(self, fileName):
    self.fileName = fileName
    self.result = 0
  
  # XML 파싱 - 입력 자료 구성
  def parse(self):
    try:
      doc = ET.parse(self.fileName)
    except Exception as e:
      logging.error(e)
      return e

    logging.debug(doc)
    # <Title Encoding="base63"><![CDATA[]]></Title>
    # <Data Encoding="base63"><![CDATA[...]]></Data>
      # html <note><text></text></note>
    # <ModifiedTime>20160914092049</ModifiedTime>