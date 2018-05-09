# image-registration-summer-school-2018
Python notebooks and data for learning about image registration.  Hosted at a summer school

## How to install jupyter
Make sure you have python3 and virtualenv installed

tensorflow intsallation intsructions are good for getting to this point

Now run

virtualenv -p python3 ~/image_registration_summer_school_python

Now activate your virtual environment

source ~/image_registration_summer_school_python/bin/activate

Now double check you are using the right python

which python

the output should point to ~/image_registration_summer_school

Now use pip to install packages

pip install ipython jupyter numpy matplotlib nibabel

Now run the notebook server

jupyter notebook

