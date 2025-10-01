import pandas as pd
import os

# Change the working directory to the directory of the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Load the knowledge map
knowledge_map = pd.read_csv('symptoms_map.csv')

# Function to suggest diagnosis based on symptoms in the sentence
def suggest_diagnosis(sentence, knowledge_map):
    for _, row in knowledge_map.iterrows():
        symptom1 = row['Symptom1'].lower()
        symptom2 = row['Symptom2'].lower()
        if symptom1 in sentence.lower() or symptom2 in sentence.lower():
            return row['DiseaseAssociated']
    return "Diagnosis not found"

def main():
    # Read the sentences from the .txt file
    with open('sentences.txt', 'r', encoding='utf-8') as file:
        sentences = file.readlines()

    # Process each sentence
    for i, sentence in enumerate(sentences, 1):
        sentence = sentence.strip()
        diagnosis = suggest_diagnosis(sentence, knowledge_map)
        print(f"Patient {i}: {sentence}")
        print(f"Suggested diagnosis: {diagnosis}\n")

if __name__ == "__main__":
    main()
