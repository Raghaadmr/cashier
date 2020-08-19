def main():
	chosen = []
	item = input ("Item (enter \"done\" when finished):")
	while item !="done":
		price = input("Price:")
		quantity = input("Quantity:")
		chosen.append({"name":item, "price": float(price), "quantity" : int(quantity)})
		item = input ("Item (enter \"done\" when finished):")
	print("-----------------")
	print("receipt")
	print("-----------------")
	for item in chosen:
		print(f"{item['quantity']} - {item['name']} - {item['quantity'] * item['price']}")
	print("-----------------")
	total = 0
	for item in chosen:
		total= total +item['quantity']*item['price']
	print ("total: " + str(total) )
if __name__ == '__main__':
	main()
