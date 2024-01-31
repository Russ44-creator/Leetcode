import typing

#Click `Run` in the top left corner to run the command line program. Output will appear in the "Program Output" tab in the right pane.

class FileSystem:
    
    def __init__(self):
        self.file_system = {}
        self.id_manage = {0: [2, "MyDocuments", "MyDocuments"]}
        self.dashboard_count = 0
        self.worksheat_count = 0
        self.dashboard_system = {}
        self.worksheat_system = {}
        self.file_system["MyDocuments"] = {}
        self.id_relation = {0: set()}
        self.id = 0
    
    # Feel free to modify the parameter/return types of these functions
    # as you see fit. Please add comments to indicate your changes with a 
    # brief explanation. We care more about your thought process than your
    # adherence to a rigid structure.
    
    def get_total_dashboards(self) -> int:
      # TODO: implement
        return self.dashboard_count
    
    def get_total_worksheets(self) -> int:
      # TODO: implement
        return self.worksheat_count
    
    def add_new_file(self, fileName: str, fileType: str, folderId: int) -> None:
      # TODO: implement
        path = self.id_manage[folderId][1].split("/")
        new_id = self.generate_id()
        
        now_folder = self.file_system
        for p in path:
            now_folder = now_folder[p]
        if fileType == "worksheet":
        # worksheet: 0
            now_folder[fileName] = 0
            file_type = 0
            self.worksheat_count += 1
            self.id_relation[folderId].add(new_id)
        elif fileType == "dashboard":
        # dashboard: 1
            now_folder[fileName] = 1
            file_type = 1
            self.dashboard_count += 1
            self.id_relation[folderId].add(new_id)
        # folder: 3
        else:
        # new folder
            file_type = 2
            now_folder[fileName] = {}
            self.id_relation[new_id] = set()
            self.id_relation[folderId].add(new_id)
        print(self.file_system)
        new_path = self.id_manage[folderId][1] + "/" + fileName
        self.id_manage[new_id] = [file_type, new_path, fileName]
        # print(self.file_system)
        return

    
    def get_file_id(self, fileName: str, folderId: int) -> int:
      # TODO: implement
        if folderId == None:
            return 0
        path = self.id_manage[folderId][1] + "/" + fileName
        for key, value in self.id_manage.items():
            if value[1] == path:
                return key

    
    def move_file(self, fileId: int, newFolderId: int) -> None:
      # TODO: implement
        path = self.id_manage[fileId][1].split("/")
        # move document
        if self.id_manage[fileId][0] != 2:
            now_folder = self.file_system
            for p in path[:(len(path) - 1)]:
                now_folder = now_folder[p]
            filename = path[-1]
            file_type = now_folder[filename]
            del now_folder[filename]
            new_path = self.id_manage[newFolderId][1].split("/")
            new_folder = self.file_system
            for p in new_path:
                new_folder = new_folder[p]
            new_folder[filename] = file_type
            self.id_manage[fileId] = [file_type, self.id_manage[newFolderId][1] + "/" + filename, filename]

        # move folder
        else:
            now_folder = self.file_system
            path_len = len(self.id_manage[fileId][1])
            for p in path[:(len(path) - 1)]:
                now_folder = now_folder[p]
            foldername = path[-1]
            folder_content = now_folder[foldername]
            del now_folder[foldername] 
            new_path = self.id_manage[newFolderId][1].split("/")
            new_folder = self.file_system
            for p in new_path:
                new_folder = new_folder[p]
            new_folder[foldername] = folder_content
            self.id_manage[fileId] = [2, self.id_manage[newFolderId][1] + "/" + foldername, foldername]
            new_path_str = self.id_manage[newFolderId][1] + "/" + foldername
            self.move_id(fileId, new_path_str, path_len)
        return 

    # helper function to change id_manage        
    def move_id(self, folderId, new_path_str, path_len):
        for item in self.id_relation[folderId]:
            if self.id_manage[item][0] != 2:
                old_path = self.id_manage[item][1][path_len:]
                self.id_manage[item][1] = new_path_str + old_path
            else:
                self.move_id(item, new_path_str, path_len)
    
    def get_files(self, folderId: int) -> typing.List[str]:
      # TODO: implement
        path = self.id_manage[folderId][1].split("/")
        now_folder = self.file_system
        for p in path:
            now_folder = now_folder[p]
        ans = []
        for key in now_folder:
            ans.append(key)
        return ans
    

    def print_files(self) -> None:
      # TODO: implement
        for key, value in self.id_manage.items():
            if key != 0:
                print(value[2])

        return
    
    def generate_id(self):
        self.id += 2
        return self.id

    
    
