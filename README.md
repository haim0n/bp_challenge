# Getting the code
git clone git@bitbucket.org:haim_daniel/bp_challenge.git

# Installation 
    $ cd bp_challenge && \
    virtualenv -p python3 venv && \
    . venv/bin/activate && \
    python setup.py install

# Running the service
    # make sure you're activated the venv from prev step
    $ bpc

# Using the service
    $ curl http://localhost:8080/events/countByEventType
    {"baz":2,"foo":3}
    $ curl http://localhost:8080/events/countWords
    {"amet":3,"dolor":13,"ipsum":11,"lorem":13,"sit":10}

