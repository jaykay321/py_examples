import pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]],
    columns=["Price","Age","Value"],
    index=["First","Second"])

df2 = pandas.DataFrame([{"Name":"John", "Surname":"Wick"}, {"Name":"Timmy"}])

print(df1)
print(type(df1))
print(df2)

print(dir(df1))
print(df1.mean())
print(df1.mean().mean())
print(10*"-")
print(df1.Price)
