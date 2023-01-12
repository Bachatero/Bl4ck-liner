
myType = 'CSV' #'csv' 'CSV' #'Excel'

urlAuth = 'https://us2.api.blackline.com/authorize/connect/token'

urlQuery = 'https://us2.api.blackline.com/api/queryruns'

urlDoc = 'https://us2.api.blackline.com/api/completedqueryrun/{0}/{1}'

apiKey = 'xyzxbikakkyyz' 



data = {'grant_type': 'password','scope': 'ReportsAPI instance_xyz','username': 'xyzUser.com','password': apiKey}

s = [120, 143, 91, 68, 75, 68, 177, 111, 102, 146, 70, 108, 122, 199, 137, 100, 82]
c = [66, 54, 122, 109, 51, 103, 50, 115, 116, 52, 111, 95, 52, 54, 50, 97]

url_pref = "https://xyz.com/sites/"
delimiter = "/"
outputDir = r"D:\Reports\OutputFiles\Blackline"
xorWord = lambda ss, cc: ''.join(chr(ord(s) ^ ord(c)) for s, c in zip(ss, cc * 100))

