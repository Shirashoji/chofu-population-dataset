import json
import numpy as np

def json2dict(jsonFilePath):
    with open(jsonFilePath, 'r') as f:
        data = json.load(f)
    return data

def dict2json(data, jsonFilePath):
    with open(jsonFilePath, 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    
def cosSim(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return np.dot(arr1, arr2) / (np.linalg.norm(arr1) * np.linalg.norm(arr2))

def main(inname, outname):
    data = json2dict(inname)
    outdata = []
    
    if (data[0]["town"] == "市内全域"):
        chofu = data[0]
    
    chofuArr = np.array(list([[i["male"], i["female"]]
                        for i in chofu["data"]])).flatten()

    for i in range(1, len(data)):
        townArr = np.array(list([[j["male"], j["female"]]
                                 for j in data[i]["data"]]), dtype=np.float64).flatten()
        cossim = cosSim(chofuArr, townArr)

        # 居住者がいない時全て0のコサイン類似度となるためJSONにしない
        if not np.isnan(cossim):
            outdata.append({"town": data[i]["town"], "value": cossim})
    dict2json(outdata, outname)


if __name__ == '__main__':
    import glob
    files = glob.glob("./normalized/*.json")
    for file in files:
        print(file)
        main(file, file.replace("normalized", "cosSim"))
    # main("./normalized/2021.json", "./cosSim/2021.json")
