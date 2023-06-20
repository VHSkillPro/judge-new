import subprocess
import helper.compile as compile
import settings.Judges as Judges
import settings.Constants as Constants
from classes.CompletedProcess import CompletedProcess

class Process :
    def __init__(self, fileName: str, timelimit: int = Judges.TIME_LIMIT_PER_TESTCASE) -> None:
        self.fileName = fileName
        self.isCompiled = False
        self.fileName = fileName
        self.timelimit = timelimit

    def compile(self) -> CompletedProcess | None:
        if self.isCompiled or (not compile.haveCompile(compile.getLanguage(self.fileName))) :
            return None
        
        process = subprocess.Popen(
            args = compile.getCompileCommand(self.fileName),
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        try :
            stdout, stderr = process.communicate(timeout = self.timelimit / 1000)
            if (process.returncode == 0) :
                return CompletedProcess(Constants.RETURN_CODE_ACCEPT, stdout.decode("utf-8"), stderr.decode("utf-8"))
            else :
                return CompletedProcess(Constants.RETURN_CODE_COMPILE_ERROR, stdout.decode("utf-8"), stderr.decode("utf-8"))

        except subprocess.TimeoutExpired :
            return CompletedProcess(Constants.RETURN_CODE_TIME_LIMIT_EXCEED)
    
    def run(self, stdin: str = None) -> CompletedProcess:
        compileProc = self.compile()
        if (compileProc != None) and (compileProc.returncode != Constants.RETURN_CODE_ACCEPT):
            return compileProc
        
        proc = subprocess.Popen(
            args = compile.getRunCommand(self.fileName),
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
        )
        try : 
            stdout, stderr = proc.communicate(
                input = stdin.encode("utf-8") if stdin != None else None,
                timeout = self.timelimit / 1000
            )
            if (proc.returncode == 0) :
                return CompletedProcess(Constants.RETURN_CODE_ACCEPT, stdout.decode("utf-8"), stderr.decode("utf-8"))
            else :
                return CompletedProcess(Constants.RETURN_CODE_RUNTIME_ERROR, stdout.decode("utf-8"), stderr.decode("utf-8"))
        except subprocess.TimeoutExpired :
            return CompletedProcess(Constants.RETURN_CODE_TIME_LIMIT_EXCEED)
        
    