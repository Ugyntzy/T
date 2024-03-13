from queue import LifoQueue
b_h= LifoQueue()
f_h= LifoQueue()
c_page = None

#visit function
noofvisits= int(input("enter the number of url history"))
print("enter URLS to visit:")
for i in range(noofvisits):
 url=input("URL: ")
 print(f"visiting {url}")
 b_h.put(c_page)
 c_page= url

 #display current page
 print(f"current page: {c_page}")

# go back
 while input("do you want to go back? (yes /no):").lower() =="yes":
  if not b_h.empty():
   f_h.put( c_page)
   c_page= b_h.get()
   print(f"going back to {c_page}")
else:
    print("no previous page available")

#go forward
while input("do you want to go forward? (yes/no):").lower() =="yes":
  if not f_h.empty():
    b_h.put(c_page)
    c_page = f_h.get()
    print(f"going forward to {c_page}")
  else:
    print("no current page available")