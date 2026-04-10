
s= "Hello word"

#O(1) access
print("First char:",s[0])

#O(n) traversal
for c in s:
    print(c, end="")

#O(n) concatenation (new string created each time)
s2 = s + "!!!"
print("\nConcantenated:", s2)

#O(n) substring search
print("Contains'word'?", "world"in s)

