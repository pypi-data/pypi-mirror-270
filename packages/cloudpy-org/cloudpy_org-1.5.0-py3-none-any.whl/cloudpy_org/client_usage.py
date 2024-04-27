from cloudpy_org import aws_framework_manager_client
import os
class cloudpy_org_aws_framework_client:
    def __init__(self,aws_namespace:str,env:str='dev',region:str="us-east-2",token_path:str=None):
        self.aws_namespace = aws_namespace
        self.sufix = env
        self.region = region
        self.token_path = token_path
        self.current_path = os.getcwd() + '/'
        if self.token_path == None:
            self.token_path = self.current_path + aws_namespace + '.txt'
        self.aws = None
        self.errors = {}
        self.errors[1] = 'Invalid service token.'
        self.errors[2] = 'No aws framework client has been initialized yet.'
        self.errors[3] = 'Provided data format cannot be converted to json.'
        
        self.aws_framework()
    def get_full_path(self,relative_path:str):
        relative_path = relative_path.replace('\\','/').replace('//','/').replace('//','')
        l = len(relative_path)
        if relative_path[l-1:l] == '/':
            relative_path = relative_path[0:l-1]
            l = len(relative_path)
        if relative_path[0:1] == '/':
            relative_path = relative_path[1:l]
        return self.s3_root_path + relative_path + '/'
        
    def aws_framework(self):
        try:
            with open(self.token_path, 'r') as f:
                self.aws = aws_framework_manager_client(service_token=f.read(),aws_namespace=self.aws_namespace)
            self.bucket_name = self.aws.get_bucket_name(self.sufix,self.region)
            self.s3_root_path = 's3://' + self.bucket_name + '/'
        except:
            print(self.errors[1])
    
    def get_s3_file_content(self,file_name:str,relative_path:str):
        if self.aws != None:
            file_name,ext = self.__treat_file_name(file_name)
            s3FullFolderPath = self.get_full_path(relative_path)
            rslt = None
            if ext == 'json':
                try:
                    rslt = self.aws.ypt.get_s3_file_content(referenceName=file_name,s3FullFolderPath=s3FullFolderPath,exceptionCase=False)
                except:
                    try:
                        rslt = self.aws.ypt.get_s3_file_content(referenceName=file_name,s3FullFolderPath=s3FullFolderPath,exceptionCase=True)
                    except Exception as e:
                        print(str(e))
            else:
                rslt = self.aws.ypt.get_s3_file_content(referenceName=file_name,s3FullFolderPath=s3FullFolderPath,exceptionCase=True)
            return rslt
        else:
            print(self.errors[2])
            return None
    def __treat_file_name(self,file_name:str):
        file_name = file_name.lower()\
        .replace('  ',' ')\
        .replace('  ',' ')\
        .replace('  ','')\
        .replace(' ','_')\
        .replace('__','_')\
        .replace('__','_')\
        .replace('__','')
        ext = file_name[::-1].split('.')[0][::-1]
        file_name = file_name.replace('.' + file_name[::-1].split('.')[0][::-1],'') + '.' + ext
        return file_name,ext
        
    def write_in_s3_folder(self,data:object,file_name:str,relative_path:str):
        if self.aws != None:
            file_name,ext = self.__treat_file_name(file_name)
            s3FullFolderPath = self.get_full_path(relative_path)
            if ext == 'txt':
                if type(data) != str:
                    data = str(data)
                self.aws.ypt.store_str_as_file_in_s3_folder(
                    strInput=data
                    ,fileName=file_name
                    ,s3FullFolderPath=s3FullFolderPath
                    ,region_name=self.region
                    ,print_res=True)
            elif ext == 'json':
                cont = True
                if type(data) != dict:
                    data = str(data)
                    try:
                        data = self.aws.dictstr_to_dict(data)
                    except:
                        cont = False
                        print(self.errors[3])
                if cont:
                    try:
                        self.aws.ypt.standard_dict_to_json(jsonOrDictionary=data,fileName=file_name,folderPath=s3FullFolderPath)
                    except Exception as e:
                        print(str(e))
        else:
            print(self.errors[2])
    
    