import numpy as np

def table_shift(array, table_array):
  array_shifted = np.zeros(table_array.shape[0], dtype='int')

  for index, value in enumerate(table_array):
    array_shifted[index] = array[value-1]

  return array_shifted

def array_split(array):
  l = int(len(array)/2)
  left_split = array[:l]
  right_split = array[l:]

  return left_split, right_split

def shifting_LtoR(array):
  temp = array[0]

  for index in range(1, len(array)):
    array[index - 1] = array[index]
  
  array[len(array) - 1] = temp

  return array

table_p_10 = np.array([3,5,2,7,4,10,1,9,8,6])
table_p_08 = np.array([6,3,7,4,8,5,10,9])

key = list('0001101101')

k = table_shift(key, table_p_10)
left_split, right_split = array_split(k)
left_split = shifting_LtoR(left_split)
right_split = shifting_LtoR(right_split)
key_merge = np.concatenate((left_split, right_split))
key_1 = table_shift(key_merge, table_p_08)
print("key 01: ", "".join([str(elem) for elem in key_1]))

left_spl, right_spl = array_split(key_1)

left_spl = shifting_LtoR(left_spl)
right_spl = shifting_LtoR(right_spl)

key_2 = np.concatenate((left_spl, right_spl))
print("key 02: ", "".join([str(elem) for elem in key_2]))
