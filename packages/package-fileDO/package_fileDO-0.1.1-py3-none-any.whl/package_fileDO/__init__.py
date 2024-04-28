from .FileDO import FileDO

identifier = 'ids:dataset/999a2b6ca6ce8a0d0c88ca99b602613e83d926daf9de1c72bca5db15a399c986'
f = FileDO(identifier)
r = f.downloadFileDO()
print(r)


response_json = f.getFileLocalPath()
print(response_json)

response_json = f.getDownloadProgress()
print(response_json)
