# from ..utils.data_utils import get_file

import numpy as np
import six.moves.cPickle as pickle
import gzip

#def load_data(mypath='mnist.pkl.gz'):
def load_data(mypath='imagetest_new_140x140.pkl.gz'):
    """Loads the MNIST dataset.

    # Arguments
        path: path where to cache the dataset locally
            (relative to ~/.keras/datasets).

    # Returns
        Tuple of Numpy arrays: `(x_train, y_train), (x_test, y_test)`.
    """

    with gzip.open(mypath, 'rb') as f:
        try:
            train_set, valid_set, test_set = pickle.load(f, encoding='latin1')
        except:
            train_set, valid_set, test_set = pickle.load(f)

    # path = get_file(path, origin='mnist.pkl.gz')
    # f = np.load(path)
    # x_train = f['x_train']
    # y_train = f['y_train']
    # x_test = f['x_test']
    # y_test = f['y_test']
    f.close()
    x_train = np.asarray( train_set[0] )
    y_train = np.asarray( train_set[1] )
    x_test = np.asarray( valid_set[0] )
    y_test = np.asarray( valid_set[1] )
    x_data = np.asarray( test_set[0] )
    y_data = np.asarray( test_set[1] )
    # return train_set , test_set
    return (x_train, y_train), (x_test, y_test) , (x_data , y_data)

if __name__ == '__main__':
    xxx = load_data()
    print( type(xxx[0][0][0]) )

    pass