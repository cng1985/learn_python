class User:
  def __init__(self,name):
    self.name=name
  def show(self):
    print(self.name)


user =User("ada66")
user.show()
user.age=35
print(user.age)
def showMsg():
  print("hi")
user.show=showMsg
user.show()