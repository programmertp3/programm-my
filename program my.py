data = []
while True:
    user_input = input("یک متن وارد کنید (برای خروج 'exit' را وارد کنید): ")
    
    if user_input.lower() == 'exit':
        break
data.append(user_input)
print("\nشما این موارد را وارد کرده‌اید:")
for item in data:
    print(item)