# /////////////////////////////////////////////////////////
# // YOU DO NOT NEED TO MAKE CHANGES BELOW UNLESS NECESSARY
# /////////////////////////////////////////////////////////
    
# PLEASE ENSURE run_example() RUNS BEFORE SUBMITTING.
def run_example():
    fs = FileSystem()
    
    rootId = fs.get_file_id("MyDocuments", None)
    fs.add_new_file("draft", "folder", rootId)
    fs.add_new_file("complete", "folder", rootId)
    draftId = fs.get_file_id("draft", rootId)
    completeId = fs.get_file_id("complete", rootId)
    fs.add_new_file("foo", "worksheet", draftId)
    fs.add_new_file("bar", "dashboard", completeId)
    fooId = fs.get_file_id("foo", draftId)
    fs.move_file(fooId, completeId)

    print(", ".join(fs.get_files(rootId)))
    print(", ".join(fs.get_files(draftId)))
    print(", ".join(fs.get_files(completeId)))
          
    fs.add_new_file("project", "folder", draftId)
    projectId = fs.get_file_id("project", draftId)
    for filename in ["page1", "page2", "page3"]:
        fs.add_new_file(filename, "worksheet", projectId)
    fs.add_new_file("cover", "dashboard", projectId)
    fs.move_file(projectId, completeId)
    projectId = fs.get_file_id("project", completeId)
    coverId = fs.get_file_id("cover", projectId)
    fs.move_file(coverId, rootId)
    
    print(", ".join(fs.get_files(rootId)))
    print(", ".join(fs.get_files(draftId)))
    print(", ".join(fs.get_files(completeId)))
    print(", ".join(fs.get_files(projectId)))

    print(fs.get_total_dashboards())
    print(fs.get_total_worksheets())
    fs.print_files()

def ask_for_int(question: str) -> int:
    val = input(question)
    try:
        return int(val)
    except:
        print('Please enter a valid integer value\n')
        return ask_for_int(question)
    
def ask_question():
    fs = FileSystem()
    running = True
    while(running):
        command = ask_for_int("\nEnter an integer to indicate a command: \n[1] get_total_dashboards\n[2] get_total_worksheets\n[3] add_new_file\n[4] get_file_id\n[5] move_file\n[6] get_files \n[7] print_files\n[8] exit\n")
        if command == 1:
            totalDashboards = fs.get_total_dashboards()
            print("There are {0} dashboards in the file system.".format(totalDashboards));
        elif command == 2:
            totalWorksheets = fs.get_total_worksheets()
            print("There are {0} worksheets in the file system.".format(totalWorksheets));
        elif command == 3:
            fileName = input("Enter a new file name: ")
            fileType = input("Enter a file type (worksheet, dashboard, or folder): ")
            folderId = ask_for_int("Enter a folder id where you'd like to put this file: ")
            fs.add_new_file(fileName, fileType, folderId);
            print("{0} has been added to folder {1}".format(fileName, folderId))
        elif command == 4:
            fileName = input("Enter the file name: ")
            folderId = ask_for_int("Enter the folder id: ")
            fileId = fs.get_file_id(fileName, folderId)
            print("{0} is file {1}".format(fileName, fileId));
        elif command == 5:
            fileId = ask_for_int("Enter a file id:")
            newFileId = ask_for_int("Enter the folder id where you'd like to move this file: ")
            fs.move_file(fileId, newFileId);
            print("Successfully moved file {0} to folder {1}".format(fileId, newFileId))
        elif command == 6:
            folderId = ask_for_int("Enter a folderId:")
            fileNames = fs.get_files(folderId)
            if (len(fileNames) == 0):
                print("There are no files in folder {0}".format(folderId))
            else:
                print("The following files are in folder {0}: ".format(folderId))
                for fileName in fileNames:
                    print("\t{0}".format(fileName))
        elif command == 7:
            fs.print_files()
        elif command == 8:
            print("Exiting program.")
            running = False
        else:
            print("Invalid command: {0}. Please try again.\n".format(command))
              
print('run_example output:')
run_example()
print('ask_question output:')
# ask_question()
