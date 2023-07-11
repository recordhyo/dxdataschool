import matplotlib.pyplot as plt
fig = plt.figure(figsize=(5,5)) #그래프 사이즈 (inch)
plt.boxplot(([100,87,29,76,88],[20,30,20,100,20]))
plt.grid()
plt.show()
fig.savefig("graph.png")