import matplotlib.pyplot as plt


w=int(input("your college hours today?:"))

x=int(input("how much you spent in houseworks?:"))

y=int(input("how much time for additionl skills?:"))

z=int(input("how much self cares hours today?:"))

u=int(input("how much hours you slept last night?:"))

e=int(input("how much hours you exercise today?:"))

def per(x):
    return (x/t)*100

v=(24-(w+x+y+z+u+e))

t=u+v+w+x+z+y

labels = 'leisure time', 'college hours', 'cooking and housework', 'additional learning','selfcare hours',"sleep","exercise"

sizes = [per(v), per(w), per(x), per(y), per(z),per(u),per(e)]

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue','pink','violet','green']

explode = (0.1, 0, 0, 0, 0, 0, 0) 


plt.pie(sizes, explode=explode, labels=labels, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal') 

plt.title("how did you spent your day today")
plt.show()
