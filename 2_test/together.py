import os
import sys
import re
import scipy as sci
import numpy
import string
import cPickle
import gzip
import time

import theano
import theano.tensor as T
from theano.tensor.shared_randomstreams import RandomStreams

from sda import SdA
from dae_class import dA
from theano_class import theano_top

corruption_level = 0.3
learning_rate = 10
batch_size = 1000.0
testing_epochs = 10
weight_reg = 0.05
sparsity_param = 0.05
sparsity_penalty = 3
stopping_condition = 0.0001

x = T.matrix('x')
rng = numpy.random.RandomState(123)
theano_rng = RandomStreams(rng.randint(2 ** 30))
autoencoder = dA( numpy_rng=rng, weight_reg=weight_reg, sparsity = sparsity_param,
            sp_penalty = sparsity_penalty, theano_rng=theano_rng, input=x, n_visible= 2000, n_hidden = 4000 )     

                
theanos = theano_top( autoencoder, stopping_condition, corruption_level, learning_rate,
                    '10_train.npy', '10_test.npy' )                
                
theanos.run_train( batch_size, 25 )                
                
#theanos.run_test( batch_size, testing_epochs )                
                
                