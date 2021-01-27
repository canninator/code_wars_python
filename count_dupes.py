def count_dupes(text):
  return (sum(x != 1 for x in {i : text.lower().count(i) for i in  text.lower()}.values()))

count_dupes("Indivisibilities")
