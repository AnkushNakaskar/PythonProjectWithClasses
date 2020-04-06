import logging
import os

from assetsCleanup.entity.CtStagingEntity import CtStagingClass

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def set_type(obj, dest_type):
    return dest_type(obj.dirpath, obj.createtime, obj.videofileName, obj.cid)


def processing(inputrecords):
    NoOfCidProcessed = 0;
    if inputrecords and type(inputrecords) is list:
        for record in inputrecords:
            record = set_type(record, CtStagingClass);
            logger.info("processing cid  ::: " + str(record.cid) + " With Number Of processing :: " + NoOfCidProcessed)
            NoOfCidProcessed += 1;
            try:
                if os.path.exists(record.dirpath):
                    logger.info("processing cid  ::: " + str(record.cid) + " With Directory path :: " + record.dirpath)
                    os.remove(record.dirpath);
            except Exception as e:
                logger.error("Exception in removing file for record : " + str(record))
