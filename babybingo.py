import matplotlib.pyplot as plt
import numpy as np
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Create bingo matrix')
    parser.add_argument('--nrows', type=int, default=4,
                        help='number of rows in matrix')
    parser.add_argument('--ncols', type=int, default=4,
                        help='number of columns in matrix')
    parser.add_argument('--figsize', type=int, default=12,
                        help='size of figure in inches')
    parser.add_argument('--fontsize', type=int, default=14,
                        help='font size')
    parser.add_argument('--file', type=str, default='tiles.txt',
                        help='path to text file from which to read tile texts. \
                        Each tile text should be separated by a new line.')
    parser.add_argument('--savename', type=str, default=None,
                        help='full path to file where bingo matrix is to be saved')
    return parser

def get_tiles(fpath):
    tiles = []
    with open(fpath, 'r') as fo:
        for line in fo: # do not need to use fo.readline() in python 3
            tiles.append(line.rstrip())
    return tiles

def get_matrix(tiles, nrows=3, ncols=3, figsize=(12,12), fontsize=14):

    selected_tiles = np.random.choice(tiles, replace=False, size=nrows*ncols)

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize = figsize, sharey=True, sharex=True)
    fig.subplots_adjust(wspace=0, hspace=0)
    for i,ax in enumerate(axes.flatten()):
        text = selected_tiles[i].split(' ')
        character_count = 0
        formatted_text = ''
        for word in text:
            character_count+=len(word)
            formatted_text += f'{word} '
            if character_count>figsize[0]/nrows*3:
                formatted_text += '\n'
                character_count = 0

#         formatted_text = '\n'.join([text])
        ax.text(0.5, 0.5,
                formatted_text,
                fontsize=fontsize,
                horizontalalignment='center',
                verticalalignment='center',
                transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])
    fig.suptitle('baby bingo\ndate:', fontsize=20, y=0.95)
    return fig

if __name__ == '__main__':
    parser = parse_arguments()
    args = parser.parse_args()
    ncols = args.ncols
    nrows = args.nrows
    fpath = args.file
    figsize = args.figsize
    fontsize = args.fontsize
    savename = args.savename

    tiles = get_tiles(fpath)

    fig = get_matrix(tiles, nrows=nrows, ncols=ncols, figsize=(figsize, figsize), fontsize=14)

    if savename is not None:
        fig.savefig(f'{savename}.png')
