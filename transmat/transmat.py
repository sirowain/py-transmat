from py3wetransfer import Py3WeTransfer
from urllib.parse import urlparse
import requests
import argparse
import os, sys

x = None


def upload(files, msg):
    print(x.upload_files(files, msg))


def download(wetransfer_url):
    resp = requests.head(wetransfer_url, allow_redirects=True)
    url_comps = str(resp.url).split("/")
    url = "https://wetransfer.com/api/v4/transfers/"+url_comps[4] + "/download"
    post = requests.post(url, json={"security_hash":url_comps[5]})

    direct_link = urlparse(post.json()["direct_link"])
    # download
    filename = direct_link.path.split("/")[-1]
    print("Downloading file: " + filename)
    file_download = requests.get(direct_link.geturl())
    open(filename, 'wb').write(file_download.content)


def print_apikey_info():
    print("""
    Transmat needs a valid API Key from https://developers.wetransfer.com
    export WETRANSFER_API_KEY=<apikey>
    """)


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.required = True
group.add_argument("-d", "--download", dest="url", help="WeTransfer short url")
group.add_argument("-u", "--upload", dest="files", nargs='+', help="List of files to be uploaded")
parser.add_argument("-m", "--message", help="Optional upload message")


def main():
    global x
    wetransfer_apikey = os.environ.get('WETRANSFER_API_KEY')

    if not wetransfer_apikey:
        print_apikey_info()
        sys.exit(1)
    else:
        x = Py3WeTransfer(wetransfer_apikey)

    args = parser.parse_args()
    if args.url:
        download(args.url)
    elif args.files:
        message = "Transmat file upload"
        if args.message:
            message = args.message
        upload(args.files, message)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
