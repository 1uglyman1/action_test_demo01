import os


def traverse_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)


if __name__ == "__main__":
    try:
    os.system("git clone https://github.com/shmilylty/OneForAll.git")
  except:
    pass
  os.system("dir")
  os.system("dir")
  current_directory = os.getcwd()
  traverse_directory(current_directory)
  
