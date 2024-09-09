def trianglearea(x,y,z): 
   print("Triangle Area Calculator")
   s = (x+y+z)/2
   area = (s*(s-x)*(s-y)*(s-z))**0.5
   print(area)

def main():
    x = float(input('Value of side x: '))
    y = float(input('Value of side y: '))
    z = float(input('Value of side z: '))
    trianglearea(x,y,z)
    
main()