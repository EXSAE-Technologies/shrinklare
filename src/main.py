from utils.Worker import FileWorker, DirectoryWorker

#worker = FileWorker('./test/t1.txt','./men')
#print(worker.compress())

worker = DirectoryWorker('./test', './output_directory/')
print(worker.compress())