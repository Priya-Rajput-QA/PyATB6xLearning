"""Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.
I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request"""

status_code = int(input("Enter the response code:").strip())
if status_code ==200:
    print("Passed API Request")
elif status_code == 404:
    print("Failed API Request")
else:
    print("Not valid API Request")


