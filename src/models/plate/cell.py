from solid import *
from .switch_slot import switch_slot
from solid.utils import *
from ...utils.utils import merge


def stabilizers(multiplier):
  if multiplier < 1.75:
    return None
  elif multiplier < 2.5:
    return union()(
      translate([-110, -8, 0])(cube([32, 140, 50], center=True)),
      translate([110, -8, 0])(cube([32, 140, 50], center=True)),
    )
  elif multiplier < 3.25:
    return union()(
      translate([-140, -8, 0])(cube([32, 140, 50], center=True)),
      translate([140, -8, 0])(cube([32, 140, 50], center=True)),
    )
  else:
    raise Exception('Not supported')

def cell(width, depth, height, multiplier):
  return difference()(
    cube([width, depth, height], center=True),
    merge([
      switch_slot(),
      stabilizers(multiplier)
    ])
  )

def calculate_cell_width(multiplier, base_key_size, key_gap):
  gaps = multiplier / 1 + (1 if (multiplier % 1) > .5 else 0)
  return base_key_size * multiplier + key_gap * gaps