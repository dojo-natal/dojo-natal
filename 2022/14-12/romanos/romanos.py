
romano_to_indo_mapping = {
  'I' : 1,
  'IV': 4,
  'V' : 5,
  'IX': 9,
  'X' : 10,
  'L' : 50,
  'C' : 100,
  'CD': 400,
  'D' : 500,
  'M' : 1000,
}

indo_to_romano_mapping = {
  1: 'I',
  # 4: 'IV', 
  5: 'V',
  # 9: 'IX',
  10: 'X',
  50: 'L',
  100: 'C',
  # 400: 'CD',
  500: 'D',
  1000: 'M',
}


reverted_indo_to_romano_keys = list(indo_to_romano_mapping.keys())[::-1]


def convert_romanos_to_indo(romanos_string):
  return '1'

def convert_indo_to_romanos(indo_value: int):


  if indo_value in indo_to_romano_mapping:
    return indo_to_romano_mapping[indo_value]

  # for key in list(indo_to_romano_mapping.keys())[::-1]: # IIII
  #   if key <= indo_value:
  #     return indo_to_romano_mapping[key] * indo_value
  
  return_value = ''
  index_value = 0

  while indo_value > 0:
    current_key_verify = reverted_indo_to_romano_keys[index_value]

    if indo_value >= current_key_verify and (indo_value % 4 != 0 or indo_value % 9 != 0):
      return_value += indo_to_romano_mapping[current_key_verify]
      indo_value -= current_key_verify
    else:
      
      pre_index = None
      
      if index_value + 2 < len(reverted_indo_to_romano_keys):
        pre_index = reverted_indo_to_romano_keys[index_value + 2]
      elif index_value + 1 < len(reverted_indo_to_romano_keys):
        pre_index = reverted_indo_to_romano_keys[index_value + 1]

      if indo_value >= current_key_verify - pre_index:
        str_value = indo_to_romano_mapping[pre_index] + indo_to_romano_mapping[current_key_verify]
        return_value += str_value
        indo_value -= current_key_verify - pre_index

      index_value += 1

      # if indo_value >= current_key_verify - pre_index:
      #   str_value = indo_to_romano_mapping[pre_index] + indo_to_romano_mapping[current_key_verify]
      #   return_value += str_value
      #   indo_value -= current_key_verify - pre_index
      # elif indo_value >= current_key_verify - pre_index_2:
      #   str_value = indo_to_romano_mapping[pre_index_2] + indo_to_romano_mapping[current_key_verify]
      #   return_value += str_value
      #   indo_value -= current_key_verify - pre_index_2



  return return_value
  
 
  


  

