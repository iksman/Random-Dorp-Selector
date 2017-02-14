import csv,random
  
class Node:
  def __init__(self,value,tail):
    self.isEmpty = False
    self.value = value 
    self.tail = tail
    self.pos = self.tail.pos + 1

class Empty:
  def __init__(self):
    self.pos = 0
    self.isEmpty = True
  
def getTo(node,item):
  list = node
  for i in range(0,item):
    if list.isEmpty == False:
      if i == (item - 1):
        return list.value
      else:
        list = list.tail

with open('nonDuplicateList.csv','r+') as csvfile:
  reader = csv.reader(csvfile, delimiter=",")
  first = True
  for row in reader:
    if first:
      first = False
      list = Empty()
    else:
      try:
        list = Node(str(row[2]),list)
      except:
        pass

csvfile.close()
item = random.randint(0, list.pos + 1)


print(getTo(list,item))