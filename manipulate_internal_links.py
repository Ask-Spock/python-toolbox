"""

what this moudlue should do:

1.run on all html file in the folder.
2.if it is an html file open it.
3.search  inside the file that open and replace "file_name" -> "file_name.html"


"""

"""

what this moudlue should do:

1 :run on all html file in the folder.

2 :on each filae in the folder open the file.

2.1 : call the function  with all the file in a list of files in the folder so it will add .html   to there ending.

3.move to the next file in the list and do the same.


"""

"""
--------change_links_inside_file-------

function input :

1.file name to work on.
2.string to search.
3.string to replace.


function output:
1.function will change ALL  occourance of the string in the file.


"""
def change_links_inside_file(file_name,origan_string,new_string):
    # read input file
    fin = open(file_name, "rt")
    # read file contents to string
    data = fin.read()
    # replace all occurrences of the required string
    #data = data.replace(file_name, file_name+".html")
    data = data.replace(origan_string,new_string)
    
    # close the input file
    fin.close()
    #open the input file in write mode
    fin = open(file_name, "wt")
    #overrite the input file with the resulting data
    fin.write(data)
    #close the file
    fin.close()
    print("change_links_inside_file activated on in {}.\n\n\n".format(file_name))

def Run_on_all_files_in_folder():
    pass


if __name__ == "__main__":

    

    
    import glob, os
    #os.chdir(".")
    for files in glob.glob("*.html"):
        for file in glob.glob("*.html"):
            print("working on {} \n".format(files))
            #this is the .html string
            base_string = str(file)
        
            enterded_string = "href=\'" + base_string + "\'"
            print("The string that will be insert: {} \n".format(enterded_string))

            #this is the sting i need to search
            searched_string = "href=\""+ base_string.replace(".html","") +'\"'
            print("The string that we are searching: {} \n".format(searched_string))

            #print(original + "\n")
            #print("The string that will be replaced")
            #change_links_inside_file(file)
            
            
            
            change_links_inside_file(files, searched_string, enterded_string)

    
