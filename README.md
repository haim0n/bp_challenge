# Getting the code
    git clone git@bitbucket.org:haim_daniel/bp_challenge.git
  or 
    wget https://drive.google.com/open?id=1xXmsuVwaNm1wcucfdkSd0MdK0473SvfL

# Installation
    # extract the tarball
    $ tar -xzf bp_challenge.tgz
    
    # build the wheel 
    $ cd bp_challenge && \
    virtualenv -p python3 venv && \
    . venv/bin/activate && \
     python setup.py bdist_wheel
     
     # install the resulting wheel
     pip install dist/bp_challenge-0.1-py3-none-any.whl

# Running the service
    # make sure you're activated the venv from prev step
    $ bpc

# Using the service
    $ curl http://localhost:8080/events/countByEventType
    {"baz":2,"foo":3}
    $ curl http://localhost:8080/events/countWords
    {"amet":3,"dolor":13,"ipsum":11,"lorem":13,"sit":10}

