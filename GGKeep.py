import gkeepapi
import logging

class GkeepApis:
  def __init__(self):
    try:
      self.keep = gkeepapi.Keep()
      #self.keep.login('dakinowebma@gmail.com','bifknylqesbazfuu')
      self.keep.login('huksandolee@gmail.com','whuuuryydboethlf')
    except Exception as e:
      logging.error(e)
      raise e
  
  def createNote(self,content):
    logging.debug(content)
    try:
      note = self.keep.createNote(content['title'],content['data'])
      note.pinned = False
      note.color = gkeepapi.node.ColorValue.White
      label = self.keep.findLabel(u'과거메모')
      note.labels.add(label)
      self.keep.sync()
    except Exception as e:
      logging.error(e)
      raise e

    return None