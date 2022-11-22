from solid import *
from solid.utils import *
import yaml
from src.models.plate.plate_cells import plate_cells 
from src.models.plate.cell import cell

with open('./config.yaml', 'r') as file:
  config = yaml.safe_load(file)

keyrows = plate_cells(config['layout'], config['base_key_size'], config['key_gap'])
cells = []
for row in keyrows:
  for col in row:
    c = translate((col['x'], col['y']))(
      cell(col['width'], col['depth'], config['plate_height'], col['multiplier'])
    )
    cells.append(c)

output = union()(*cells)

scad_render_to_file(output, './output.scad', file_header=f'$fn = {30};')
# print(config)
#config = json.load(open('./config.json'))

# keyrows = config['keyRows']





# scad_render_to_file(output, 'test.scad', file_header=f'$fn = {30};')