import gdown
import os
import argparse


downs = {
    "MTT":{
        "url":"https://drive.google.com/drive/folders/1B2yBBGUyb71JdA4SEfIefDVUEGt_-b5R?usp=drive_link",
        "output" : 'MTT'
    },
}




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download experiments')
    parser.add_argument('--path', type=str, default='', help='file_path')
    args = parser.parse_args()
    mtt = downs['MTT']
    output = os.path.join(args.path , mtt['output'])
    gdown.download_folder(url=mtt['url'], output=output)