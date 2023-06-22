import settings.Judges as Judges
import settings.Constants as Constants
import settings.Messages as Messages
from classes.Process import Process
from classes.CompletedProcess import CompletedProcess

class Checker (Process) :
    def __init__(self, fileName: str, timelimit: int = Judges.TIME_LIMIT_PER_TESTCASE) -> None:
        super().__init__(fileName, timelimit)
        
    def run(self, fileInp: str, fileOut: str, fileAns: str) -> CompletedProcess:
        if (self.fileName == None) :
            fout = open(fileOut, "r")
            fans = open(fileAns, "r")
            
            if (fout.read().strip() == fans.read().strip()) :
                return CompletedProcess(Constants.RETURN_CODE_ACCEPT)
            else :
                return CompletedProcess(Constants.RETURN_CODE_WRONG_ANS)
                
        return super().run(argv = [fileInp, fileOut, fileAns])