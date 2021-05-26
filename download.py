import gdown
def download_from_drive():

    url = 'https://drive.google.com/uc?id=1OFU0jAaUIhvWS3MSIlZmvxfYVGCOjzwO'
    output = './BestModel1'
    gdown.download(url, output, quiet=False)
