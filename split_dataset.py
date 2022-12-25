import argparse
from utils.dataloaders import *

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, default='./datasets/cars' , help='path to image dir')
    opt = parser.parse_args()
    autosplit(path=opt.path, weights=(0.8, 0.2, 0.2))