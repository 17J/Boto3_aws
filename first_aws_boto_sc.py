# # # import boto3



# # # client = boto3.client('s3')
# # # # client = boto3.client("eks")


# # # # response = client.create_bucket(
# # # #     Bucket='rahul-demo-yt-boto-1285',
# # # #     CreateBucketConfiguration={
# # # #         'LocationConstraint': 'ap-south-1'
# # # #     },
   
# # # # )

# # # #get list of bucket

# # # respo = client.get_bucket_acl(
# # #     Bucket = "rahul-demo-yt-boto-1285",
# # #     # print(f"{Bucket}")
# # # )


# # # print(respo)


# # # import json

# # # x =  '{ "name":"John", "age":30, "city":"New York"}'

# # # y = json.loads(x)
# # # print(y)

# # #josn.loads is using convert json code into python

# # # import json
# # # x = '{"name":"Rahul","age":"25"}'

# # # y = json.loads(x)
# # # print(y)


# # import json

# # # j = '{"name":"rahul"}'

# # # h = json.loads(j)
# # # print(h)


# # # y = '{"name":"rahul","lname":"joshi"}'

# # # k = json.loads(y)

# # # print(k)


# # # fulldetails = '{"fname":"rahul","lname":"joshi","kname":"kish"}'

# # # hh = json.loads(fulldetails)
# # # print(hh)

# # # infodetails = '{"fname":"jl","sjk":"jsk","sajjsh":"hsajhs"}'

# # # print(json.loads(infodetails))

# # # myinf = '{"fname":"jsjja","saj":"sajjas","sjakjsa":"jsakjs"}'
# # # k = json.loads(myinf)
# # # print(k)
# # # print(json.dumps(k))

# # # infodetails = '{"fname":"rahul","lname":"jishu"}'
# # # kk = json.loads(infodetails)
# # # print(kk)
# # # #for python to json

# # # print(json.dumps(kk))


# # # basidetails = '{"fname":"rahul","lname":"joshi"}'

# # # #json to python
# # # y = json.loads(basidetails)
# # # print(y)
# # # #python to json
# # # h = json.dumps(y)
# # # print(h)


# # # needs = '{"niyam":"dridh","abhyas":"dridh"}'

# # # #json to python
# # # ool = json.loads(needs)
# # # print(f"code of python is {ool}")

# # # #python to json

# # # print(json.dumps(ool))


# # # needs = '{"abyas":"dridh","niyam":"dridh"}'
# # # #json to python

# # # jj = json.loads(needs)
# # # print(jj)
# # # #python to json
# # # print(json.dumps(jj))

# # # needs = {"abyas": "dridh", "niyam": "dridh"}

# # # #python to json
# # # jj = print(json.dumps(needs))
# # # #json to python
# # # # print(json.loads(jj))
# # # kk = json.loads(jj)
# # # print(kk)


# # # x = {
# # #   "name": "John",
# # #   "age": 30,
# # #   "city": "New York"
# # # }
# # # #python to json
# # # print(json.dumps(x))
# # # print(json.dumps({"name": "John", "age": 30}))


# # x = {
# #   "name": "John",
# #   "age": 30,
# #   "married": True,
# #   "divorced": False,
# #   "children": ("Ann","Billy"),
# #   "pets": None,
# #   "cars": [
# #     {"model": "BMW 230", "mpg": 27.5},
# #     {"model": "Ford Edge", "mpg": 24.1}
# #   ]
# # }
# # import json
# # a = '{"fname":"rahul","lname":"joshi"}'

# # #json to python
# # conver = json.loads(a)
# # print(conver)
# # #python to json 
# # print(json.dumps(conver))

# # # python to json
# # print(json.dumps(x,indent=5,separators=(". ", " = ")))

# # import json
# # full_info = '{"fname":"rahul","lname":"joshi","edu":"b.tech"}'
# # #json to python convert

# # j = json.loads(full_info)
# # # print(j)

# # #python to json
# # print(json.dumps(j))


# # try:
# #   print("Hello")
# # except:
# #   print("welcome")
# # x = 10
# # try:
# #   print(f"Hello world {x}")
# # except NameError as e:
# #   print("Hello")


# # f = open("sample.txt","x")
# # f.write("Hello")

# # f = open("sample.txt","a")
# # f.write("\nHello")

# # f = open("sample.txt","r")
# # print(f.readline())

# # print(f.readline())

# # import json

# # # some JSON:
# # x =  '{ "name":"John", "age":30, "city":"New York"}'

# # # parse x:
# # y = json.loads(x)

# # # the result is a Python dictionary:
# # print(y["city"])


# #for loop with dictonary


# nested_dict = {"group1": ["a", "b", "c"], "group2": {"x": 10, "y": 20}}

# # for i in my_dict:
# #   print(f"Value of {i} values are {my_dict[i]}")

# # for key, value in my_dict.items():
# #     if value > 2:
# #         print(f"Key: {key}, Value: {value} (greater than 2)")
# #     else:
# #         print(f"Key: {key}, Value: {value} (less than or equal to 2)")

# # for key in my_dict:
# #   if keys == my_dict[key]

# # for g_name,g_item in nested_dict.items():
# #   print(f"Group:{g_name}")
# #   if 

# # filtered_dict = {key: value for key, value in my_dict.items() if key not in ["b", "d"]}
# # print(f"Filtered dictionary: {filtered_dict}")

# # thisdict = {"a":1,"b":2,"c":3}
# # for x, y in thisdict.items():
# #   print(x, y)

# # for x in thisdict:
# #   if thisdict[x] == 2:
# #     print("value is equal to two")
# #     continue
  
#   # print(f"values of {x} and {thisdict[x]}")
  
  
  
  
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}


for x in myfamily:  
  # print(x,y)
  if myfamily[x] == "child2":
    print(myfamily[x])
    print(f"value of child is {myfamily[x]["name"]}")
# # for x in myfamily:
# #   print(x)
# #   for y in myfamily[x]:
# #     print(y)
# #     if myfamily[x] == "":
# #       print(f"value is eqaul to two just print name {myfamily[x]["name"]}")
      