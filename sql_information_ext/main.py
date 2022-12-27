import re
import json
def target_table_name(lst):
    '''It will return list contain dictionary(s) with type(join or from) with the table name'''
    from_pat = re.compile(r'FROM ')
    join_pat = re.compile(r'JOIN ')

    from_lst = re.split(from_pat,lst)
    join_lst = re.split(join_pat,lst)
      
    from_lst.pop(0)
    join_lst.pop(0)

    type_ = set()
    for i in from_lst:
      n = i.split()
      # print(n)
      if n[0]!='(':
        type_.add(n[0])
      
    join_ = set()
    for i in join_lst:
      n = i.split()
      # print(n)
      if n[0]!='(':
        join_.add(n[0])
           
    result = []
    
    for i in type_:
      dic = {}
      dic["type"] = 'FROM'
      dic["name"] = i
      result.append(dic)
    
    for i in join_:
      dic = {}
      dic["type"] = 'JOIN'
      dic["name"] = i
      result.append(dic)

    if len(result) == 0:
      return(None)
    else:
      return(result)

def check_type(c):
    ''' check the type for given query i.e. Update, Create or Insert'''
    if c=='I':
        return("Insert")
    elif c=='C':
        return("Create")
    elif c=='U':
        return("Update")

def sql_to_json(lst):
    res = []
    for i in range(len(lst)):
        dic = {}
        dic["statement_id"] = i+1
        dic["statement_type"] = check_type(lst[i][0])
        dic["target_table_name"] = target_table_name(lst[i])
        
        res.append(dic)
    
    final = json.dumps(res, indent=4)
    
    json_file = open('sample_stored_procedure.json','w')
    json_file.write(final)
    json_file.close()
    
    
if __name__=="__main__":
  
  # open and read the sql file
  f = open('sample_stored_procedure.sql')
  content = f.read()
  
  # split our string on the basis of specified pattern(split if three or more new line characters present in between two queries)
  pat = re.compile(r'\n\n\n+')

  # make a list of queries present
  lst = re.split(pat,content)
  # print(len(res))

  # removing unwanted query type
  for i in lst:
      if i[0]  == 'D':
          lst.remove(i)
          
  sql_to_json(lst)
  
  f.close()