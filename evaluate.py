#necessary libraries
import difflib
import keras_ocr
import matplotlib.pyplot as plt
import numpy as np
import os

def find_similar_chemicals(chemical_list, word):
    similar_chemicals = []
    for chemical in chemical_list:
        similarity_ratio = difflib.SequenceMatcher(None, chemical, word).ratio()
        if similarity_ratio == 1.0:
            similar_chemicals.append(chemical)
    return similar_chemicals

def search_risky_chemicals(chemical_list_file):
    pipeline = keras_ocr.pipeline.Pipeline()
    image=keras_ocr.tools.read(os.path.join("test-img","test_img.png"))
    prediction_groups = pipeline.recognize([image])
    word_list=[]   #words list
    for i in range(len(prediction_groups[0])):
        word_list.append(prediction_groups[0][i][0])
    risky_chemicals = []
    with open(chemical_list_file, 'r') as file:
        chemical_list = file.read().splitlines()
    for word in word_list:
        similar_chemicals = find_similar_chemicals(chemical_list, word)
        risky_chemicals.extend(similar_chemicals)
    return risky_chemicals