class Shape:
 try:
  def aoc(self,r):
    if r>0:
      circle=(3.14*r*r)
      print(circle)
    else:
      print("enter positive value")
 except Exception as error:
      print(error)
 try:
   def aor(self,l,b):

    if l>0 and b>0:
          rectangle=(l*b)
          print(rectangle)
    else:
         print("enter positive value")
 except Exception as error:
      print("no negative value")

obj=Shape()
obj.aoc(-5)
obj.aor(2,3)
 """


"""
class Shape:
  def __init__ (self):
    pass

  def __aoc(self, r):
      try:
            if r > 0:
                circle = (3.14 * r * r)

                print(circle)
            else:
                print("enter positive value")
      except Exception as error:
        print(error)

  def aor(self, l, b):
      try:
            if l > 0 and b > 0:
                rectangle = (l * b)

                print(rectangle)
            else:
                print("enter positive value")

      except Exception as error:
        print("no negative value")

obj = Shape()
obj.__aoc(5)
obj.aor(2, 3)
class Shape1:
  def num(self,r):
    print("num")

"""
class Person:
    def get_gender(self):
        print("male")


class Male(Person):
    def get_gender(self):
        print("male")


class Female(Person):
    def get_gender(self):
        print("female")


Male().get_gender()
Female().get_gender()


class Money:
    def __init__(self, dollars, cent):
        self.dollars = dollars
        self.cent = cent
        dollar_string = '$' + str(self.dollars) + '.' + str(cent)
        self.repr(dollar_string)

    def repr(self, string):
        print "Dollar is :", string

    def add_india(self):
        rupee = self.dollars * 71.87
        paise = self.cent * 7.19
        indian_rupee = rupee + paise
        return str(indian_rupee)

    def add_kuwait_dinar(self):
        dinar = self.dollars * 0.30
        k_paise = self.cent * 0.030
        k_dinar = dinar + k_paise
        return str(k_dinar)

    def add_canadian_dollar(self):
        c_dollar = self.dollars * 1.31
        c_cent = self.cent * 0.13
        canadian_dollar = c_dollar + c_cent
        return str(canadian_dollar)


if __name__ == "__main__":
    dol = raw_input('Enter the dollar and cent value :')
    li = map(int, dol.split('.'))
    obj = Money(li[0], li[1])

    india = obj.add_india()
    print "Indian Rupees is :", india

    kuwait = obj.add_kuwait_dinar()
    print "Kuwaiti Dinar is :", kuwait

    canada = obj.add_canadian_dollar()
    print "Canadian Dollar is :", canada
