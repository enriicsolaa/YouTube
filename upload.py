import argparse
import starfilese

def upload_file(file_path):
    link = starfiles.upload(file_path)
    print(link)

def main():
    parser = argparse.ArgumentParser(description='Upload a file to Starfiles')
    parser.add_argument('file', metavar='file_path', type=str, help='path to the file to upload')
    args = parser.parse_args()

    upload_file(args.file)

if __name__ == "__main__":
    main()
