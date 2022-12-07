import os
from PIL import Image
from fpdf import FPDF
file_location = r"/home/r0h8n/Desktop/Python/sulav_test/output"
def get_pdf():
    pdf = FPDF()
    w,h = 0,0
    os.chdir(file_location)
    ls = os.listdir(file_location)
    i = 0
    for im in ls:
        if im.endswith(".JPG") or im.endswith(".png") or im.endswith(".jpg"): 
            if i == 0:
                cover = Image.open(im)
                w,h = cover.size
                pdf = FPDF(unit = "pt", format = [w,h])
            image = im
            pdf.add_page()
            pdf.image(image,0,0,w,h)
        i+=1
    pdf.output("output.pdf","F")

def delete_files():
    os.chdir(file_location)
    rm_fl = os.listdir()
    for files in rm_fl:
        os.remove(files)

def get_basic():
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


