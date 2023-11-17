# import csv

# def convert_csv_to_txt(csv_file_path, txt_file_path):
#     with open(csv_file_path, 'r') as csv_file:
#         csv_reader = csv.reader(csv_file)
        
#         with open(txt_file_path, 'w') as txt_file:
#             for row in csv_reader:
#                 # Assuming the first column is for questions and the second is for answers
#                 question = row[0]
#                 answer = row[1]
                
#                 # Write the question and answer to the TXT file in a format suitable for a chatbot
#                 txt_file.write(f"Question: {question}\nAnswer: {answer}\n\n")

# # Example usage:
# csv_file_path = './Final_IC.csv'
# txt_file_path = 'output.txt'

# convert_csv_to_txt(csv_file_path, txt_file_path)


import csv
import json

# Read CSV file
csv_file_path = './Final_IC.csv'
json_file_path = 'output-1.json'

data = []

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        article_id, article_desc = row
        tag = article_id.split(" of Indian Constitution")[0].strip()
        data.append({"tag": tag, "patterns": [article_id], "responses": [article_desc]})

# Write to JSON file
with open(json_file_path, 'w') as json_file:
    json.dump({"intents": data}, json_file, indent=4)

print(f'Conversion completed. JSON file saved at: {json_file_path}')
