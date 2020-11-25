from fact import Fact

def is_contain_variable(X):
   Flag = False
   for var in X.args:
      if var[0].isupper():
         Flag = True
         return  Flag
   return Flag

def is_variable(x):  # check if there is variable in argumnt list
   flag = isinstance(x, str) and x[0].isupper()
   return flag

def is_compound(x):
   flag = isinstance(x, Fact)    # check if clause is a fact class or not
   return flag

def is_list(x):
   flag = isinstance(x, list)
   return flag
