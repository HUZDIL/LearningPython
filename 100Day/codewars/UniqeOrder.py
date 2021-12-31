def unique_in_order(iterable):
   chars = []

   for i in iterable:
         chars.append(i)

   for i in chars:
       if chars.count(i) == chars.count(i+1):
           chars.count(i+1).remove()


   return chars


print(unique_in_order("AAAABBBCCDAABBB"))