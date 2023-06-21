class CompletedProcess : 
    def __init__(self, returncode: int, outs: str = None, errs: str = None) -> None:
        self.returncode = returncode
        self.outs = outs
        self.errs = errs