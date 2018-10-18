def parse(args):
    delimiter = '='
    arr = {}
    for elem in args:
        if delimiter in elem:
            key_val = elem.split(delimiter,1)
            arr[key_val[0]] = key_val[1]
    return arr


def load_data(file):
    import pickle
    data = {}
    try:
        fileopen = open(file, 'rb')
        data = pickle.load(fileopen)
        fileopen.close()
    except:
        save_data(data, file)
    finally:
        return data


def save_data(data, file):
    import pickle
    fileopen = open(file, 'wb')
    pickle.dump(data, fileopen)
    fileopen.close()
