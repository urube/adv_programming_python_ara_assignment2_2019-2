"""
    >>> import tkinter
    >>> canvas = tkinter.Canvas(tkinter.Tk(), width=500, height=500)
    >>> from drawer_kieran import DrawerKieran
    >>> from parser_jerry import ParserJerry
    >>> d = DrawerKieran(canvas)
    >>> p = ParserJerry(d)
    >>> p.parse(["P 2"])
    Selected pen 2

    >>> p.parse(["X 250"])
    GOTO X=250

    >>> p.parse(["Y 250"])
    GOTO Y=250

    >>> p.parse(["D 0"])
    pen down

    >>> p.parse(["W 200"])
    drawing line of length 200 at 270 degrees

    >>> p.parse(["N 100"])
    drawing line of length 100 at 0 degrees

    >>> p.parse(["E 200"])
    drawing line of length 200 at 90 degrees

    >>> p.parse(["S 100"])
    drawing line of length 100 at 180 degrees

    >>> p.parse(["U 0"])
    pen up

    >>> from drawer_jack import DrawerJack
    >>> from parser_dang import ParserDang
    >>> d = DrawerJack(canvas)
    >>> p = ParserDang(d)
    >>> p.parse(["P 2"])
    Selected pen 2

    >>> p.parse(["X 250"])
    GOTO X=250

    >>> p.parse(["Y 250"])
    GOTO Y=250

    >>> p.parse(["D 0"])
    pen down

    >>> p.parse(["W 200"])
    drawing line of length 200 at 270 degrees

    >>> p.parse(["N 100"])
    drawing line of length 100 at 0 degrees

    >>> p.parse(["E 200"])
    drawing line of length 200 at 90 degrees

    >>> p.parse(["S 100"])
    drawing line of length 100 at 180 degrees

    >>> p.parse(["U 0"])
    pen up

    >>> from drawer_turtle_jack import DrawerTurtleJack
    >>> from parser_jonathan_v2 import ParserJonathon
    >>> d = DrawerTurtleJack(canvas)
    >>> p = ParserJonathon(d)
    >>> p.parse(["P 2"])
    Selected pen 2

    >>> p.parse(["X 250"])
    pen up
    GOTO X=250

    >>> p.parse(["Y 250"])
    pen up
    GOTO Y=250

    >>> p.parse(["D 0"])
    pen down

    >>> p.parse(["W 200"])
    drawing line of length 200 at 270 degrees

    >>> p.parse(["N 100"])
    drawing line of length 100 at 0 degrees

    >>> p.parse(["E 200"])
    drawing line of length 200 at 90 degrees

    >>> p.parse(["S 100"])
    drawing line of length 100 at 180 degrees

    >>> p.parse(["U 0"])
    pen up

"""
import doctest

if __name__ == '__main__':
    doctest.testmod()
