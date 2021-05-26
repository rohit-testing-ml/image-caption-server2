import gdown
def download_from_drive():
    url = 'https://drive.google.com/uc?id=1lPiJ05zxv4Nepq2PNTKv8Onyf72rXfBL'
    output = 'BestModel'
    gdown.download(url, output, quiet=False)