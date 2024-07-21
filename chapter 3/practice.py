# string slicing 
""" name=input('enter your name: ')
fname=name[0:4]
mname=name[5:9]
last_name=name[10:1]
print('your first name is: ',fname)
print('your middle name is: ',mname)
print('your last name is,',last_name)
print(len(name)) """
# -----------------------------------

""" # name = 'syed'
# first = name[-len(name):]
# print(first) """
# ------------------------------------
# negative string slicing
""" name = 'syed'
first = name[-4:-1] #this can print only 'sye' not full name
first_full = name[-4:-1]+name[-1] #this can print fullname'syed' 
print(first)
print(first_full) """
  
#print name with negative idexex
""" name=input('enter your name: ')
fname=name[-17:-13]
mname=name[-12:-8]
last_name=name[-7:-1]+name[-1] #tichneque to print last infex
print('your first name is: ',fname)
print('your middle name is: ',mname)
print('your last name is,',last_name)
print(-len(name)) """

# --------------------------------------
""" name = 'syed'
first = name[-4:-1] + name[-1]
print(first) """

""" name = 'syed'
first = name[-4:0] + name[0:] # [0:] it means [0:-1]
print(first) """
# -----------------------------------------------
""" name= 'SyedUmer'
print(len(name)) #find the length of string
print(name.endswith('mer')) #tr ue
print(name.startswith('ume')) #false
print(name.startswith('sy')) #false
print(name.startswith('Sy')) #true """
# ----------------------------------------------------
""" name= 'umer gillani'
print(name.capitalize() """
# --------------------------------------
""" x=-6.45344
print(abs(-4))
# print(round(8.34343,3))
print(round(x,4))
print(int(x))
print(type(x))
y=int(x)
print(type(y)) """
# -----------------------------------------
                           #escape sequences examples
""" print('i am syed umer gillani, and i am AI student')
print('i am syed umer gillani,\n and i am AI student')
print('i am syed umer gillani,\t and i am AI student')
print('i am syed umer gillani, \'and i am AI student\'')
print('i am syed umer gillani, "and i am AI student"')
print("i am syed umer gillani, 'and i am AI student'") """

                #chapter 3 practice set
                

# this is just replace funcation
""" name=input('enter your name:')
print(f'good afternoon, {name}') 
letter = 'Dear <|Name|>,You are selected!<|Date||>'
print(letter.replace("<|Name|>","umer").replace("<|Date||>","24 sep,2024"))  """
# ----------------------------------------------------------------------------
# this is find and replace funcation

""" name='hey! I am Syed Umer   Gillani'
print(name.find("   "))
print(name.replace("   "," "))
letter = "Dear Harry,\n \tthis python course is nice. \n\tThanks!"
print(letter)  """