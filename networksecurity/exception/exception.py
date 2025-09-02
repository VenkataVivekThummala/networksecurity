import sys
from networksecurity.logging import loggger
class NetworkSecurityEXception(Exception):
    def error_message_detail(self,error_message,error_detail:sys):
        _,_,exc_tb=error_detail.exc_info()
        self.file_name=exc_tb.tb_frame.f_code.co_filename
        self.lineno=exc_tb.tb_lineno


    def __str__(self):
        return  "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(self.file_self.lineno,str(self.error_message))
        
    
if __name__=="__main__":
    try:
        loggger.logging.info("Enter the try block")
        a=1/0
        print("Ths will not printed",a)
    except Exception as e:
        raise NetworkSecurityEXception(e,sys)    
    


        