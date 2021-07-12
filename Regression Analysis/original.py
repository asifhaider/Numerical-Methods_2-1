from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

def print_answer(c0, c1):
    print("Kmax: " + str(1/c0))
    print("Cs: " + str(c1/c0))    
    return 1/c0, c1/c0

def input_data():
    x_val = []
    y_val = []
    target_file = "data.txt"
    file = open(target_file)
    for i in file:
        entry = i.split(" ")
        x_val.append(float(entry[0]))
        y_val.append(float(entry[1]))   
    
    return x_val, y_val

# function for initial plotting
def plot_function(a, b):
        
    x, y = input_data()

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='.', c='blue')

    plt.xlim(-1.0, 5)
    plt.ylim(-1.0, 10)
    
    ax.axhline(y=0, color='grey')
    ax.axvline(x=0, color='grey')
    
    sns.set_theme(style="darkgrid")
    x = np.linspace(0, 5, 100)
    y = (a*(np.array(x)**2))/(b+(np.array(x)**2))
    ax.plot(x, y, 'red')
    plt.show()
