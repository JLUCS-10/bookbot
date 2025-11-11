book1 = "frankenstein.txt"

def get_num_words(book_text):
    list = book_text.split()
    num_words = len(list)
    return num_words

def get_characters(book_text):
    count = {}
    convert_to_lc = book_text.lower()
    for i in convert_to_lc:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count

def build_sorted_char_list(dictionary):
    sorted_list = []
    for char,num in dictionary.items():
        sorted_list.append({"char": char, "num": num})

    def sort_on(item):
        return item["num"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

    
    

        
