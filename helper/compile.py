import os
import settings.CompileOptions as CompileOptions

def getFileNameWithoutExt(fileName: str) -> str :
    language = getLanguage(fileName)
    return fileName.removesuffix("." + language) if language != None else fileName

def getLanguage(fileName: str) -> str | None :
    pos = fileName.rfind('.')
    return fileName[pos + 1::] if pos != -1 else None 

def haveCompile(language: str) -> bool:
    return language in CompileOptions.compileOptions[os.name]

def haveRun(language: str) -> bool :
    return language in CompileOptions.runOptions[os.name]

def getCompileCommand(fileName: str) -> list[str] | None:
    language = getLanguage(fileName)
    if not haveCompile(language) :
        return None
    cmd = CompileOptions.compileOptions[os.name][language]
    cmd = cmd.replace("$fileNameWithoutExt", getFileNameWithoutExt(fileName))
    return cmd.replace("$fileName", fileName).split(sep=" ")

def getRunCommand(fileName: str, argv: list[str] = None) -> list[str] | None :
    language = getLanguage(fileName)
    if not haveRun(language) :
        return None
    cmd = CompileOptions.runOptions[os.name][language]
    return cmd.replace("$fileNameWithoutExt", getFileNameWithoutExt(fileName)).split(sep=" ") + (argv if argv != None else [])