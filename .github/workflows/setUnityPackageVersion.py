import argparse
from unityVersionHelpers import setPackageVersion

def main():
    # Create command-line argument parser
    parser = argparse.ArgumentParser(description="Build a Unity project")
    parser.add_argument('path_to_package', type=str, help='The path to the Unity package json file')
    parser.add_argument('version_number', type=str, help='A Semantic version number')

    # Parse arguments
    args = parser.parse_args()
    setPackageVersion(args.path_to_package, args.version_number)

if __name__ == "__main__":
    main()