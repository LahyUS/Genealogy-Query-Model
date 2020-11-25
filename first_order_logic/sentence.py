class Sentence:

   @staticmethod
   def classify(line):
      line = line.strip()
      if not line:
         return 'blank'
      if line.startswith('/*') and line.endswith('*/'):
         return 'comment'
      if ':-' in line:
         return 'rule'
      return 'fact'

   @staticmethod
   def read_list(data_list):
      index = 0
      current_line = data_list[index].strip()
      if current_line.startswith('/*'):            # parse comments (returns True if the string starts with the specified value)
         while not current_line.endswith('*/'):    # comments can be at lines
            index += 1                             # we need to ignore all of them
            current_line += data_list[index].strip()
      elif current_line:                           # parse rule/fact
         while not current_line.endswith('.'):     # it can be includes multiple rules/facts in each line
            index += 1                             # we need to get all of them
            current_line += data_list[index].strip()

      return current_line, data_list[index + 1:]   # update and return : remove lines we parsed for the next process
                                                   # str[idx + 1:] means substring the source string from idx + 1 to it's end
