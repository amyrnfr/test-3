num = int (input("Enter a two-digit number"))
tens = num // 10 
ones = num % 10
result1 = tens ** ones
result2 = ones ** tens
print(f"{tens}^{ones}=={result1}")
print(f"{ones}^{tens}=={result2}")