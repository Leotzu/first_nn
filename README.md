This is the first neural network I leanred how to build. Started in January 2020.

Website guide: https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/ 

Software configuration guide (theano, keras, tensorflow, etc.): https://machinelearningmastery.com/setup-python-environment-machine-learning-deep-learning-anaconda/ 

Installed in virtualenv:
------
pip install scipy numpy matplotlib pandas statsmodels sklearn pymc3 theano tensorflow-gpu==2.0 keras

# NOTE: using tensorflow 2.0.0 ($ pip install tensorflow-gpu==2.0), since 2.1 was giving lots of errors.

# NOTE: theano is giving me this warning (WARNING (theano.tensor.blas): Using NumPy C-API based implementation for BLAS functions.), so I installed pymc3 and mkl, but no luck. It seems to just make things slower, so I ignored it and everything works just fine. 
------

RUN: 
$ python keras_first_network.py 

