def search_suggestion(products, searchword):
  products.sort()
  prefix = ''
  ans = []
  for char in searchword:
    prefix += char
    ans.append([x for x in products if x.startswith(prefix)][:3])
  return ans

    