from typing import Type, TypeVar, Generic
from types import TracebackType, FunctionType

T = TypeVar('T')
class NamespaceGroup(Generic[T]):
    def __init__(self, group_name: str = "lol") -> None:
        self.members: dict[str, Type[T]] = {}

    def __enter__(self):
        return self

    def add(self, elem: T, alias: str | None = None) -> None:
        if alias is None:
            alias: str = elem.__name__

        if isinstance(elem, FunctionType): # is a function
            self.members[alias] = FunctionType(elem.__code__, globals())

        else: # is a class
            method_dict = {name: method for name, method in elem.__dict__.items() if callable(method)}
            self.members[alias] = type(alias, (object,), method_dict)

        # add as attribute
        setattr(self, alias, self.members[alias])

    def __exit__(self,
                 exec_type: Type[BaseException] | None,
                 exec_value: BaseException | None,
                 traceback: TracebackType | None) -> bool | None:
        if exec_type is not None:
            print(f'Exception: {exec_type} with value {exec_value}\ntraceback: {traceback}')

if __name__ == '__main__':
    pass
