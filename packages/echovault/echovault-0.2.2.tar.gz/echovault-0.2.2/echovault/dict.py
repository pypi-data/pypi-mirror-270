from dulwich.objects import Tree, Blob
from pickle import dumps, loads
from base64 import b64decode, b64encode
from stat import S_IFREG
from echovault._container import Container 

class Dict(Container):
    @staticmethod
    def encode(value):
        return b64encode(dumps(value))

    @staticmethod
    def decode(value):
        return loads(b64decode(value))
    
    def __init__(self, object_store, container, identifier, items=(), *, tree=None):
        super().__init__(object_store, container, identifier, tree)
        self.update(items)

    def __getitem__(self, key):
        _, id_ = self.tree[self.encode(key)]
        return loads(self.object_store[id_].data)

    def __setitem__(self, key, value):
        self.update(((key, value),))

    def update(self, items):
        if hasattr(items, 'items'):
            items = items.items()
        
        for key, value in items:
            blob = Blob()
            blob.data = dumps(value)
        
            if not blob.id in self.object_store:
                self.object_store.add_object(blob)
            
            self.tree[self.encode(key)] = S_IFREG | 0o755, blob.id

        self._update()


    def __delitem__(self, key):
        del self.tree[self.encode(key)]
        
        self._update()
            
    def __iter__(self):
        return (self.decode(raw_key)
                for raw_key
                in iter(self.tree)
                if raw_key != b'_')

    def keys(self):
        yield from iter(self)

    def items(self):
        for key in self.keys():
            yield (key, self[key])

    def values(self):
        for _, id_ in self.tree.values:
            return loads(self.object_store[id_].data)
        
    def __repr__(self):
        return repr(dict(self.items()))
