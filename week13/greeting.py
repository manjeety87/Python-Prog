class Greeting:
   def __init__(self, name):
      self.name = name

   def say_hello(self):
      print(f"Hello, {self.name}!")

# Instantiate the class
greet = Greeting("Sheridan")
greet.say_hello()