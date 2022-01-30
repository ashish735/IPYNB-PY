import numpy as np

def sigmoid(x):   #activation function
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):    #loss derivative function to adjust weights
    return x * (1 -x )

# training_inputs shape (4, 3)
training_inputs = np.array ([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

# training_outputs shape (4, 1)
training_outputs = np.array ([[0,1,1,0]]).T

np.random.seed(1)   #seed gives same random values

# synaptics_weights = array([[-0.45000758],
#                            [ 0.66094852],
#                            [-0.07133576]])
# synaptics_weights shape (3, 1)
synaptics_weights = 2 * np.random.random((3, 1)) - 1

print('Random Starting Synaptic Weights:')
print(synaptics_weights)

for iteration in range(200000):

    input_layer = training_inputs

    # outputs = array([[0.43924997],
    #                    [0.4051455 ],
    #                    [0.6492655 ],
    #                    [0.22372498]])
    # outputs shape (4, 1)
    outputs = sigmoid(np.dot(input_layer, synaptics_weights))  #summation of weights and inputs
                                                                #then activation function
    # error is same as outputs
    error = training_outputs - outputs                   # cost function

    # adjustments is same as outputs
    adjustments = error * sigmoid_derivative(outputs)    #backpropagation

    synaptics_weights += np.dot(input_layer.T, adjustments)   #parameter update

print('Synaptics weights after training')
print(synaptics_weights)

print('Outputs after training:')
print(outputs)