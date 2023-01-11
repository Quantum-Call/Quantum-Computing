from qiskit import IBMQ
import logging
import os

#log = logging.getLogger(__name__)

    

def authentication():
    with open('ky.txt','r') as f:
        line = f.readline()
        MY_API_TOKEN = line
        IBMQ.save_account(MY_API_TOKEN)
    
    return IBMQ.load_account()
        #log.debug("Authentication Successfully logged")