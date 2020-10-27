import matplotlib.pyplot as plt
import matplotlib.path as mpath
from matplotlib.patches import Rectangle
import numpy as np
import plot_the_nn as ptn

#------------------------------ Weights and Biases ------------------------------#
# bias will be -0.3 for all neurons
b = -0.1

weights_2 = [np.random.randint(2,9)/10 for _ in range(12)]


def new_weights():
    global weights_2
    print("Previous weights were: {}".format(weights_2))
# random weights between 0.2 and 0.9
    weights_2 = [np.random.randint(2,9)/10 for _ in range(12)]
    ini()

#------------------------------ Ini --------------------------------------------------#
#------------------------------ Controlling Input ---------------------------------#
# get_input is to limit user input to only four options:  /  \  -  |
# however, l  &  _  have been added "just in case"
ok_list = ["\\", "/", "|", "l", "-", "_"]
def ini():
    global symbol
    global x_input
    symbol = str(input("Please choose a symbol:\n|  or  -  or  /  or  \ \n"))
    while symbol not in ok_list:
        symbol = str(input("Please choose a symbol:\n|  or  -  or  /  or  \ \n"))
    if symbol == "\\":
        x_input = [1, 0, 0, 1]
        nn_layer_input(x_input)
    elif symbol == "/":
        x_input = [0, 1, 1, 0]
        nn_layer_input(x_input)
    elif symbol == "-":
        x_input = [1, 1, 0, 0]
        nn_layer_input(x_input)
    elif symbol == "_":
        x_input = [0, 0, 1, 1]
        nn_layer_input(x_input)
    elif symbol == "|":
        x_input = [1, 0, 1, 0]
        nn_layer_input(x_input)
    elif symbol == "l":
        x_input = [0, 1, 0, 1]
        nn_layer_input(x_input)
    else:
        ini()
#------------------------------ Layers ---------------------------------------------#
# all ReLU's [Rectified Linear Activation Function] have a "round()" function to avoid
# having a lot of decimals
# input layer only receives the pixels from the image, thus it does not need to have weights or biases
def nn_layer_input(x_input):
    n_1 = x_input[ 0 ]
    n_2 = x_input[ 1 ]
    n_3 = x_input[ 2 ]
    n_4 = x_input[ 3 ]
    in_list = [n_1, n_2, n_3, n_4]
    # ReLU 
    global input_neurons
    input_neurons = [round(in_list[n], 2) if in_list[n] > 0 else 0 for n in range(len(in_list))]
    return nn_layer_hidden(input_neurons)

# hidden layer
def nn_layer_hidden(input_neurons):
    # horizontal
    h_1 = weights_2[ 0 ] * input_neurons[ 0 ] + weights_2[ 6 ] * input_neurons[ 1 ] + b
    h_2 = weights_2[ 1 ] * input_neurons[ 2 ] + weights_2[ 7 ] * input_neurons[ 3 ] + b
    # vertical
    h_3 = weights_2[ 2 ] * input_neurons[ 0 ] + weights_2[ 8 ] * input_neurons[ 2 ] + b
    h_4 = weights_2[ 3 ] * input_neurons[ 1 ] + weights_2[ 9 ] * input_neurons[ 3 ] + b
    # diagonals
    h_5 = weights_2[ 4 ] * input_neurons[ 1 ] + weights_2[ 10 ] * input_neurons[ 2 ] + b
    h_6 = weights_2[ 5 ] * input_neurons[ 0 ] + weights_2[ 11 ] * input_neurons[ 3 ] + b
    # put results together in a list
    hn_list = [h_1, h_2, h_3, h_4, h_5, h_6]
    # "ReLU"
    global hidden_neurons
    hidden_neurons = [round(hn_list[h], 2) if hn_list[h] > 0 else 0 for h in range(len(hn_list))]
    return nn_layer_out(hidden_neurons)

# output layer
def nn_layer_out(hidden_neurons):
    o_1 = hidden_neurons[ 0 ] + hidden_neurons[ 1 ] + b
    o_2 = hidden_neurons[ 2 ] + hidden_neurons[ 3 ] + b
    o_3 = hidden_neurons[ 4 ] + b
    o_4 = hidden_neurons[ 5 ] + b
    # put results together in a list
    on_list = [o_1, o_2, o_3, o_4]
    norm_list = [i/sum(on_list) for i in on_list]
    # "ReLU"
    global output
    output = [round(norm_list[o]*100, 0) if norm_list[o] > 0 else 0 for o in range(len(norm_list))]
    return out(output)

#------------------------------ Output --------------------------------------------#
# print output as a list
def out(output):
    ptn.plot_the_nn(x_input, weights_2, input_neurons, hidden_neurons, output)
    new = str(input("Was it correct?\nPlease type: y / n / out\n"))
    if new == "y" or new == "Y":
        print("Let's try another line!")
        ini()
    elif new == "n" or new == "N":
        print("Thank you! Updating weights...")
        new_weights()
    else:
        print("It was fun, bye!")
# call main function
ini()
