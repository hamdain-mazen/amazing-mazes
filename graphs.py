
import matplotlib.pyplot as plt



"""
# line 1 points
size_maze = [10, 100, 150, 175, 200, 250, 300, 350, 400, 450, 500]
time_needed = [3.4, 3.78, 3.86, 3.96, 3.99, 3.96, 4.5, 4.56, 4.9, 5.35, 5.78]
# plotting the line 1 points 
plt.plot(size_maze, time_needed, label = "line 1")
  
# line 2 points
size_class= [10, 100, 150, 175, 200, 250, 300, 350, 400, 450, 500]
time_class= [0.0, 0.47, 2.98, 4.86, 9.97, 17.18, 35.72, 66.87, 96.08, 194.14, 312.67]
# plotting the line 2 points 
plt.plot(size_class, time_class, label = "line 2")
  
# naming the x axis
plt.xlabel('size of a maze')
# naming the y axis
plt.ylabel('time nedded')
# giving a title to my graph
plt.title('Time needed to generate mazes in seconds!')
  
# show a legend on the plot
plt.legend()
  
# function to show the plot
plt.show()
"""


size_class= [10, 100, 150, 175, 200, 250, 300, 350, 400, 450, 500]
time_class= [0.0, 0.47, 2.98, 4.86, 9.97, 17.18, 35.72, 66.87, 96.08, 194.14, 312.67]



# 2nd line

# plotting the points 
plt.plot(size_class, time_class)
  
# naming the x axis
plt.xlabel('size of a maze')
# naming the y axis
plt.ylabel('time needed to generate the maze')
  
# giving a title to my graph
plt.title('Time needed to generate mazes in seconds!')
  
# function to show the plot
plt.show()

