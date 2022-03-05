
# importing the required module
import matplotlib.pyplot as plt
from git import Repo

figure, axis = plt.subplots(3,1,figsize=(10,10))
# x axis values
x = [1,2,3,4]
# corresponding y axis values
y = [20,40,10,4]
y1= [20,50,80,6]
y2 =[50,30,60,9]

axis[0].plot(x, y, color = 'r', marker='o', markerfacecolor='black', markersize=5)
axis[0].set_title("Temperature Data")

axis[1].plot(x, y1, color = 'g', marker='o', markerfacecolor='black', markersize=5)
axis[1].set_title("Pressure Data")

axis[2].plot(x, y2, color = 'b', marker='o', markerfacecolor='black', markersize=5)
axis[2].set_title("Humidity Data")
# function to show the plot
figure.tight_layout()
plt.savefig('chart.png')
# plt.show()

PATH_OF_GIT_REPO = ''  # make sure .git folder is properly configured
COMMIT_MESSAGE = 'comment from python script'

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='master')
        origin.push()
    except Exception as e:
        print(e)    

git_push()
