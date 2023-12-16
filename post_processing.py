import re

def capitalize_first_letter(match):
    # Capitalize the first letter of each word
    return ' '.join(word.capitalize() for word in match.split())

def post_processing(filepath, infor):
    # Find ID
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            # Using regular expression to find sequences of digits with length >= 8
            digit_sequences = re.findall(r'\b\d{9,}\b', line)
            
            # Save found sequences to the external variable
            infor.extend(digit_sequences)
    # Find name
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Using regular expression to find "Họ và tên:" and the following line
        matches = re.findall(r'họ và tên:?\s*([^\n\r]+)', content, re.IGNORECASE | re.DOTALL)
        # Remove leading and trailing whitespaces from each match
        infor.extend(match.upper().strip() for match in matches)
    # Find DOB
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
        # Find all date patterns (dd/mm/yyyy or dd-mm-yyyy)
        date_patterns = re.findall(r'\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b', content)
        
        # Append all found date patterns to the list
        infor.extend(date_patterns)
    # Find gender
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()

    # Find all occurrences of "Nam" or "Nữ" after the first date pattern
    gender_matches = re.findall(r'(?<=\b\d{2}/\d{2}/\d{4}\b|\b\d{2}-\d{2}-\d{4}\b)[\s\n]*.*?\b(Nam|Nữ)\b', content)

    if gender_matches:
        # Take the first occurrence as the result
        gender_found = gender_matches[0]
        infor.append(gender_found)

    # Find quoc tich
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Using regular expression to find "quốc tịch:" and the following line
        quoc_tich_matches = re.findall(r'quốc tịch:?\s*([^\n\r]+)', content, re.IGNORECASE | re.DOTALL)
        # Capitalize the first letter of each word and remove leading and trailing whitespaces
        formatted_quoc_tich = ' '.join(capitalize_first_letter(match) for match in quoc_tich_matches)
        infor.append(formatted_quoc_tich)
    # Find quê quán
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Using regular expression to find "quê quán:" and everything until the word 'nơi'
        que_quan_matches = re.findall(r'quê quán:?\s*(.*?)\s*nơi', content, re.IGNORECASE | re.DOTALL)
        formatted_que_quan = que_quan_matches[0].replace('\n', ' ').strip()
        infor.extend([formatted_que_quan])
    # Find nơi thường trú
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        # Using regular expression to find 
        matches = re.findall(r'nơi thường trú:?\s*(.*?)\s*có', content, re.IGNORECASE | re.DOTALL)
        formatted = matches[0].replace('\n', ' ').strip()
        infor.extend([formatted])

# Usage
infor = []
filepath = "C:/Users/vandu/Downloads/output_11.txt"  # Replace with the actual path to your text file
post_processing(filepath, infor)
# Print the found information
print(infor)
