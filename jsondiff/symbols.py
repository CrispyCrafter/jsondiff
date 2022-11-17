import struct 

class Symbol(object):
    def __init__(self, label):
        self.label = label

    def pack(self):
        s = bytes(self.label, 'utf-8')
        return struct.pack("I%ds" % (len(s),), len(s), s)
    
    @staticmethod
    def unpack(data):
        (i,), data = struct.unpack("I", data[:4]), data[4:]
        return Symbol(data[:i].decode("utf-8") )

    def __repr__(self):
        return self.label

    def __str__(self):
        return "$" + self.label

missing = Symbol('missing')
identical = Symbol('identical')
delete = Symbol('delete')
insert = Symbol('insert')
update = Symbol('update')
add = Symbol('add')
discard = Symbol('discard')
replace = Symbol('replace')
left = Symbol('left')
right = Symbol('right')

_all_symbols_ = [
    missing,
    identical,
    delete,
    insert,
    update,
    add,
    discard,
    replace,
    left,
    right
]

__all__ = [
    'missing',
    'identical',
    'delete',
    'insert',
    'update',
    'add',
    'discard',
    'replace',
    'left',
    'right',
    '_all_symbols_'
]