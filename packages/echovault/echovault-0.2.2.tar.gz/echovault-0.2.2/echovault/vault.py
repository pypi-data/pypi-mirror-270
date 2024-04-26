from dulwich.objects import Tree, Commit
from echovault.list import List
from base64 import b64decode, b64encode
from socket import getfqdn, gethostname
from os import getpid, getlogin, name as operating_system_name
from sys import argv
from typing import Optional
from time import time
from stat import S_IFDIR
from echovault._container import Container

try:
    from os import getuid, getgid
except:
    def getuid():
        return None

    def getgid():
        return None
    

class Vault(Container):
    @staticmethod
    def encode(string):
        return string.encode('utf-8')

    @staticmethod
    def decode(value):
        return value.decode('utf-8')
    
    def __init__(self, object_store, refs, *, tree:Tree=None, ref=None):
        self.refs = refs

        if ref is not None:
            ref = b'refs/heads/' + ref.encode('utf-8')
            
            if ref in self.refs and tree is None:
                tree = self.object_store[self.object_store[self.refs[ref]].tree]
        
        self.ref = ref

        super().__init__(object_store, None, None, tree)

    def __getitem__(self, name:str):
        identifier = self.encode(name)
        _, oid = self.tree[identifier]
        tree = self.object_store[oid]
        return List(self.object_store,
                     self,
                     identifier,
                     tree=tree)

    def __setitem__(self, name:str, iterable):
        identifier = self.encode(name)
        self.tree[identifier] = S_IFDIR, None
        table = List(self.object_store, self, identifier, iterable)
        self._update()

    def __delitem__(self, name:str):
        del self.tree[self.encode(name)]
        self._update()

    def __iter__(self):
        return (self.decode(raw_key)
                for raw_key
                in iter(self.tree))

    def rollback(self):
        if self.ref is None:
            self.tree = Tree()
        else:
            self.tree = self.object_store[self.object_store[self.refs[ref]].tree]
    
    def commit(self,
               ref:Optional[str]=None,
               message:Optional[str]='',
               author:Optional[str]=None,
               committer:Optional[str]=None,
               time_:Optional[int]=None,
               timezone:Optional[int]=None,
               ):
        if ref is None:
            ref = self.ref
        else:
            ref = b'refs/heads/' + ref.encode('utf-8')
            
        commit = Commit()
        
        commit.message = message.encode('utf-8')
        commit.tree = self.tree

        if committer is None:
            committer = ('_'.join((getfqdn(), gethostname(),
                                   operating_system_name,
                                   repr(getgid()),
                                   repr(getuid()), repr(getpid())))
                         + ': '
                         + ' '.join(argv))
            
        if author is None:
            author = getlogin()

        commit.committer = committer.encode('utf-8')
        commit.author = author.encode('utf-8')

        if time_ is None:
            time_ = int(time())

        if timezone is None:
            timezone = 0

        commit.commit_time = time_
        commit.commit_timezone = timezone
        commit.author_time = time_
        commit.author_timezone = timezone

        try:
            parents = (self.refs[ref],)
        except:
            parents = ()
            
        commit.parents = parents
        
        if not commit.id in self.object_store:
            self.object_store.add_object(commit)

        self.refs[ref] = commit.id
