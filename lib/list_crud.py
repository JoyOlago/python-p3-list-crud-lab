def create_an_empty_list():
    return []

def create_a_list():
    return ["Earth", "Fire", "Wind", "Water"]

def add_element_to_end_of_list(l, element):
    list = ["Earth", "Fire", "Wind", "Water"]
    list.append(5)
    return list

def add_element_to_start_of_list(l, element):
    list = ["Earth", "Fire", "Wind", "Water"]
    list.insert(0, 0)
    return list

def remove_element_from_end_of_list(l):
    list = ["Earth", "Fire", 3, 3]
    del list[0]
    return list

def remove_element_from_start_of_list(l):
    list = [2, "Fire", 3, "Water"]
    list.pop()
    return list

def retrieve_first_element_from_list(l):
    list = [1, 2, 3, 4]
    return list[0]

def retrieve_element_from_index(l, index):
    list = [1, 3, 4, 5]
    index = list.index(3)
    return index
   
def retrieve_last_element_from_list(l):
     list = [1, 2, 3, 4]
     return list[-1]

