import argparse, json, pathlib, os

parser = argparse.ArgumentParser()
parser.add_argument('paths', type=pathlib.Path, nargs='+')
args = parser.parse_args()

args.paths = [os.path.abspath(p) for p in args.paths]

merged_scenes  = {}

for i, path in enumerate(args.paths):
    with open(path, 'r') as input_json:
        data = json.load(input_json)

    for j, (scene_name, scene) in enumerate(data['scenes'].items()):
        if scene_name in merged_scenes:
            scene_name = f'{i}-{j}'

        merged_scenes[scene_name] = scene

subsets = {'train': list(merged_scenes)}

with open('merged.json', 'w') as merged_json:
    json.dump({
        'scenes' : merged_scenes,
        'subsets': subsets,
    }, merged_json)
