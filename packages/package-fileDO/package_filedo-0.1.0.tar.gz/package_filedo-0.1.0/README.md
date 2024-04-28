# python SDK

## 接口设计

### getFileLocalPath() 方法

- **功能描述**：获取文件地址
- **输入参数**：DO标识，如："ids:dataset/999a2b6ca6ce8a0d0c88ca99b602613e83d926daf9de1c72bca5db15a399c986"
- **输出**：文件地址，如："C:/ada/icc"
- **调用Java端接口**：`toLocalPath`

### downloadFileDO() 方法

- **功能描述**：输入DO标识作为参数，下载文件
- **输入参数**：DO标识，如："ids:dataset/999a2b6ca6ce8a0d0c88ca99b602613e83d926daf9de1c72bca5db15a399c986"
- **输出**：无
- **调用Java端接口**：`downloadFileDO`

### batchDownloadFileDO() 方法

- **功能描述**：批量下载
- **输入参数**：DO标识组
- **输出**：无
- **调用Java端接口**：`downloadFileDO`

### getDownloadProgress() 方法

- **功能描述**：获取下载进度
- **输入参数**：DO标识，如："ids:dataset/999a2b6ca6ce8a0d0c88ca99b602613e83d926daf9de1c72bca5db15a399c986"
- **输出**：实时下载进度结果
- **调用Java端接口**：`getDownloadProgress`

## Python SDK设计步骤

http://127.0.0.1:21030/SCIDE/SCManager?action=executeContract&contractID=IODIC&operation=downloadFileDO&arg={"dpml":"<dpml><data>ids:dataset/999a2b6ca6ce8a0d0c88ca99b602613e83d926daf9de1c72bca5db15a399c986</data></dpml>"}

mime

pypi
