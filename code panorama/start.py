from os import path, listdir
from stitching_detailed import main
import numpy as np
from pprint import pprint

# класс для конвертации словаря в объект
class DictToObject(object):
    def __init__(self, myDict):
        for key, value in myDict.items():
            if type(value) == dict:
                setattr(self, key, DictToObject(value))
            else:
                setattr(self, key, value)

scr_dir = path.dirname(path.abspath(__file__))

# папка с изображениями для панорамы
imagesDir = "d1/"

# получаем список файлов в папке, конкретизируем путь к ним
imagesDirContent = listdir(scr_dir+'/'+imagesDir)
imagesDirContent = [imagesDir+i for i in imagesDirContent]

# словарь параметров создания панорамы
params = {
    'img_names': imagesDirContent,
    'try_cuda': False,
    'work_megapix': 0.6,
    'features': 'brisk',
    'matcher': 'homography',
    'rangewidth': -1,
    'match_conf': 0.3,
    'conf_thresh': 1,
    'estimator': 'homography',
    'ba': 'ray',
    'ba_refine_mask': 'xxxxx',
    'wave_correct': 'horiz',
    'save_graph': 'test.txt',
    'warp': 'cylindrical',
    'seam_megapix': 0.1,
    'seam': 'gc_colorgrad',
    'compose_megapix': -1,
    'expos_comp': 'no',
    'expos_comp_nr_feeds': np.int32(1),
    'expos_comp_block_size': np.int32(32),
    'blend': 'multiband',
    'blend_strength': np.int32(5),
    'timelapse': None,
    'output': 'result.jpg',
}

# конвертация словаря в объект
params = DictToObject(params)

main(params)
