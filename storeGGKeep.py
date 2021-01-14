import gkeepapi
import logging

class storeGGKeep:
  def __init__(sefl,(idx,data,mdate)):
    logging.debug("%s,%s,%s" % (idx, data, mdate))
    exit()

    try:
      keep = gkeepapi.Keep()
      keep.login(settings.keep_user, settings.keep_pswd)
      note = keep.createNote('lgPhone', 'hello world')
      note.pinned = True
      note.color = gkeepapi.node.ColorValue.Red
      keep.sync()
    except Exception as e:
      logging.error(e)
      return e