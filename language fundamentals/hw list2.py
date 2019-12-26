words = ["python", "fun"]
index = 1
words.insert(index+5, "is")
print(words)
print(words[2])

nums = [9, 8, 7, 6]
nums.insert(2, 11)
nums.append(12)
print(nums)
print(len(nums))

letters = ["a", "b", "c", "l", "a", "a"]
print("\n", letters.index("c"))

print(max(letters))
print(letters.count("a"))