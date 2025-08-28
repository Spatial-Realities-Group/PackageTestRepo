import argparse
from unityVersionHelpers import getPackageVersionStr

def main():
    # Create command-line argument parser
    parser = argparse.ArgumentParser(description="Build a Unity project")
    parser.add_argument('path_to_package', type=str, help='The path to the Unity package json file')

    # Parse arguments
    args = parser.parse_args()
    return getPackageVersionStr(args.path_to_package)

if __name__ == "__main__":
    main()