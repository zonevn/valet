import pickle


class DataAdapter:

    def load(self, db):
        fopen = open(db, 'rb')
        data = pickle.load(fopen)
        fopen.close()
        return data

    def save(self, db, data):
        fopen = open(db, 'wb')
        pickle.dump(data, fopen)
        fopen.close()
