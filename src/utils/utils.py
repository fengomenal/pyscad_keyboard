from solid import *
from solid.utils import *

def merge(objects):
  return union()(
    *filter(lambda x: x, objects)
  )