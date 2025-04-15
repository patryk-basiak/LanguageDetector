import os

from Perceptron import Perceptron

perceptrons = [Perceptron(0.01, 26, x) for x in os.listdir('pliki do train i test/pliki do train i test/Train')]
def count_chars(string):
    if len(string) == 0:
        return [0]
    letters = [0 for _ in range(26)]
    suma = 0
    for char in string:
        if not char.isalpha() or not char.isascii():
            continue
        letters[ord(char.lower()) - ord('a')] += 1
    for char in letters:
        suma += char
    return [lab / suma for lab in letters]

def read_file(dir_path, file):
    letters = [0 for _ in range(26)]
    with open(dir_path + "/" + str(file), encoding="utf8") as f:
        suma = 0
        for line in f:
            for char in line:
                if char.isalpha() and char.isascii():
                    letters[ord(char.lower()) - ord('a')] += 1
        for char in letters:
            suma += char
    return [lab / suma for lab in letters]

def learning_process_0(training_data):
    for p in perceptrons:
        learn_0(training_data, p)

def learning_process(training_data):
    learn(training_data, perceptrons)

def read_files(path_name):
    l = []
    for (dir_path, dir_names, file_names) in os.walk(path_name):
        if len(file_names) == 0:
            continue
        for file in file_names:
            if not os.path.isdir(os.path.join(dir_path, file)):
                l.append([read_file(dir_path, file), dir_path.split("\\")[-1]])
    return l
def read_test_data(path_name):
    l = []
    for (dir_path, dir_names, file_names) in os.walk(path_name):
        if len(file_names) == 0:
            continue
        for file in file_names:
            if not os.path.isdir(os.path.join(dir_path, file)):
                l.append([read_file(dir_path, file), file])
    return l

def learn_0(test_list, perceptron):
    index = 0
    while checked_answer_0(test_list, perceptron) != len(test_list):
        index += 1
        for l in test_list:
            computed = perceptron.compute_0(l[0])
            decision = l[1] == perceptron.language
            perceptron.learn_0(l[0], decision, computed)

def checked_answer_0(check_list, p):
    count_true = 0
    for x in check_list:
        correct_label = x[1] == p.language
        if p.compute_0(x[0]) == correct_label:
            count_true += 1
    return count_true

def analyze(text, **kwargs):
    if kwargs.get('data_form') == "String":
        text = count_chars(text)
    outputs = []
    for perc in perceptrons:
        outputs.append([perc.language.split("\\")[-1], perc.compute(text)])
    return max(outputs, key= lambda pe: pe[1])

def analyze_0(text, **kwargs):
    if kwargs.get('data_form') == "String":
        text = count_chars(text)
    outputs = []
    for perc in perceptrons:
        outputs.append([perc.language.split("\\")[-1], perc.compute_0(text)])
    return max(outputs, key= lambda pe: pe[1])

def learn(training_data, perceptron):
    for p in perceptron:
        epoque = 0
        while True:
            to_break = 0
            for inputs, language in training_data:
                if language != p.language:
                    continue
                decision = 1 if language == p.language else -1
                e = 0.5 * (decision - p.compute(inputs)) ** 2
                p.learn(inputs, e)
                epoque += 1
                if e < 0.00001:
                    to_break = 1
                    break
            if to_break:
                break

def new_perceptrons():
    global perceptrons
    perceptrons = [Perceptron(0.001, 26, x) for x in os.listdir('pliki do train i test/pliki do train i test/Train')]