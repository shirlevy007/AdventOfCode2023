import re

ALMANAC_WORDS = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity ', 'location']
DICTS = ['seed_to_soil', 'soil_to_fertilizer', 'fertilizer_to_water', 'water_to_light', 'light_to_temperature',
         'temperature_to_humidity', 'humidity_to_location']

def get_seeds(output):
    seeds = output[0].split()
    seeds = sorted(int(number) for number in seeds)
    return seeds

def get_results(seeds, list_of_dicts):
    for dic in list_of_dicts:
        items = list(dic.keys())
        item_index = 0
        for i, seed in enumerate(seeds):
            while items[item_index]+dic[items[item_index]][1]-1 < seed and item_index < len(items)-1:
                item_index += 1
            if items[item_index] <= seed <= items[item_index]+dic[items[item_index]][1]-1:
                seeds[i] = dic[items[item_index]][0]+(seed-items[item_index])
            # if item_index == len(items)-1:
            #     break
        seeds = sorted(seeds)
    return seeds[0]
    # return min(seeds)





def mapping_values(text_file="Day5_IfYouGiveASeedAFertilizer.txt"):
    seeds_regex = "seeds:\s((\d+\s)+)"
    dict_name_regex = "([a-z]+)-to-([a-z]+) map:"
    dst_src_rng_regex = "(\d+)\s(\d+)\s(\d+)"

    text_file = open(text_file, "r")
    line = text_file.readline()
    seeds = []
    if line:
        output = re.findall(seeds_regex, line)[0]
        seeds = get_seeds(output)
    list_of_dicts = []
    line = text_file.readline()
    while (line):
        try:
            dict_name_match = re.match(dict_name_regex, line)
            if dict_name_match:
                current_dict = {}
                line = text_file.readline()
                dsr_match = re.match(dst_src_rng_regex, line)
                while line and dsr_match:
                    dst, src, rng = dsr_match.group(1), dsr_match.group(2), dsr_match.group(3)
                    current_dict[int(src)] = (int(dst), int(rng))
                    line = text_file.readline()
                    dsr_match = re.match(dst_src_rng_regex, line)

                current_dict = dict(sorted(current_dict.items()))
                list_of_dicts.append(current_dict)
            else:
                line = text_file.readline()
        except Exception as e:
            print(e)
        # done creating necessary dicts
    return seeds, list_of_dicts

def manage(txt_file = "Day5_IfYouGiveASeedAFertilizer.txt", part1=True):
    seeds, list_of_dicts = mapping_values(txt_file)
    return get_results(seeds, list_of_dicts)


if __name__ == '__main__':
    print(manage())
