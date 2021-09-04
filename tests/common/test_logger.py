from PRODUCER.commons.logger import get_logger

def test_get_logger():
    logger = get_logger('test')
    logger.debug('In the test DEBUG')
    logger.info('In the test INFO')
    logger.error('In the test ERROR')
    logger.critical('In the test CRITICAL')
    assert logger.name == 'test'
	