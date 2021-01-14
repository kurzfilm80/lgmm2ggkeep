import sys
import os
import shutil
import logging

from parseFile import ParseLGmmFile
from GGKeep import GkeepApis

def getTargetDir():
  if len(sys.argv) != 2:
    logging.error("arg cnt=%s" % sys.argv)
    exit()
  return sys.argv[1]

def searchLowerDir(momDir):
  logging.info("momDir=%s"%momDir)
  filenames = os.listdir(momDir)
  try:
    for filename in filenames:
      full_filename = os.path.join(momDir, filename)
      if os.path.isdir(full_filename):
        yield full_filename
  except Exception as e:
    logging.error("fail search; err=%s" % e)
    exit()
  
def main():
  logging.basicConfig(
    filename='lgmm2ggkeep.log', 
    level=logging.INFO,
    #stream=sys.stdout,
    format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s: %(message)s')
  logging.info("start...")

  # 매개변수로 대상 폴더 읽어오기
  targetDir = getTargetDir()
  logging.info("targetDir=%s" % targetDir)

  # 성공 리스트 저장할 디렉토리 확인 및 생성
  succDir = targetDir + '\succDir'
  try :
    if not os.path.isdir(succDir):
      os.makedirs(os.path.join(succDir))
  except Exception as e:
    logging.error(e)
    exit()

  # 폴더 순회
  for lowerDir in searchLowerDir(targetDir):
    logging.info("lowerDir=%s" % lowerDir)
    logging.info("succDir =%s" % succDir)

    # 성공 리스트 백업 디렉토리 SKIP
    if lowerDir == succDir :
      continue

    # 파일 파싱 
    try:
      clsParse = ParseLGmmFile(lowerDir)
      resultParse = clsParse.parse()
    except Exception as e:
      logging.error("fail to parse file; lowerDir=%s,err=%s"%(lowerDir,e))
      continue

    # 입력 데이터 재구성
    logging.debug(resultParse)
    tmpStr = resultParse[2]
    title = u"%s년%s월%s일%s시%s분%s초" % \
      (tmpStr[0:4],tmpStr[4:6],tmpStr[6:8],tmpStr[8:10],tmpStr[10:12],tmpStr[12:14])
    data = resultParse[1].replace('&quot','')
    content = {"title":title,"data":data}

    # google keep 입력
    try :
      clsGKeep = GkeepApis()
      clsGKeep.createNote(content)
      #print(content)
    except Exception as e:
      logging.error("fail to createNote; lowerDir=%s,err=%s"%(lowerDir,e))
      continue

    # 성공 디렉토리 move
    try :
      shutil.move(lowerDir,succDir)
    except Exception as e:
      logging.error("fail to move; lowerDir=%s,err=%s"%(lowerDir,e))
      continue


if __name__ == "__main__" :
  main()
