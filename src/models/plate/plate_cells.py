from .cell import calculate_cell_width

def plate_cells(layout, base_key_size, key_gap):
  row_depth = base_key_size + key_gap
  output = []
  for index, row in enumerate(layout):
    x = 0
    y = -index * row_depth
    cell_row = []
    for col in row:
      width = calculate_cell_width(col, base_key_size, key_gap)
      cell_row.append({ 'width': width, 'depth': row_depth, 'x': x + width / 2.0, 'y': y, 'multiplier': col })
      x += width
    output.append(cell_row)
  return output