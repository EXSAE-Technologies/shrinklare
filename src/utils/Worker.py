import lzma, os

class FileWorker:
    def __init__(self,file_input:str,output_directory:str):
        self._fin = file_input #what if it does not exist
        self._fout = file_input.split('/')[-1]
        self._dout = os.path.abspath(output_directory)
    
    def _get_output_dir(self):
        try:
            os.mkdir(self._dout)
        except Exception as e:
            print(e)
        
        return self._dout
    
    def compress(self):
        dout = self._get_output_dir()
        path_out = os.path.join(dout,self._fout)
        with open(self._fin,'rb') as inread, open(path_out,mode='wb') as outwrite:
            data = inread.read()
            print('compressing',self._fin)
            compresseddata = lzma.compress(data)
            outwrite.write(compresseddata)
        return path_out
    
    def decompress(self):
        dout = self._get_output_dir()
        path_out = os.path.join(dout,self._fout)
        with open(self._fin,'rb') as inread, open(path_out,mode='wb') as outwrite:
            print('decompressing',self._fin)
            data = lzma.decompress(inread.read())
            outwrite.write(data)
        return path_out

class DirectoryWorker:
    def __init__(self,input_directory:str,output_directory:str()):
        self._din = input_directory
        self._dout = os.path.abspath(output_directory)
    
    def _get_output_dir(self):
        try:
            os.mkdir(self._dout)
        except Exception as e:
            print(e)
        
        return self._dout
    
    def compress(self):
        dout = self._get_output_dir()
        len_dir_path = len(self._din)
        for root, _, files in os.walk(self._din):
            for file in files:
                file_path = os.path.join(root, file)
                w = FileWorker(file_path, os.path.join(dout,root))
                print(w.compress())
        return dout
