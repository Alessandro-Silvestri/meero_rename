#!/usr/bin/python3

'''
MEERO RENAME

Tool I built for renaming NEF files from a given text file list.
As I thought this tool for working with Meero Company
this is the file structure you have to follow:
Folder1 called as the restaurant name with inside
the NEF files, a text file name list and this script.
Inside the Folder1 there is a subfolder with inside the photos taken from the top
The renaming follow the alphabetical order

Made by Alessandro Silvestri © 2022 <alessandro.silvestri.work@gmail.com>

############## bugs to fix ################
Linux version
in LINUX doesn't work the rename
give the chance to avoid the hero pictures (OK DONE!)
check if in the text file there are repeated names
space in the hero picture names
asking the directory pat in the begining
###########################################

'''
import os

class MeeroRename:
    def __init__(self):
        self.checks()
        self.restaurant_name = str(os.getcwdb())[:-1].split('/')[-1].lower()               # restaurant name (from folder name)            
        self.list_txt = list(filter(lambda x: x.endswith('.txt'), os.listdir()))[0]         # list txt file name
        self.item_list_name = list(map(lambda x: x.lower(), self.reading_txt_file()))       # text file content (list) converted in lower case
        self.nef_files = list(filter(lambda x: x.endswith('.NEF'), os.listdir()))           # NEF files (list)

        # if a folder exists
        self.hero_exists = False
        if self.exist_hero_folder(os.listdir()):
            self.hero_exists = True
            self.dir_hero_name = list(filter(lambda x: '.' not in x, os.listdir()))[0] + '/'    # Hero directory name (list)   

    
        # cheking the text file matching with number of NEFs
        if not len(self.item_list_name) == len(self.nef_files):                             
            print("\nThe items number doesn't match with the NEF files\n")
            print("Program ended")
            quit()
        
        ######### DEBUG ############
        print(self.nef_files)
        print(self.item_list_name)
        quit()
        ######### DEBUG ############
    
    def exist_hero_folder(self, lista: list):
        '''boolean: check if a folder exists'''
        a = False
        for i in os.listdir(): # fix here (lista is not needed)
            if not '.' in i:
                a = True
                break
        return a

    def checks(self):
        '''Checking if the structure files is right'''
        count = 0
        nef_in = txt_in = False
        for i in os.listdir():
            if '.txt' in i: count += 1
            if not '.' in i: pass
            if '.NEF' in i: nef_in = True
            if '.txt' in i: txt_in = True          
        if count > 1: print('Error: there are more then 1 text file') / quit()
        if count == 0: print('Error: text file missing') / quit()
        if not nef_in: print('Error: files NEF missing') / quit()
        if not txt_in: print('Error: files text missing') / quit()

    def rename(self):
        '''Renaming the NEF files'''
        self.banner()
        print('Restaurant name:', self.restaurant_name)
        user_input = input('Do you want rename everything? (y/n): ')
        # user confermation before renaming
        if user_input.lower() == 'n':
            print('Bye')
            quit()
        elif user_input.lower() == 'y':
            pass
        else:
            print('\nWrong command, program ended\n')
            quit()


        # loop for renaming all the NEF files (not the hero ones)
        for i in range(len(self.item_list_name)):
            nef = self.nef_files[i]
            # new name expression (replacing the spaces with underscore)
            name = self.restaurant_name.replace(" ", "") + '_' + self.item_list_name[i] + ".NEF"


######### DEBUG ############
            print(nef, name)
            
            '''
            os.rename(nef, name)
            '''
######### DEBUG ############





        if self.hero_exists:
            self.rename_hero()

    def reading_txt_file(self):
        '''Returns the content (list) without the \n character and spaces'''
        with open(self.list_txt, 'r') as f:
            items = list(f.readlines())
        content = list(map(lambda x: x.replace("\n", "").replace(' ', ''), items))
        return content

    def rename_hero(self):
        '''rename the files in the directory (any directory name) and put them outside'''
        hero_list = os.listdir(self.dir_hero_name)       # list with the hero names
        for i in range(len(hero_list)):
            hero_name = hero_list[i]
            hero_name_path = self.dir_hero_name + hero_name
            hero_name_new = self.restaurant_name + '_hero' + str(i+1) + '.NEF'
            os.rename(hero_name_path, hero_name_new)
    
    def banner(self):
        print('''
                                               
 _____ ___ ___ ___ ___    ___ ___ ___ ___ _____ ___ 
|     | -_| -_|  _| . |  |  _| -_|   | .'|     | -_|
|_|_|_|___|___|_| |___|  |_| |___|_|_|__,|_|_|_|___|

Make a backup files just in case

''')

a = MeeroRename()
a.rename()

