# Exercise 8. Prefix/Suffix Check

url = "https://amazon.com"

is_secure = url.startswith("https")
is_com = url.endswith("com")

if is_secure and is_com:
    print("Given URL is Valid : connecting to the server...")
else :
    print("Given URL is invalid : please check again !")