#!/usr/bin/env python3
"""
Scripts to train a keras model using tensorflow.
Basic usage should feel familiar: train.py --tubs data/ --model models/mypilot.h5

Usage:
    train.py [--tubs=tubs] (--model=<model>) [--type=(linear|inferred|tensorrt_linear|tflite_linear)]

Options:
    -h --help              Show this screen.
"""

# Import OpenCV first, see https://github.com/opencv/opencv/issues/14884
import cv2

from docopt import docopt
import donkeycar as dk
from donkeycar.pipeline.training import train


def main():
    args = docopt(__doc__)
    cfg = dk.load_config()
    tubs = args['--tubs']
    model = args['--model']
    model_type = args['--type']
    train(cfg, tubs, model, model_type)


if __name__ == "__main__":
    main()
