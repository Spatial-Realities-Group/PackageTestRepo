import argparse
from unityVersionHelpers import semanticVerStrToArray
from unityVersionHelpers import semanticVerArrayToStr

Major = 'Major'
Minor = 'Minor'
Patch = 'Patch'
AsIs = 'AsIs'

def incrementMajor(version: list[int, int, int]) -> list[int, int, int]:
    version[0] += 1
    version[1] = 0
    version[2] = 0
    return version

def incrementMinor(version: list[int, int, int]) -> list[int, int, int]:
    version[1] += 1
    version[2] = 0
    return version

def incrementPatch(version: list[int, int, int]) -> list[int, int, int]:
    version[2] += 1
    return version

def incrementVersion(version: list[int, int, int], incrementPart: str) -> list[int, int, int]:
    if incrementPart == Major:
        return incrementMajor(version)
    elif incrementPart == Minor:
        return incrementMinor(version)
    elif incrementPart == Patch:
        return incrementPatch(version)
    elif incrementPart == AsIs:
        return version
    else:
        raise Exception(f'Part ({incrementPart}) is not a valid option. Valid options: {", ".join([Major, Minor, Patch, AsIs])}')

def main():
    # Create command-line argument parser
    parser = argparse.ArgumentParser(description="Increment a Semantic version number")
    parser.add_argument('version_number', type=str, help='A Semantic version number')
    parser.add_argument('increment_part', type=str, help=f'Accepted Values: {", ".join([Major, Minor, Patch, AsIs])}')
    # Parse arguments
    args = parser.parse_args()
    version = semanticVerStrToArray(args.version_number)
    version = incrementVersion(version, args.increment_part)
    versionStr = semanticVerArrayToStr(version)
    return versionStr

if __name__ == "__main__":
    main()