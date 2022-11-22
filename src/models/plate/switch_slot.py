from solid import *
from solid.utils import *

def switch_slot():
  return union()(
    cube([139, 139, 50], center=True),
    left(42.5)(cube([35, 156.255, 50], center=True)),
    right(42.5)(cube([35, 156.255, 50], center=True)),
  )
