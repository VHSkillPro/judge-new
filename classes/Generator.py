import settings.Judges as Judges
from classes.CompletedProcess import CompletedProcess
from classes.Process import Process
from datetime import datetime

class Generator (Process) :
    def __init__(self, fileName: str, timelimit: int = Judges.TIME_LIMIT_PER_TESTCASE) -> None:
        super().__init__(fileName, timelimit)
        
    def run(self, stdin: str = None, argv: list[str] = None) -> CompletedProcess:
        return super().run(stdin, (argv if argv != None else []) + [str(datetime.now().timestamp() * 10**6)])
        