import sys
import importlib
import pymysql
# import MySQLdb
import logging

from assetsCleanup.entity  import CtStagingEntity



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def fetchListOfRecord(query,iniValues):
    try:
        logger.info("Fetching record from database for host :: " + iniValues.get("dbhost"))
        db = pymysql.connect(host=iniValues['dbhost'],
                             user=iniValues['dbuser'],
                             passwd=iniValues['dbpassword'],
                             db=iniValues['dbschema'])
        cursor = db.cursor();
        cursor.execute(str(query));
        logger.info("Started QC Process ..!!")
        logger.info("Total video process   are  : " + str(cursor.rowcount))
        listOfRecords =[];
        for record in cursor:
            listOfRecords.append(CtStagingEntity.CtStagingClass(str(record[0]),str(record[1]),str(record[2]),str(record[3])))
        return  listOfRecords;
    except Exception as  e:
        logger.error("Exception while fetching data from database :: ",e)
