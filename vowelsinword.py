def vowelcount():
  vowels = "AEIOUaeiou"
  result = 0
  for num in word:
    if num in vowels:
      result += num
  return result