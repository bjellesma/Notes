- s3 stands for simple storage service
- s3 stores objects
- objects in regions are divided further into **buckets** ![](images/../res/2021-07-24-16-47-12.png)
- When creating a bucket, set to public for demonstation purposes and ensure that the bucket has a unique name ![](images/../res/2021-07-24-16-53-10.png)

## Uploading to s3

Copy files to a remote server with the following command

```bash
aws s3 cp <local_folder> s3://<bucket>/<remote_folder> --recursive --exclude "<pattern>"
```

For example, to copy all of the js files, you would use the following command. We have no files to exclude.

```bash
aws s3 cp ./assets/js s3://pizza-luvrs-billj/js --recursive
```

If we log into aws now, we file be able to see these files ![](images/../res/2021-07-27-00-37-42.png)

### Cors

Enable CORS on your s3 bucket by using a JSON object ![](images/../res/2021-07-27-01-03-05.png)

### Creating IAM Roles

- Create a role through IAM to auth with your app ![](images/../res/2021-07-27-01-12-59.png)
- Create the role on EC2 and give the role full s3 access ![](images/../res/2021-07-27-01-14-23.png)
