import json
    
def setPackageVersion(pathToJsonFile: str, version: str) -> None:
    try:
        packageJson = getPackageJsonStr(pathToJsonFile)
        packageJson["version"] = version
        
        jsonFile = open(pathToJsonFile, 'w')
        json.dump(packageJson, jsonFile)
        jsonFile.close()
        return packageJson
    except Exception as e:
        print(f"Unable to set Unity project version to: {version}. Reason: {e}")

def getPackageJsonStr(pathToJsonFile: str) -> str:
    try:
        jsonFile = open(pathToJsonFile, 'r')
        packageJson = json.loads(jsonFile.read())
        jsonFile.close()
        return packageJson
    except Exception as e:
        print(f"Returning empty string for package version string. Reason: {e}")
        return ""

def getPackageVersionStr(pathToJsonFile: str) -> str:
    return getPackageJsonStr(pathToJsonFile)['version']

def getPackageVersion(pathToJsonFile: str) -> list[int, int, int]:
    versionStr = getPackageVersionStr(pathToJsonFile)
    return semanticVerStrToArray(versionStr)

def validateSemanticVersion(version: list[int, int, int]) -> bool:
    length = len(version)
    if (length != 3):
        raise Exception(f"Version number has length ({length}). Expected (3) parts for a semantic version number")
    elif (not version[0].isdigit()):
        raise Exception(f"Major version ({version[0]}) is not a whole number")
    elif (not version[1].isdigit()):
        raise Exception(f"Minor version ({version[1]}) is not a whole number")
    elif (not version[2].isdigit()):
        raise Exception(f"Patch version ({version[2]}) is not a whole number")
    else:
        return True
    return False

def semanticVerStrToArray(versionStr: str) -> list[int, int, int]:
    versionNums = versionStr.split('.')
    if validateSemanticVersion(versionNums):
        return [int(versionNums[0]), int(versionNums[1]), int(versionNums[2])]

def semanticVerArrayToStr(version: list[int, int, int]) -> str:
    if validateSemanticVersion(version):
        return f'{version[0]}.{version[1]}.{version[2]}'