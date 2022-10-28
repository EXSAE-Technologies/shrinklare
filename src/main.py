from utils.Worker import FileWorker, DirectoryWorker
import sys

#worker = FileWorker('./test/t1.txt','./men')
#print(worker.compress())

#worker2 = DirectoryWorker('./output_directory/test/', './original/')
#print(worker2.decompress())

def main():
    if len(sys.argv) == 4:
        worker = FileWorker(sys.argv[2],sys.argv[3])
        if sys.argv[1] == "-c":
            try:
                print("Compressing...")
                worker.compress()
            except Exception as e:
                print(e)
            else:
                print("Done!")
        elif sys.argv[1] == "-d":
            try:
                print("Decompressing...")
                worker.decompress()
            except Exception as e:
                print(e)
            else:
                print("Done!")
        else:
            print("Invalid command option")
            print("shrinklare <-c|-d> <souce_file> <destination_directory>")
    else:
        print("shrinklare <-c|-d> <souce_file> <destination_directory>")
    
main()