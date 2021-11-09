import json
import random

def prepareGraph(filename, json_dump):
    just_nodes = []
    jsoned = {'nodes': [], 'edges': []}

    data = 'var rendru = ' + json_dump
    savefile = open('%s.js' % filename, 'w+')
    savefile.write(data)
    savefile.close()

    vision = open('ErgoVision.html', 'r')
    lines = vision.readlines()
    lines[6] = '<script id="ourfile" src="%s"></script>\n' % (filename + '.js')
    with open('ErgoVision.html', 'w+') as vision_save:
        for line in lines:
            vision_save.write(line)

    vision.close()
