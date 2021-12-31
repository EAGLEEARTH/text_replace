import json




new_file_name = "new_file"

def read_json():
    with open("./changes_word.json","r",encoding="utf-8") as f:
        options_data = json.loads(f.read()) 
    return options_data



def read_file():
    print("Working....")
    with open("./text.txt","r", encoding="utf-8") as f:
        text = f.read()
    return text



def write_file(text):
    with open(new_file_name+".txt", "w", encoding="utf-8") as file1:
        # Writing data to a file
        file1.write(text)



def replace_processor():
    replace_word = read_json()
    replace_text = read_file()
    for key,value in replace_word.items():
        if key:
            check_word = key
            if value:
                changed_word = value
                replace_text = replace_text.replace(check_word,changed_word)
            else:
                changed_word = ""
                replace_text = replace_text.replace(check_word,changed_word)

        text = replace_text
        write_file(text)






replace_processor()