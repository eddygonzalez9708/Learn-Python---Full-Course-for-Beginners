class Chef:
  def make_chicken(self):
    print("The chef makes a chicken")
  
  def make_salad(self):
    print("The chef makes a salad")

  def make_special_dish(self):
    print("The chef makes bbq ribs")

class ChineseChef(Chef):
  def make_special_dish(self):
    print("The chinese chef makes orange chicken")

  def make_fried_rice(self):
    print("The chinese chef makes fried rice")

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()