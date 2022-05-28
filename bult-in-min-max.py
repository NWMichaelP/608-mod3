#Code By Michael Pogue
def maximum(value1, value2, value3):

#Defining Values for Max
  max_value = value1
  if value2 > max_value:
    max_value = value2
  if value3 > max_value:
    max_value = value3
  return max_value
def minimum(value1, value2, value3):

#Defining Values for Max
  min_value = value1
  if value2 < min_value:
    min_value = value2
  if value3 < min_value:
    min_value = value3
  return min_value