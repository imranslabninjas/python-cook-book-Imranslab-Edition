record = ('ACME', 50, 123.45, (12, 18, 19, 2012))
name, *_, (*__, year) = record

print(name)
print(*_)
print(*__)
print(year)
