import os
import function



os.system("cls||clear")
print(" *******            **                        ".center(100))
print("/**////**          /**                        ".center(100))
print("/**   /**   ****** /**       ******   ******* ".center(100))
print("/*******   **////**/******  //////** //**///**".center(100))
print("/**///**  /**   /**/**///**  *******  /**  /**".center(100))
print("/**  //** /**   /**/**  /** **////**  /**  /**".center(100))
print("/**   //**//****** /**  /**//******** ***  /**".center(100))
print("//     //  //////  //   //  //////// ///   ///".center(100)) 
print("\n"+"::Welcome To Converter::".center(100))
print("Choose Your Request:".center(100))
print('''
            1) Convert PDF
            2) Delete Folders
            3) Upload to Drive (comming soon)
            4) Exit    
    ''')

while True:
    inp = int(input("Enter your Choice::"))

    if inp == 1:
        function.get_pdf()
        out = 0
    elif inp == 2:
        function.delete_files()
        out = 0
    elif inp == 3:
        out = "comming soon"
    elif inp == 4:

        os.system("cls||clear")
        break
    else:
        out = "Not Valid"
       
    os.system("cls||clear")
    function.get_basic()
    if out != 0:
        print(out)
    

    