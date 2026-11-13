import matplotlib.pyplot as plt

#plt.rcParams["font.family"] = "AppleGothic" #MAC OS  
plt.rcParams["font.family"] = "Malgun Gothic"

weight = [55, 54, 51, 53, 49.5]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(weight)

for i, p in enumerate(weight):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points", xytext=(0, 8), ha="center")

ax.set_title("나의 몸무게 변화")
fig.savefig("my_first_chart.png")