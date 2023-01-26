import logging
import tator
import cv2
import tempfile
import pytesseract

import numpy as np

logger = logging.getLogger(__name__)

def test_get_clip(host: str,
                 token: str,
                 count_video: int):
  api = tator.get_api(host, token)
  media = api.get_media(count_video, presigned=3600)
  with tempfile.TemporaryDirectory() as td:
    util = tator.util.MediaUtil(td)
    # This load takes a tator object
    util.load_from_media_object(media, quality=None)

    concat_path,_ = util.get_clip([(25, 49)])
    reader = cv2.VideoCapture(concat_path)
    ok,frame = reader.read()
    expected=25
    while ok:
      img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      text = pytesseract.image_to_string(img)
      _,val=text.strip().split('=')
      val = val.replace('/','')
      assert(int(val) == expected)
      expected += 1
      ok,frame = reader.read()

    # Check a non-contiguous video
    concat_path,_ = util.get_clip([(25, 49), (100,149)])
    reader = cv2.VideoCapture(concat_path)
    ok,frame = reader.read()
    expected=[*list(np.linspace(25,49,25).astype(np.int32)),
              *list(np.linspace(100,149,50).astype(np.int32))]
    expected_idx = 0
    while ok:
      img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      text = pytesseract.image_to_string(img)
      _,val=text.strip().split('=')
      val = val.replace('/','')
      assert(int(val) == expected[expected_idx])
      expected_idx += 1
      ok,frame = reader.read()


def test_get_tile_image(host: str,
                        token: str,
                        count_video: int):
  api = tator.get_api(host, token)
  media = api.get_media(count_video, presigned=3600)
  with tempfile.TemporaryDirectory() as td:
    util = tator.util.MediaUtil(td)
    # This load takes a tator object
    util.load_from_media_object(media, quality=None)

    tile=util.get_tile_image([1])
    img = cv2.imread(tile)
    text = pytesseract.image_to_string(img)
    _,val=text.strip().split('=')
    val = val.replace('/','')
    assert(int(val) == 1)

    tile=util.get_tile_image([123,231,100,50])
    img = cv2.imread(tile)
    text = pytesseract.image_to_string(img)
    val=text.strip()
    val = val.replace('/','').split('\n')
    assert(val[0] == "Frame=123 Frame=231")
    assert(val[2] == "Frame=100 Frame=50")



def test_get_animation(host: str,
                       token: str,
                       count_video: int):
  api = tator.get_api(host, token)
  media = api.get_media(count_video, presigned=3600)
  with tempfile.TemporaryDirectory() as td:
    util = tator.util.MediaUtil(td)
    # This load takes a tator object
    util.load_from_media_object(media, quality=None)

    random_frames = [25,39,40,3,100,300,10,44,137] 
    animation_path = util.get_animation(random_frames, 1, render_format='mp4')
    reader = cv2.VideoCapture(animation_path)
    ok,frame = reader.read()
    e_idx = 0
    while ok:
      img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      text = pytesseract.image_to_string(img)
      _,val=text.strip().split('=')
      val = val.replace('/','')
      assert(int(val) == random_frames[e_idx])
      e_idx += 1
      ok,frame = reader.read()