1. Create a login
```sql
USE [master]
GO
CREATE LOGIN [SQLLOGIN] WITH PASSWORD=N'Password', DEFAULT_DATABASE=[CommerceCenter], DEFAULT_LANGUAGE=[us_english], CHECK_EXPIRATION=OFF, CHECK_POLICY=OFF
GO
```
2. Map the login to a user
```sql
USE [CommerceCenter]
GO
CREATE USER [vendordb] FOR LOGIN [SQLLOGIN] WITH DEFAULT_SCHEMA=[dbo]
GO
```
