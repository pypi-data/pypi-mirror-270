from os.path import exists
from datetime import datetime
from sqlton import parse
from sqlton.ast import Select
from sqletic import Engine
from functools import partialmethod
from echovault import Vault 
from dulwich.object_store import DiskObjectStore
from dulwich.refs import DiskRefsContainer
    
def __forward(self, method_name, *args, **kwargs):
    if method_name.startswith('execute'):
        statement, = parse(args[0])
        
        return getattr(self._engine, method_name)(*args, *kwargs)
    else:
        return getattr(self._engine, method_name)(*args, *kwargs)

class Cursor:
    def __init__(self, tables, engine):
        self._engine = engine
        self._tables = tables

    def __iter__(self):
        yield from iter(self._engine)

    @property
    def description(self):
        return self._engine.description

    def close(self):
        ...

class Connection:
    def __init__(self, path, branch='main'):
        self.__path = path

        if exists(path + '/.git'):
            path += '/.git/'

        self.__tables = Vault(DiskObjectStore(path + '/objects/'),
                              DiskRefsContainer(path + '/'),
                              ref=branch)

        self._engine = Engine(self.__tables)

    def close(self):
        ...

    def commit(self):
        if self.__tables.tree.id == self.__tables.object_store[self.__tables.refs[self.__tables.ref]].tree:
            # nothing to commit as the hash of the tree did not change
            return
        
        self.__tables.commit(message=f'update at {datetime.now().isoformat()}')

    def rollback(self):
        self.__tables.rollback()

    def cursor(self):
        return Cursor(self.__tables, self._engine)

    @property
    def description(self):
        return self._engine.description

for method_name in {'execute', 'fetchone', 'fetchmany', 'fetchall'}:
    setattr(Cursor, method_name, partialmethod(__forward, method_name))
    setattr(Connection, method_name, partialmethod(__forward, method_name))

def connect(path):
    return Connection(path)
