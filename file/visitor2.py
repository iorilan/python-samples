from visitor import FileVisitor
v = FileVisitor(trace=0)
v.run("D:\Tmp")
print(v.dcount, v.fcount)