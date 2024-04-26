from dulwich.objects import Tree, Blob
from stat import S_IFREG, S_IFDIR
from uuid import uuid4
from echovault._container import Container
from echovault.dict import Dict

class List(Container):
    def __init__(self, object_store, container, identifier, values=(), *, tree=None):
        super().__init__(object_store, container, identifier, tree)
        self.extend(values)

    def __iter__(self):
        for key in self.tree:
            if key == b'_':
                continue
            
            _, id_ = self.tree[key]
            yield Dict(self.object_store,
                       self,
                       key,
                       tree=self.object_store[id_])
            
    def append(self, value):
        self.extend((value,))
            
    def extend(self, iterable):
        for item in iterable:
            identifier = str(uuid4()).encode('utf-8')
            self.tree[identifier] = S_IFDIR, None
            entry = Dict(self.object_store,
                         self,
                         identifier,
                         item)

        self._update()
            
    def remove(self, entry):
        del self.tree[entry.identifier]
        
        self._update()
