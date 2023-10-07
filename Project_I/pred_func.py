import csv
import pickle
import numpy as np

model = pickle.load(open('models/my_final_model.pkl', 'rb'))

print("inside pred_func.py")

def read_csv(filename):
    symptoms = []
    with open('tsymptoms.csv', 'r') as f:
        symptoms_dict = csv.reader(f)
        for columns in symptoms_dict:
            symptoms.append(columns[1])
    return symptoms


symptoms = read_csv('symptoms.csv')
# print(symptoms)

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = value.capitalize()
    symptom_index[symptom] = index


with open('predictor.pkl', 'rb')as f:
    data_dict = pickle.load(f)


def predict_disease(symptoms):
    # symptoms = symptoms.split(",")
    input_data = [0]*len(data_dict["symptom_index"])
    print(data_dict)
    for symptom in symptoms:
        # print(symptom)
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1

    input_data = np.array(input_data).reshape(1, -1)

    rf_prediction = data_dict["predictions_classes"][model.predict(input_data)[
        0]]

    return rf_prediction


# disease = predict_disease(
#     ["Muscle Pain","Back Pain","Mild Fever","Redness Of Eyes","Red Spots Over Body","Nausea"])
# print(f"Predicted disease: {disease}")
