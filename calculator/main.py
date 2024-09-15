import art


def add(n1,n2):
  return n1 + n2
  
def subtract(n1,n2):
  return n1 - n2
  
def multiply(n1,n2):
  return n1 * n2
  
def divide(n1,n2):
  return n1 / n2 



operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}


def calculate():
  print(art.logo)

  num1 = float(input("what is the first number: "))
  calculate_over = False
  
  while not calculate_over:
    
    for i in operations:
      print(i)
    
    operation_type = input("pick the operation you wanted.")
    num2 = float(input("what is the second number: "))
    calculation_function = operations[operation_type]
    answer = calculation_function(num1, num2) 
    print(f"{num1} {operation_type} {num2} = {answer} ") 
    cont = input("would you like to go on with same number ?  'y' or 'n' ")
    
    if cont == "y":
      num1 = answer
    elif cont == "n":
      calculate_over = True
      calculate()
    else:
      print("please print 'y' or 'n' ")
      
calculate()


      
    
    
    
    
  



