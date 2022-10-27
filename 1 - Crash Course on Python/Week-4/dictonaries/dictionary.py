x = {}
type(x)
# <class "dict">

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
# {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts["txt"]
# 14
"jpg" in file_counts
# True
"html" in file_counts
# False
file_counts["cfg"] = 8
print(file_counts)
# {"jpg":10, "txt":14, "csv":2, "py":23, "cfg":8}
file_counts["jpg"] = 5
# {"jpg":5, "txt":14, "csv":2, "py":23, "cfg":8}
del file_counts["cfg"]
print(file_counts)
# # {"jpg":5, "txt":14, "csv":2, "py":23}


toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"] = 39 # Epilogue starts on page 39
toc["Chapter 3"] = 24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
if "Chapter 5" in toc:
    print(True)
else:
    print(False) # Is there a Chapter 5?