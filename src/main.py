from utils.Worker import FileWorker, DirectoryWorker

#worker = FileWorker('./test/t1.txt','./men')
#print(worker.compress())

worker2 = DirectoryWorker('./output_directory/test/', './original/')
print(worker2.decompress())