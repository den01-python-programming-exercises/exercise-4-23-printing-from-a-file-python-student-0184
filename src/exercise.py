def main():
    #write your code below this line
    with open("data.txt",'r') as f:
      data = f.read().splitlines()
    
    for row in data:
      print(row)

if __name__ == '__main__':
    main()
