class User:
  def __init__(self,name):
    self.name=name
  def show(self):
    print(self.name)

  @classmethod
  def class_foo(cls):
      print(cls)

  def printMessage(self):
    print("hi")

user =User("ada66")
user.show()
user.age=35
user.class_foo()
print(user.age)
def showMsg():
  print("hi")
user.show=showMsg
user.show()