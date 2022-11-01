import sys
(i,mul) = (None, 0)
for line in sys.stdin:
    (key, value) = line.strip().split("\t")
    if i and i!=key:
        print ("%s\t%s" % (i,mul))
        (i,mul) = (key,float(value))
    else:
        (i,mul) = (key, mul + float(value))
print ("%s\t%s" % (i, mul))
