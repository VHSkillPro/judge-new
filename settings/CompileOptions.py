import settings.Constants as Constants

compileOptions = {
    Constants.WINDOWS : {
        "c" : "gcc -std=c11 -Wall -O2 -lm -fmax-errors=5 -march=native -s $fileName -o $fileNameWithoutExt.exe",
        "cpp" : "g++ -std=c++17 -Wall -O2 -lm -fmax-errors=5 -march=native -s $fileName -o $fileNameWithoutExt.exe"
    },
    Constants.LINUX : {
        "c" : "gcc -std=c11 -Wall -O2 -lm -fmax-errors=5 -march=native -s $fileName -o $fileNameWithoutExt",
        "cpp" : "g++ -std=c++17 -Wall -O2 -lm -fmax-errors=5 -march=native -s $fileName -o $fileNameWithoutExt"
    }
}

runOptions = {
    Constants.WINDOWS : {
        "c" : "$fileNameWithoutExt.exe",
        "cpp" : "$fileNameWithoutExt.exe",
        "py" : "python3 -m compileall -q $fileNameWithoutExt.py"
    },
    Constants.LINUX : {
        "c" : "./$fileNameWithoutExt",
        "cpp" : "./$fileNameWithoutExt",
        "py" : "python3 -m compileall -q $fileNameWithoutExt.py"
    }
}