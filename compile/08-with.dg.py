..compile      = import
..parse.tree   = import
..parse.syntax = import


with = (code) ->
  parse.syntax.ERROR: (not $ code `isinstance` parse.tree.Closure) 'wtf'
  parse.syntax.ERROR: (not: code) 'wtf'
  (code.popleft:), code


compile.r.builtins !! 'with' = (self, code) ->
  '''
    with $
      context
      do_something

    Evaluate `context`, call its `__enter__` method, then `do_something`.
    `context`'s `__exit__` method is called in the end regardless
    of whether `do_something` finished successfully; it may also silence
    the exception.

  '''

  context, stuff = with: code
  self.load: None
  end_ptr = self.opcode: 'SETUP_WITH' context delta: 2
  self.opcode: 'POP_TOP'         delta: -1
  self.opcode: 'ROT_THREE' stuff delta:  1
  self.opcode: 'ROT_TWO'         delta:  0
  self.opcode: 'POP_BLOCK'       delta: -1
  self.load: None
  end_ptr:
  self.opcode: 'WITH_CLEANUP' delta: 1
  self.opcode: 'END_FINALLY' delta: -3
