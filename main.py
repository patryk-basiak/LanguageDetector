import os
import random

from Perceptron import Perceptron
from GUI import Gui
from Service import read_files, analyze, learning_process

training_data = read_files('pliki do train i test/pliki do train i test/Train')
test_data = read_files("pliki do train i test/pliki do train i test/Test")

correct_answers = ['Angielski', 'Niemiecki', 'Francuski', 'Angielski', 'Polski', 'Czeski', 'Francuski', 'Wloski', 'Polski']
random.shuffle(training_data)
learning_process(training_data)
print("====")
correct = 0
for x in range(len(test_data)):
    print("Test no.", x+1)
    testing = analyze(test_data[x][0])
    print("Result " + testing[0])
    b = testing[0] == correct_answers[x]
    print("Correct =", b)
    if b:
        correct += 1
    print("===")
print(f"Test done with accuracy: {correct/ len(correct_answers)*100} ")
print(f"Test done with accuracy: {correct}/{len(correct_answers)} ")

g = Gui()







