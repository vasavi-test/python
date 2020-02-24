import json
# data = """
# {"items":[{"objectGroupid":"12345","count":100}]
# ,"groupBy":"objectGroupid","count":100}
# """
# print type(data)
# data_dict = json.loads(data)
# print  data_dict["count"]
# print len(data_dict["items"])

data = {"items":[{"objectGroupid":"12345","count":100}]
 ,"groupBy":"objectGroupid","count":100}
print type(data)

data_json = json.dumps(data)
print data_json
print type(data_json)