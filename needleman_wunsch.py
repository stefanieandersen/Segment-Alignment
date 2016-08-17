debug = False

def matrix_printer(matrix, words):
  print(" " * 13),
  for letter in words['x']:
    print(letter.upper()),
    print("    "),
  print('\n')

  for index,y in enumerate(matrix):
    if index == 0:
      print("     "),
    else:
      print(words['y'][index-1].upper()),
      print("   "),
    for x in y:
      score = x['score'];
      if score >= 0:
      	print(""),
      print(score),
      print("   "),
    print('\n')

    
def score_matrix(words):
  width = len(words['x']) + 1
  height = len(words['y']) + 1
  
  matrix = [[{} for x in range(width)] for y in range(height)]
  
  for y in range(height):
    for x in range(width):
	  
      if x == 0 and y == 0:
        matrix[y][x]['score'] = 0
      else:
        
        if y > 0:
          up = matrix[y-1][x]['score'] - 1
        else:
          up = float('-inf')
        
        if x > 0:
          left = matrix[y][x-1]['score'] - 1
        else:
          left = float('-inf')
          
        if x > 0 and y > 0:
          if words['x'][x-1] == words['y'][y-1]:
            diag = matrix[y-1][x-1]['score'] + 1
          else:
            diag = matrix[y-1][x-1]['score'] - 1
        else:
          diag = float('-inf')
               
        matrix[y][x]['score'] = max(up, left, diag)
        matrix[y][x]['path'] = []
        '''u = u'\u2191'
        l = u'\u2190'
        d = u'\u2196'''
        
        if max(up, left, diag) == up:
          matrix[y][x]['path'].append('u')
        if max(up, left, diag) == left:
          matrix[y][x]['path'].append('l')
        if max(up, left, diag) == diag:
          matrix[y][x]['path'].append('d')
  return(matrix)

def stepping_stone(matrix, y, x, words, level):
  #level is to format the debugging print-out
  if debug:
    tab = ' |' * level  
    print tab, x, y
  
  if y == 0 and x == 0:
    return [{'x': '',
            'y': ''}]

  previous_y = y - 1
  previous_x = x - 1
  
  current_index = matrix[y][x]
  path_check = current_index.get('path')
  previous_diag_index = matrix[previous_y][previous_x]  
  
  aligned_all = [];
  
  if debug:
    print tab, path_check
    
  for path in path_check:
    if debug:
      print tab, path
    if path == 'd':
      aligned = stepping_stone(matrix, previous_y, previous_x, words, level + 1)
      if previous_diag_index['score'] > current_index['score']:
        append_x = words['x'][x-1].lower()
        append_y = words['y'][y-1].lower()
      else:
        append_x = words['x'][x-1].upper()
        append_y = words['y'][y-1].upper()

      for alignment in aligned:
        alignment['y'] += append_y
        alignment['x'] += append_x

    elif path == 'u':
      aligned = stepping_stone(matrix, previous_y, x, words, level + 1)   
      for alignment in aligned:
        alignment['y'] += words['y'][y-1].lower()
        alignment['x'] += "-"

    else:
      aligned = stepping_stone(matrix, y, previous_x, words, level + 1)
      for alignment in aligned:
        alignment['y'] += "-"
        alignment['x'] += words['x'][x-1].lower()

    aligned_all += aligned
    
  if debug:
    print tab, aligned_all
    
  return aligned_all  
          
def aligner(words):
  
  matrix = score_matrix(words)
  
  y = len(words['y'])
  x = len(words['x'])

  if debug:
    matrix_printer(matrix, words)

  aligned = stepping_stone(matrix, y, x, words, 0)    

  print words['x']
  print words['y']

  for alignment in aligned:
    print
    print(alignment['x'])
    print(alignment['y'])
       


aligner({'x': 'gcatgcu',
      	 'y': 'gattaca'})











