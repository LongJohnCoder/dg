builtins  = import
operator  = import
functools = import
importlib = import

# Choose a function based on the number of arguments.
varary = (*fs) -> (*xs) -> (fs !! (len: xs)): (*): xs

builtins . $ = (f, *xs) -> f: (*): xs
builtins . : = (f, *xs) -> f: (*): xs
builtins . , = (*xs) -> xs

builtins . <  = operator.lt
builtins . <= = operator.le
builtins . == = operator.eq
builtins . != = operator.ne
builtins . >  = operator.gt
builtins . >= = operator.ge
builtins . is = operator.is_
builtins . in = (a, b) -> operator.contains: b a

builtins . not = operator.not_
builtins . ~   = operator.invert
builtins . +   = varary: None operator.pos operator.add
builtins . -   = varary: None operator.neg operator.sub
builtins . *   = operator.mul
builtins . **  = operator.pow
builtins . /   = operator.truediv
builtins . //  = operator.floordiv
builtins . %   = operator.mod
builtins . !!  = operator.getitem
builtins . &   = operator.and_
builtins . ^   = operator.xor
builtins . |   = operator.or_
builtins . <<  = operator.lshift
builtins . >>  = operator.rshift

builtins.import = importlib.import_module
builtins.foldl  = functools.reduce
builtins . ~:   = functools.partial
builtins . ...  = Ellipsis
