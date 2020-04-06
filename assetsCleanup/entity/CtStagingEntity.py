class CtStagingClass:
     def __init__(self,dirpath,createtime,videofileName,cid):
         self.dirpath=dirpath;
         self.createtime=createtime;
         self.videofileName=videofileName
         self.cid = cid;

     def __repr__(self):
        response = f"[{self.cid},{self.dirpath},{self.createtime},{self.videofileName}]"
        return  response;
     def convertToEntity(dirpath,createtime,videofileName,cid):
         return  CtStagingClass(cid,dirpath,createtime,videofileName);

