from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation as fa
import numpy as np


time = np.linspace(0, 10, 100)

y = np.sin(time)

fig, axis = plt.subplots()

axis.set_xlim([min(time), max(time)])
axis.set_ylim([-2, 2])

anime_plot, = axis.plot([0], [0], marker="^")

print(f"Animated plot: {anime_plot,}")

def update_func(frame):
    # update previous plot with current one
    anime_plot.set_data(time[:frame], y[:frame])
    
    return anime_plot,

animation = fa(
    fig=fig,
    func=update_func,
    frames=len(time),
    interval=25,
)

plt.show()

# saving the animation
# animation.save("sin wave.gif")