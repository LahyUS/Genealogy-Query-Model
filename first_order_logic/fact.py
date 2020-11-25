class Fact:

   def __init__(self, predicate='', args=[], negated = False):
      self.predicate = predicate    # relation or function
      self.args = args              # variables or constants
      self.negated = negated        # not

# This method returns the string representation of the object.
# This method is called when print() or str() function is invoked on an object.
   def __repr__(self):
      str_obj = '{}({})'.format(self.predicate, ', '.join(self.args))
      return str_obj

   def __lt__(self, other):
      if self.predicate != other.predicate:
         return self.predicate < other.predicate
      if self.negated != other.negated:
         return self.negated < other.negated
      return self.args < other.args

   def __eq__(self, other):     # compares two instances by their predicate and negated value
      if self.predicate != other.predicate:
         return False
      if self.negated != other.negated:
         return False
      return self.args == other.args

   def __hash__(self):
      hash_obj = hash(str(self))
      return hash_obj
   
   def copy(self):
      return Fact(self.predicate, self.args.copy(), self.negated)

   def negate(self):
      self.negated = 1 - self.negated

   def get_args(self):
      return self.args

   def get_predicate(self):
      return self.predicate

   @staticmethod
   def parse_fact(fact_str):
      # Example: female(princess_diana).
      fact_str = fact_str.strip()
      fact_str = fact_str.rstrip('.')
      fact_str = fact_str.replace(' ', '')  # format : remove '.' and replace ' ' by ''
      sep_idx = fact_str.index('(')  # get index of separate char ('(')

      # Predicate and arguments are separated by '('
      predicate = fact_str[:sep_idx]  # substring : get predicate , get from index 0 to sep_index
      args = fact_str[sep_idx + 1 : -1].split(',') # list of argument
      return Fact(predicate, args)
