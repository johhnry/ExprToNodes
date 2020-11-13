import abc


class ASTNode(abc.ABC):
    @abc.abstractmethod
    def expand(self):
        raise NotImplemented

    @abc.abstractmethod
    def accept(self, visitor):
        raise NotImplemented
