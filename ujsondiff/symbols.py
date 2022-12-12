class Symbol:
    def __init__(self, label):
        self.label = label

    def pack(self):
        return bytes(self.label, "utf-8")

    @staticmethod
    def unpack(data):
        return Symbol(data.decode("utf-8"))

    def __eq__(self, other):
        if isinstance(other, Symbol):
            return self.label == other.label
        else:
            return False

    def __hash__(self):
        return hash(self.label)

    def __repr__(self):
        return self.label

    def __str__(self):
        return "$" + self.label


missing = Symbol("missing")
identical = Symbol("identical")
delete = Symbol("delete")
insert = Symbol("insert")
update = Symbol("update")
add = Symbol("add")
discard = Symbol("discard")
replace = Symbol("replace")
left = Symbol("left")
right = Symbol("right")

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
    right,
]

__all__ = [
    "missing",
    "identical",
    "delete",
    "insert",
    "update",
    "add",
    "discard",
    "replace",
    "left",
    "right",
    "_all_symbols_",
]
