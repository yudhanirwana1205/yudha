#import time
#import math

#def calculate_time(func):

 #   def inner1(*args, **kwargs):
        
  #      begin = time.time()

   #     func(*args, **kwargs)

    #    end = time.time()
     #   print("total time taken in: ",func.
      #        __name__,end - begin)

       # return inner1
    
#@calculate_time
#def factorial(num):

 #       time.sleep(2)
  #      print(math.factorial(num))

#factorial(10)


import requests

#r = requests.get('https://jsonplaceholder.typicode.com/posts')
#data = r.json()
#print(data)

post = {
    'body' : "lorem ipsum",
    'title': "Title",
    'userld': 5,
    'id' : 5
}

req = requests.post('https://jsonplaceholder.typicode.com/posts', json=post)
print(req.json())

update_post = post
update_post['id'] = 5

req = requests.put('https://jsonplaceholder.typicode.com/posts/5', json=update_post)
print(req.json())

square = lambda x: x ** 2
print(square(2))