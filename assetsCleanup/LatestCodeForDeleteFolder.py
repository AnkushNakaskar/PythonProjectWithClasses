import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
from assetsCleanup.service.CtStagingService import  fetchListOfRecord
from assetsCleanup.processor.FileProcessor import processing
from assetsCleanup.config.PropertyReader import ProjectConfig

if __name__ == '__main__':
    query = "select replace(CONVERT(url USING utf8),'http://pcontent.vuclip.com/partner','/pcontent/storage'),createtime,video_file_name,cid from ct_staging_content where  date(createtime)  BETWEEN '2019-04-01' AND '2020-03-01' and status='published'  and cid  in (select cid from forbidden_content) "
    iniValues = {
        "dbhost": "localhost",
        "dbuser": "root",
        "dbpassword": "Vuclip@123",
        "dbschema": "blueapple"
    }
    value =ProjectConfig();
    value =value.cfg["mysql"]["host"]

    logger.info("Value for config :: "+value)

    # listOfRecord =fetchListOfRecord(query,iniValues);
    # logger.info ("listOfRecords ::  "+str(listOfRecord));
    # processing(listOfRecord)
