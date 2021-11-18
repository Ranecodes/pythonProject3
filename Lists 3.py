import matplotlib.pyplot as plt
sales = [100, 200, 300, 400, 500]

slice_labels = ["1st Qtr", "2nd Qtr", "3rd Qtr", "4th Qtr", "5th Qtr"]

plt.pie(sales, labels=slice_labels, colors=('r', 'b', 'c', 'm', 'k'))

plt.title("Sales Of The Year")
plt.show()