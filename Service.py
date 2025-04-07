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
    for p in perceptrons:
        learn(training_data, p)

def read_files(path_name):
    l = []
    for (dir_path, dir_names, file_names) in os.walk(path_name):
        if len(file_names) == 0:
            continue
        for file in file_names:
            if not os.path.isdir(os.path.join(dir_path, file)):
                l.append([read_file(dir_path, file), dir_path.split("\\")[-1]])
    return l

def learn_0(test_list, perceptron):
    index = 0
    while checked_answer_0(test_list, perceptron) != len(test_list):
        index += 1
        for l in test_list:
            computed = perceptron.compute_0(l[0])
            decision = l[1] == perceptron.correct_path
            perceptron.learn_0(l[0], decision, computed)
    print(f"Laps {index}")

def checked_answer_0(check_list, p):
    count_true = 0
    for x in check_list:
        correct_label = x[1] == p.correct_path
        if p.compute_0(x[0]) == correct_label:
            count_true += 1
    return count_true

def checked_answer(check_list, p):
    count_true = 0
    for x in check_list:
        expected = 1 if x[1] == p.correct_path else 0
        predicted = 1 if p.compute(x[0]) >= p.threshold else 0
        if predicted == expected:
            count_true += 1
    return count_true

def analyze(text, **kwargs):
    if kwargs.get('data_form') == "String":
        text = count_chars(text)
    outputs = []
    for perc in perceptrons:
        outputs.append([perc.correct_path.split("\\")[-1], perc.compute(text)])
    return max(outputs, key= lambda pe: pe[1])

def learn(train_list, perceptron):
    index = 0
    while index < 1000:
        index += 1
        total_error = 0.0
        for l in train_list:
            decision = 1 if l[1] == perceptron.correct_path else -1
            error = perceptron.learn(l[0], decision)
            total_error = float(0.5*(decision - perceptron.compute(l[0]))**0.5)
        print(total_error)
        if total_error < 0.01:
            break
    print(f"Laps {index}")