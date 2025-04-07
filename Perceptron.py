import random


def normalize_vector(vector):
    distance = sum(x ** 2 for x in vector)**0.5
    if distance == 0:
        return [0 for _ in vector]
    return [x / distance for x in vector]


class Perceptron:
    def __init__(self, alpha, dim, correct_path):
        self.alpha = alpha
        self.correct_path = correct_path
        self.weights = [random.uniform(-0.5, 0.5) for _ in range(dim)]
        self.threshold = 1

    def learn(self, inputs, correct_value):
        inputs = normalize_vector(inputs)
        prediction = self.compute(inputs)
        error = abs(correct_value - prediction)
        if error > 0.01:
            for w in range(len(self.weights)):
                self.weights[w] += float(inputs[w]) * self.alpha * (correct_value - prediction)
        return error

    def compute(self, inputs):
        inputs = normalize_vector(inputs)
        if len(inputs) != len(self.weights):
            raise ValueError("Inputs size is not equal to weights size")
        value = 0
        for x in range(len(inputs)):
            value += float(inputs[x]) * self.weights[x]
        return value

    def compute_0(self, inputs):
        if len(inputs) != len(self.weights):
            raise ValueError("Inputs size is not equal to weights size")
        value = 0
        for x in range(len(inputs)):
            value += float(inputs[x]) * self.weights[x]
        if self.threshold <= value:
            return 1
        else:
            return 0

    def learn_0(self, inputs, correct_value, perceptron_decision):
        for w in range(len(self.weights)):
            self.weights[w] += float(inputs[w]) * self.alpha * (correct_value - perceptron_decision)
        self.threshold += (correct_value - perceptron_decision) * (-1) * self.alpha