import check50
import check50.c

@check50.check()
def exists():
    """bharat.c exists"""
    check50.exists("bharat.c")

@check50.check(exists)
def compiles():
    """bharat.c compiles"""
    check50.c.compile("bharat.c", lcs50=True)

@check50.check(compiles)
def world():
    """bharat.c prints \"Hello Bharat\""""
    check50.run("./bharat").stdout("Hello Bharat").exit()