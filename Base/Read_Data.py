import yaml,os
class Read_Data:
    def __init__(self,file_name):
        self.file_path=os.getcwd()+os.sep+'Data'+os.sep+file_name+'.yml'
    def get_test_data(self):
        with open (self.file_path,'r',encoding='utf-8') as f:
            return yaml.load(f)
    def get_test_data1(self):
        with open (self.file_path,'r',encoding='utf-8') as f:
            return yaml.load(f)