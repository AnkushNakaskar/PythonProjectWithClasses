import yaml
import os;


class ProjectConfig:
    def __init__(self):
        self.cfg =self.__readConfig();
    def __repr__(self):
        response = f"[{self.cfg}]"
        return response;

    def __readConfig(self):
        print("path >>>>"+str(os.curdir+ "/config/local.yaml"))
        with open(os.curdir+ "/config/local.yaml", "r") as ymlfile:
            config = yaml.load(ymlfile)
        return  config;
