import array_stack

def reverse_file(filename):
  """Overwrite given file with its contents line-by-line reversed."""
  S = array_stack.ArrayStack()
  original = open(filename,'r')       
  for line in original:
    S.push(line.rstrip('\n'))     # we will re-insert newlines when writing
  original.close()

  # now we overwrite with contents in LIFO order
  output = open(filename, 'w')    # reopening file overwrites original
  while not S.is_empty():
    output.write(S.pop() + '\n')  # re-insert newline characters
  output.close()
  
reverse_file("deneme.txt")