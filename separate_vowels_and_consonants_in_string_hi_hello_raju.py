st="hi hello raju"
vo="aeiou"
con=["consonents="]+[val for val in st if val not in vo and val not in  " "],["vowels="]+[val for val in st if val in vo],["spaces="]+[val for val in st if val in " "]
print(con)
