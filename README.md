This repository contains a simple sample of how to process multipart form-data in Azure Functions using Python. This demonstrate the support added [here](https://github.com/Azure/azure-functions-python-library/commit/dbda14f635b9967a9b6f20acdf0d26ee7e011655).

When running locally or deploying to Azure, one can access the sample HTML page like below:

![alt text](https://user-images.githubusercontent.com/207474/57368849-d68a5800-7194-11e9-815c-98969756d38f.png "Screenshot 1")

After uploading a file, a page is returned with the name of the uploaded file:

![alt text](https://user-images.githubusercontent.com/207474/57368850-d68a5800-7194-11e9-82cf-205453a3f0d5.png "Screenshot 2")

Code tested on:

```
$ func --version
2.7.1158
```
