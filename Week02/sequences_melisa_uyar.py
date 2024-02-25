my_int = 100
my_float =0.5
my_bool = True
my_complex= 11 + 14j


my_list = [1, "two",3,4]

my_tuple=(5,6,7)

my_set ={"eight",9}

my_dict={ "year":2023,
"month":"July",
"day": 29 }

def remove_duplicates(my_list):
    new_list=[]
    return new_list( set(my_list))

def list_counts(new_list):
  new_dict={}
  for e in new_list :
      if e in new_dict :
         new_dict[e] += 1
      else:
         new_dict[e] = 1
  return new_dict 

def reverse_dict(my_dict):
  reversed_dict  = {}
  for k, v in my_dict.items():
     reversed_dict[v] = k
  return reversed_dict


