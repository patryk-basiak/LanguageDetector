import os
import random

from Perceptron import Perceptron
from GUI import Gui
from Service import read_files, analyze, learning_process, learning_process_0, perceptrons, new_perceptrons, analyze_0

training_data = read_files('pliki do train i test/pliki do train i test/Train')
test_data = read_files("pliki do train i test/pliki do train i test/Test")
def main():
    learning_process(training_data)
    print("====")
    correct = 0
    for x in range(len(test_data)):
        print("Test no.", x+1)
        testing = analyze(test_data[x][0])
        print("Result " + testing[0])
        b = testing[0] == test_data[x][1].split("_")[0]
        print("Correct =", b)
        if b:
            correct += 1
        print("===")
    print(f"Test done with accuracy: {correct/ len(test_data) *100} ")
    print(f"Correct test: {correct}/{len(test_data) } ")
    #
    g = Gui()

def main_2():
    learning_process_0(training_data)
    print("====")
    correct = 0
    for x in range(len(test_data)):
        print("Test no.", x + 1)
        testing = analyze_0(test_data[x][0])
        print("Result " + testing[0])
        b = testing[0] == test_data[x][1].split("_")[0]
        print("Correct =", b)
        if b:
            correct += 1
        print("===")
    print(f"Test done with accuracy: {correct / len(test_data) * 100} ")
    print(f"Correct test: {correct}/{len(test_data)} ")

if __name__ == "__main__":
    main_2()
    new_perceptrons()
    main()








