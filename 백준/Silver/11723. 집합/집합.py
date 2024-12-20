import sys ; input = sys.stdin.readline

class Set :
    def __init__(self) :
        self.set = set()
        
    def add(self, x: int) :
        if self._check(x) : return
        self.set.add(x)
        
    def remove(self, x: int) :
        if not self._check(x) : return
        self.set.remove(x)

    def check(self, x: int) :
        print(self._check(x))

    def _check(self, x: int) :
        if x in self.set : return 1
        else             : return 0

    def toggle(self, x: int) :
        if self._check(x) : self.remove(x)
        else              : self.add(x)

    def all(self) :
        self.set = set([i + 1 for i in range(20)])

    def empty(self) :
        self.set = set()

if __name__ == "__main__" :
    M = int(input().rstrip())
    S = Set()

    for _ in range(M) :
        command = input()
        
        if len(command.split()) > 1 :
            command, x = command.split()
            x = int(x)
        
        if   'add'    in command : S.add(x)
        elif 'remove' in command : S.remove(x)
        elif 'check'  in command : S.check(x)
        elif 'toggle' in command : S.toggle(x)
        elif 'all'    in command : S.all()
        elif 'empty'  in command : S.empty()