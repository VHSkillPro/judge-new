import argparse
import settings.Judges as Judges
from app.Controller import Controller 

class Router :
    def __init__(self) -> None:
        self.route = argparse.ArgumentParser(prog="Judge",description="Judge for competitive progamming")
        self.route.add_argument("-c", "--code", dest="fileCode", help="File code need judge", required=True)
        self.route.add_argument("-s", "--sol", dest="fileSol", help="File solution", required=True)
        self.route.add_argument("-g", "--gen", dest="fileGen", help="File generator testcase", required=True)
        self.route.add_argument("-ck", "--check", dest="fileChecker", help= "File checker")
        self.route.add_argument("-nt", "--nTest", dest="nTest", help="Number of testcase", default=Judges.TESTCASE_NUMBER, type=int)
        self.route.add_argument("-tl", "--tlimit", dest="timelimit", help="Time limit per testcase", default=Judges.TIME_LIMIT_PER_TESTCASE, type=int)
        
        args = self.route.parse_args()
        app = Controller()
        app.judge(args.fileCode, args.fileSol, args.fileGen, args.fileChecker, args.nTest, args.timelimit)