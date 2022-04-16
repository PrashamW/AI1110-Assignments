import matplotlib.pyplot as plt

a = [0,5]
b = [12,0]
r = [12,5]
origin = [0,0]
fig, ax = plt.subplots()
plt.grid()
ax.set_xlim(-1,13) 
ax.set_ylim(-1,6) 

ax.quiver(b[0],b[1], a[0],a[1], angles='xy', scale_units='xy', scale=1, color = 'b')
ax.quiver(origin[0],origin[1], a[0],a[1], angles='xy', scale_units='xy', scale=1, color = 'b')
ax.quiver(origin[0],origin[1], b[0],b[1], angles='xy', scale_units='xy', scale=1, color = 'g')
ax.quiver(origin[0],origin[1], r[0],r[1], angles='xy', scale_units='xy', scale=1, color = 'r')

plt.savefig('./vector_diagram.png')
plt.show()