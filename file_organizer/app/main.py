import os
import shutil

#folder to organize
folder_path=input("Enter Folder Path: ")
os.makedirs(folder_path,exist_ok=True)
#file-type mapping
file_types={
    "Images":[".png",".jpg",".jpeg"],
    "Documents":[".pdf",".txt",".json"],
    "Audio":[".mp3",".wav"],
    "Videos":[".mp4",".mkv"]
}



#loop through files
for file in os.listdir(folder_path):

    file_path=os.path.join(folder_path,file)

    #avoid unecessary folders
    if os.path.isdir(file_path):
        continue

    #extenstion split process
    file_name,ext=os.path.splitext(file)
    print(file_name,"->",ext)

    matched=False
    for folder,extenstion in file_types.items():
        if ext.lower() in extenstion: 
            matched=True
            
            #create folder 
            dest_folder=os.path.join(folder_path,folder)
            os.makedirs(dest_folder,exist_ok=True)
            break

    #if extenstion is out of file_types
    if not matched:
        dest_folder=os.path.join(folder_path,"Others")
        os.makedirs(dest_folder,exist_ok=True)

    #duplicate handling
    dest_path=os.path.join(dest_folder,file)
    if os.path.exists(dest_path):
        counter=1
        while os.path.exists(dest_path):
            new_name=f"{file_name}_{counter}{ext}"
            dest_path=os.path.join(dest_folder,new_name)
            counter+=1

    shutil.move(file_path,dest_path)
