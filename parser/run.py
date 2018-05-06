
"""
Runs the java parser on a small java source file
"""
import sys
sys.path.insert(0, '../../pybison/build/lib.linux-x86_64-2.7/')
import parsec

#src = "tst.java"

argv = sys.argv
argc = len(argv)
verbose =1
keepfiles=0

if argc == 2:
    src = argv[1]
else:
    src = None

p = parsec.Parser(verbose=verbose)

print "delmebld.py: running parser on HelloWorldApp.java"
res = p.run(file=src)
print "back from engine, parse tree dump follows:"
if 0:
    print "------------------------------------------"
    res.dump()
    print "------------------------------------------"
    print "end of parse tree dump"
