import os

def find_files(search_path, filename):
   result = []

# Wlaking top-down from the root
   for root, dir, files in os.walk(search_path):
      if filename in files:
         result.append(os.path.join(root, filename))
   return result

x = input("give that fuckin shit: ")
y = input("second shit: ")

print(find_files(x,y))
