p = int(input())
if (p == 1):
	print("Top 1")
elif (p == 2 or p == 3):
	print("Top 3")
elif (p == 4 or p == 5):
	print("Top 5")
elif (p >= 6 and p <= 10):
	print("Top 10")
elif (p >= 11 and p <= 25):
	print("Top 25")
elif (p >= 26 and p <= 50):
	print("Top 50")
elif (p >= 50 and p <= 100):
	print("Top 100")