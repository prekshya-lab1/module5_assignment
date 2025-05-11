class NumberProcessor:
  def_init_(self):
  self.numbers = []
def add_number(self, number):
  self.numbers.append(number)
def find_number(self,x):
  try: index = self.numbers.index(x) + 1
    return index
except ValueError:
   return -1
