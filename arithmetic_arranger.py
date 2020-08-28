def arithmetic_arranger(problems, options = False):

  if len(problems) > 5:
    return 'Error: Too many problems.'

  line1 = ''
  line2 = ''
  line3 = ''
  line4 = ''

  for i,problem in enumerate(problems):
    #print(problem)
    app = problem.split(" ")
    if app[1] not in ['+', '-']:
      return 'Error: Operator must be \'+\' or \'-\'.'
    if not (app[0].isdigit() and app[2].isdigit()):
      return 'Error: Numbers must only contain digits.'
    
    len1 = len(app[0])
    len2 = len(app[2])
    if len1 > 4 or len2 > 4:
      return 'Error: Numbers cannot be more than four digits.'
    #print (app)
    res = int(app[0]) + int(app[2]) if app[1] == '+' else int(app[0]) - int(app[2])
    spacing = max(len1,len2)
    line1 = line1 + app[0].rjust(spacing+2) + '    '
    line2 = line2 + app[1]+ app[2].rjust(spacing+1) + '    '
    line3 = line3 + ''.rjust(spacing+2,'-') + '    '
    line4 = line4 + str(res).rjust(spacing+2) + '    '
   
  line1 = line1.rstrip()
  line2 = line2.rstrip()
  line3 = line3.rstrip()
  line4 = line4.rstrip() 
  
  if options:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3 + '\n' + line4
  else:
    arranged_problems = line1 + '\n' + line2 + '\n' + line3
  return arranged_problems
