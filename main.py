class Car:
	def __init__(self, brand, model, color):
		self.brand = brand
		self.model = model
		self.color = color
		print ("Auto nuevo creado")

	def set_brand(self,brand):
		self.brand = brand
		print ("La nueva marca es " + self.brand)
	
	def get_brand(self):
		print ("La marca actual es " + self.brand)

def main():
	auto = Car("bmw","z3","black")
	auto.set_brand("Audi")
	auto.get_brand()


if __name__ == "__main__":
	main()