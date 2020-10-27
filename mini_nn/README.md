The scope of this mini project is to visualize the inner workings of a (very) simple neural network [NN].

The most simple NN that comes to mind receives an input image of side 2x2 pixels and can differentiate:
• horizontal line     -  or  _
• vertical line       |  or  l  (lowercap L)
• forward diagonal    /
• backward diagonal   \

The NN architecture is compossed as follows:
• 4 input neurons
    each neuron receives one pixel
• 6 hidden neurons
    detects patterns by adding up results of the input layer
• 4 output neurons
    last layer to add up the results of the hidden layer

For simplicity's sake the input format is a symbol and
for demosntration purposes the output includes an Activation Map.

Input has the                          Example:
following order :                     if input is " - "  or  " _ ", 
                                      that's a horizontal line:
+-----+-----+                         +----+-----+      +----+-----+
|  0  |  1  |                         ||||||||||||      |    |     |
+-----+-----+                         +----+-----+  or  +----+-----+
|  2  |  3  |                         |    |     |      ||||||||||||
+-----+-----+                         +----+-----+      +----+-----+
