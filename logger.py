
# import logging

# logging.basicConfig(filename='logging.txt')

# logging.warning('Hello world!')
# logging.info('Hello world again!')


import logging

logger = logging.getLogger('ArthurSay')

hdlr = logging.FileHandler('/var/tmp/arthur123.log')

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)

logger.addHandler(hdlr) 

logger.setLevel(logging.DEBUG)

# logger.error('We have a problem')
# logger.info('While this is just chatty')



