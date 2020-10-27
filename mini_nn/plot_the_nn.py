import matplotlib.pyplot as plt
import matplotlib.path as mpath
from matplotlib.patches import Rectangle
import numpy as np

def plot_the_nn(x_input, weights_2, input_neurons, hidden_neurons, output):
    sep_y = 5
    sep_x = sep_y
    l0 = 2
    l1 = l0+20
    l2 = (l1/sep_x+5)*sep_x
    l3 = (l2/sep_x+4)*sep_x
    pos_pos = ["backard slash", "forward slash", "vertical", "horizontal"]
    # separation in x axis
    pos = [ [l1 for _ in range(4)], [l2 for _ in range(6)], [l3 for _ in range(4)] ]
    # y positions of input layer
    in_n = [i*sep_y for i in range(2,6)]
    # y positions of hidden layer
    hi_n = [i*sep_y for i in range(1,7)]
    # y positions of output layer
    ou_n = in_n
    vv = 2 # to easily adjust max width
    # max lenght is position of output layer plus the separtion between layers.
    # max height is last element of hidden neurons plus the separtion between layers.
    plt.figure(figsize=(13, 8), frameon=False)
    plt.axis([0, l3+3*sep_y, 0, hi_n[-1]+sep_y])

    # stuff to get ratio betweeb x & y:
    #print("x: ",hi_n[-1]+sep_y,"\ny: ",l3+sep_y,"\nratio: ",(hi_n[-1]+sep_y)/(l3+sep_y))

    # fake stuff------------------------------------------------------------------------------------------------------------------------------------#
    # weights specify line width. This section is commented, but not removed to allow running this file as standalone.
    #weights_1 = [np.random.randint(2,9)/10 for _ in range(4)]
    #weights_2 = [np.random.randint(2,9)/10 for _ in range(12)]
    #input
    #x_input = [1, 0,  0,1]
    # input layer
    #input_neurons = [np.random.randint(2,9)/10 for _ in range(4)]
    # hidden layer
    #hidden_neurons = [np.random.randint(2,9)/10 for _ in range(6)]
    # output
    #output = [np.random.randint(2,9)/10 for _ in range(4)]
    # fake stuff------------------------------------------------------------------------------------------------------------------------------------#

    # plots the input just to visualize it
    # input figure to input layer
    X, Y = 10, (hi_n[-1]+sep_y)/2
    a = 3
    currentAxis = plt.gca()
    #
    x_axis = currentAxis.axes.get_xaxis()
    x_axis.set_visible(False)
    y_axis = currentAxis.axes.get_yaxis()
    y_axis.set_visible(False)
    #
    # white background
    currentAxis.add_patch(Rectangle((X -a , Y -a), 2*a, 2*a, fc = "white",))
    # first pixel
    currentAxis.add_patch(Rectangle((X -a , Y ), a, a, fill=x_input[0]))
    # second pixel
    currentAxis.add_patch(Rectangle((X, Y ), a, a, fill=x_input[1]))
    # third pixel
    currentAxis.add_patch(Rectangle((X -a , Y -a ), a, a, fill=x_input[2]))
    # fourth pixel  
    currentAxis.add_patch(Rectangle((X, Y -a), a, a, fill=x_input[3]))

    # plots lines between layers (has to go before neurons so that the circles can partially hide the lines)
    # input figure to input layer
    #x1, x2, y1, y2
    plt.plot([X-a/2,pos[0][0]],[Y+a,in_n[3]], 'blue', linewidth=vv)
    plt.plot([X+a,pos[0][0]],[Y+a/2,in_n[2]], 'blue', linewidth=vv)
    plt.plot([X-a,pos[0][0]],[Y-a,in_n[1]], 'blue', linewidth=vv)
    plt.plot([X+a,pos[0][0]],[Y-a/2,in_n[0]], 'blue', linewidth=vv)
    # input-to-hidden
    # n_4
    plt.plot([pos[0][0], pos[1][0]], [in_n[0], hi_n[0]], 'green', linewidth=weights_2[11]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[0], hi_n[2]], 'green', linewidth=weights_2[9]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[0], hi_n[4]], 'green', linewidth=weights_2[7]*vv)
    # n_3
    plt.plot([pos[0][0], pos[1][0]], [in_n[1], hi_n[1]], 'blue', linewidth=weights_2[10]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[1], hi_n[3]], 'blue', linewidth=weights_2[8]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[1], hi_n[4]], 'blue', linewidth=weights_2[1]*vv)
    # n_2
    plt.plot([pos[0][0], pos[1][0]], [in_n[2], hi_n[1]], 'red', linewidth=weights_2[4]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[2], hi_n[2]], 'red', linewidth=weights_2[3]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[2], hi_n[5]], 'red', linewidth=weights_2[6]*vv)
    # n_1
    plt.plot([pos[0][0], pos[1][0]], [in_n[3], hi_n[0]], 'purple', linewidth=weights_2[5]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[3], hi_n[3]], 'purple', linewidth=weights_2[2]*vv)
    plt.plot([pos[0][0], pos[1][0]], [in_n[3], hi_n[5]], 'purple', linewidth=weights_2[0]*vv)
    # hidden-to-output
    # weights are set to 2 because the neuron in the output layer adds its inputs
    plt.plot([pos[1][0], pos[2][0]], [hi_n[5], ou_n[3]],'purple', linewidth=2)
    plt.plot([pos[1][0], pos[2][0]], [hi_n[4], ou_n[3]],'purple', linewidth=2)
    plt.plot([pos[1][0], pos[2][0]], [hi_n[3], ou_n[2]], 'red', linewidth=2)
    plt.plot([pos[1][0], pos[2][0]], [hi_n[2], ou_n[2]], 'red', linewidth=2)
    plt.plot([pos[1][0], pos[2][0]], [hi_n[1], ou_n[1]], 'green', linewidth=2)
    plt.plot([pos[1][0], pos[2][0]], [hi_n[0], ou_n[0]], 'blue', linewidth=2)

    # plots the neurons in all layers----------------------------------------------------------------------------------------------------------------#
    circle = mpath.Path.unit_circle()
    mk_size = (hi_n[-1]+sep_y)/(l3+sep_y)*42
    # white circles to hide lines
    plt.plot(pos[0], in_n, 'wo', marker=circle, markersize= mk_size)
    plt.plot(pos[1], hi_n, 'wo', marker=circle, markersize= mk_size)
    plt.plot(pos[2], ou_n, 'wo', marker=circle, markersize= mk_size)
    # transparency to indicate level of activation
    # input layer from topmost neuron to bottom
    input_neurons.reverse()
    hidden_neurons.reverse()
    output.reverse()
    for i in range(4):
        plt.plot(pos[0][0], in_n[i], 'bo', alpha = max(0.1,min(input_neurons[i],1)), marker=circle, markersize= mk_size)
    # hidden layer from topmost neuron to bottom
    for j in range(6):
        plt.plot(pos[1][0], hi_n[j], 'bo', alpha = max(0.1,min(hidden_neurons[j],1)), marker=circle, markersize= mk_size)
    # output layer from topmost neuron to bottom
    for k in range(4):
        plt.plot(pos[2][0], ou_n[k], 'bo', alpha = max(0.1,min(output[k],1)), marker=circle, markersize= mk_size)

    # adding text------------------------------------------------------------------------------------------------------------------------------------#
    # weights between hidden neurons and output neurons
    # h_6 -> o_4
    #               x1       + (     x2        -       x1     )/2      y1    + (     y2     -    y1     )/2          label
    plt.text( pos[1][0] + ( pos[2][0] - pos[1][0] )/2, hi_n[0] + ( ou_n[0] - hi_n[0] )/2,         'w = 1',
    #                           (      y2    -    y1     )/(       x2     -       x1     )              other parameters
             rotation=85*( ou_n[0] - hi_n[0] )/( pos[2][0] - pos[1][0] ),         ha='center', va='top', multialignment='center')
    # h_5 -> o_3
    plt.text( pos[1][0] + ( pos[2][0] - pos[1][0] )/2, hi_n[1] + ( ou_n[1] - hi_n[1] )/2,         'w = 1',
             rotation=85*( ou_n[1] - hi_n[1] )/( pos[2][0] - pos[1][0] ),         ha='center', va='top', multialignment='center')
    # h_4 -> o_2
    plt.text( pos[1][0] + ( pos[2][0] - pos[1][0] )/2, hi_n[2] + ( ou_n[2] - hi_n[2] )/2,         'w = 1',
             rotation=85*( ou_n[2] - hi_n[2] )/( pos[2][0] - pos[1][0] ),         ha='center', va='top', multialignment='center')
    # h_3 -> o_2
    plt.text( pos[1][0] + ( pos[2][0] - pos[1][0] )/2, hi_n[3] + ( ou_n[2] - hi_n[3] )/2,         'w = 1',
             rotation=85*( ou_n[2] - hi_n[3] )/( pos[2][0] - pos[1][0] ),         ha='center', va='top', multialignment='center')
    # h_2 -> o_1
    plt.text( pos[1][0] + ( pos[2][0] - pos[1][0] )/2, hi_n[4] + ( ou_n[3] - hi_n[4] )/2,         'w = 1',
             rotation=85*( ou_n[3] - hi_n[4] )/( pos[2][0] - pos[1][0] ),         ha='center', va='top', multialignment='center')
    # h_1 -> o_1
    plt.text( pos[1][0] + ( pos[2][0] - pos[1][0] )/2, hi_n[5]+0.5 + ( ou_n[3] - hi_n[5] )/2,         'w = 1',
             rotation=85*( ou_n[3] - hi_n[5] )/( pos[2][0] - pos[1][0] ),         ha='center', va='top', multialignment='center')

    # weights between input neurons and hidden neurons
    # connections between input neuron #1 and hidden neurons 1, 4, 6
    # n_1 -> h_1
    plt.text(  pos[1][0] - 5.5, hi_n[0]+5,         f"w= {weights_2[5]}",
             rotation=60*( hi_n[0] - in_n[3] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_1 -> h_4
    plt.text(  pos[1][0] - 5, hi_n[3]+2.5,         f"w= {weights_2[2]}",
             rotation=60*( hi_n[3] - in_n[3] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_1 -> h_6
    plt.text(  pos[1][0] - 5, hi_n[5]+1,         f"w= {weights_2[0]}",
             rotation=60*( hi_n[5] - in_n[3] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # connections between input neuron #2 and hidden neurons 2, 3, 6
    # n_2 -> h_6
    plt.text(  pos[0][0] + 4.5, in_n[2]+4.2,         f"w= {weights_2[6]}",
             rotation=65*( hi_n[5] - in_n[2] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_2 -> h_3
    plt.text(  pos[0][0] + 5.5, in_n[2]+0.8,         f"w= {weights_2[3]}",
             rotation=65*( hi_n[2] - in_n[2] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_2 -> h_2
    plt.text(  pos[0][0] + 4.6, in_n[2]-1,         f"w= {weights_2[4]}",
             rotation=75*( hi_n[1] - in_n[2] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # connections between input neuron #3 and hidden neurons 2, 4, 5
    # n_3 -> h_2
    plt.text(  pos[1][0] - 5, hi_n[1]+2.7,         f"w= {weights_2[10]}",
             rotation=65*( hi_n[1] - in_n[1] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_3 -> h_4
    plt.text(  pos[1][0] - 5, hi_n[3]-0.5,         f"w= {weights_2[8]}",
             rotation=65*( hi_n[3] - in_n[1] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_3 -> h_5
    plt.text(  pos[1][0] - 4.8, hi_n[4]+0.7,         f"w= {weights_2[1]}",
             rotation=65*( hi_n[4] - in_n[1] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # connections between input neuron #4 and hidden neurons 1, 3, 5
    # n_4 -> h_5
    plt.text(  pos[0][0] + 5, in_n[0]+4,         f"w= {weights_2[7]}",
             rotation=65*( hi_n[4] - in_n[0] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_4 -> h_3
    plt.text(  pos[0][0] + 8, in_n[0]+2,         f"w= {weights_2[9]}",
             rotation=70*( hi_n[2] - in_n[0] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # n_4 -> h_1
    plt.text(  pos[0][0] + 5.5, in_n[0]-0.7,         f"w= {weights_2[11]}",
             rotation=70*( hi_n[0] - in_n[0] )/( pos[1][0] - pos[0][0] ),         ha='center', va='top', multialignment='center')
    # result after ReLU for each neuron
    # labels for input neurons
    for i in range(4):
        plt.text(  pos[0][0], in_n[i], f"{input_neurons[i]}", ha='center', va='center', multialignment='center')
    # labels for hidden neurons
    for i in range(6):
        plt.text(  pos[1][0], hi_n[i], f"{hidden_neurons[i]}", ha='center', va='center', multialignment='center')
    # labels for output neurons
    for i in range(4):
        plt.text(  pos[2][0]+5, ou_n[i], f"{output[i]}% chance\n    of being:\n    {pos_pos[i]}", ha='center', va='center', multialignment='center')
    # and input, just to be extra clear on what is "on":1, and what is "off":0
    plt.text(  X-a/2, Y+a/2, f"{x_input[0]}", ha='center', va='center', multialignment='center')
    plt.text(  X+a/2, Y+a/2, f"{x_input[1]}", ha='center', va='center', multialignment='center')
    plt.text(  X-a/2, Y-a/2, f"{x_input[2]}", ha='center', va='center', multialignment='center')
    plt.text(  X+a/2, Y-a/2, f"{x_input[3]}", ha='center', va='center', multialignment='center')

    return plt.show()
