import argparse
import os.path
from unityVersionHelpers import getPackageVersionStr

def main():
    # Create command-line argument parser
    parser = argparse.ArgumentParser(description="Build a Unity project")
    parser.add_argument('path_to_package', type=str, help='The path to the Unity package json file')

    # Parse arguments
    args = parser.parse_args()

    if not os.path.isfile(args.path_to_package):
        raise Exception(f"Path to package.json not valid: {args.path_to_package}")

    version = getPackageVersionStr(args.path_to_package)
    return version

if __name__ == "__main__":
    main()