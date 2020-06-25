
# Python supports mutli dimensional array as listoflist
# there are 2 array from 2 files -  we will call them arrayA and arrayB we will then do
# arrayA * arrayB


def testifLengthis0(valueFoundWithoutJ):
    """This method tests if a parameter is of zero length - say we have had a complex number writeen like j 
    or it has bene written 2j - need to return the size -  in this caes 1 or 2 for the imaginary part

    Parameters
    ----------
    valueFoundWithoutJ : int
  
    Returns
    -------
    int
        size of the imaginary part
    """
    if len(valueFoundWithoutJ) == 0:
        return 1
    else:
        return valueFoundWithoutJ  

    
def cleanJandNewline(inString):
    """This remove the imaginary part indicator - j etc and removes any newlines.
    Method then calls a supporting method to get the size of the imaginary part

    Parameters
    ----------
    valueFoundWithoutJ : int
  
    Returns
    -------
    int
        size of the imaginary part
    """
    valueFoundWithoutJ = inString.replace('j','')
    valueFoundWithoutJornewline = valueFoundWithoutJ.replace('\n','')
    imagPartSizeAsString = testifLengthis0(valueFoundWithoutJornewline)
    return imagPartSizeAsString

def loadFileToMultiDimensionalArray(infile):
    """This mthod loads a file and then parses through the file and creates multi dimensional arrays

    Parameters
    ----------
    The file with the complex numbers : file
  
    No strict multi dimenaionsla arrays in basic python

    Returns
    -------
    list of list of complex numbers
    """
    with open(infile,'r') as openedfile:
        listofListofComplexNumbers = list()
        for line in openedfile:
            print(line)
            listofComplexNumbersFromLine = list()
            listofComplexNumber = line.split(" ")
            for complexnumberString in listofComplexNumber:
                # we now have to split this up
                if complexnumberString.find("+") > 0 : # 2 parts - imaginary part has a positive co-efficient
                    listofPartsofComplexNumber = complexnumberString.split("+")
                    realpart = listofPartsofComplexNumber[0]
                    imagPartSizeAsString = cleanJandNewline(listofPartsofComplexNumber[1])
                    complexVal = complex(int(realpart),int(imagPartSizeAsString))
                elif complexnumberString.find("-") > 0: # 2 parts - imaginary part has a negative co-efficient
                    listofPartsofComplexNumber = complexnumberString.split("-")
                    realpart = listofPartsofComplexNumber[0]
                    imagPartSizeAsString = cleanJandNewline(listofPartsofComplexNumber[1])
                    #valueFoundWithoutJ = listofPartsofComplexNumber[1].replace('j','')
                    #imagPartSizeAsString = testifLengthis0(valueFoundWithoutJ) 
                    complexVal = complex(int(realpart),int(imagPartSizeAsString) * -1)
                # no plus or minus symbol
                elif complexnumberString.find("j") > 0: # 1 part -  imaginary only
                    #valueFoundWithoutJ = complexnumberString.replace('j','')
                    imagPartSizeAsString = cleanJandNewline(complexnumberString)
                    complexVal = complex(0,int(imagPartSizeAsString))
                else: # no imaginary part
                    complexVal = complex(int(complexnumberString),0)
                listofComplexNumbersFromLine.append(complexVal)
            listofListofComplexNumbers.append(listofComplexNumbersFromLine)

    print(listofListofComplexNumbers)

    openedfile.close()

    return listofListofComplexNumbers



def calculateOutputArrayandWriteToFile(inlistofListofComplexNumbersArrayA, inlistofListofComplexNumbersArrayB):
    outF = open("myOutFile.txt", "w")
    """This method takes 2 multidiamtional arrays (as list of list of complex numbers) 
    and then iterates through them and writes result lines an output file

    Parameters
    ----------
    The file with the complex numbers : file
  
    No strict multi dimensional arrays in basic python

    Returns
    -------
    Nothing -  will have written to file
    """
    #print(len(inlistofListofComplexNumbersArrayA))
    #print(len(inlistofListofComplexNumbersArrayB))
    heigthof1stArray = len(inlistofListofComplexNumbersArrayA)
    widthof1stArray = len(inlistofListofComplexNumbersArrayA[0])
    #heigthof2ndArray = len(inlistofListofComplexNumbersArrayB)
    widthof2ndArray = len(inlistofListofComplexNumbersArrayB[0])
    #print("heigthOf1stArray"  + str(heigthof1stArray))
    #print("widthof1stArray" + str(widthof1stArray))
    #print("heigthOf2ndArray"  + str(heigthof2ndArray))
    #print("widthof2ndArray" + str(widthof2ndArray))

    for i in range(0,heigthof1stArray):
        resultrow = ""
        for j in range(0,widthof2ndArray):
            #listofcomplexinArow = listofListofComplexNumbersArrayA[i]
            complexValCalculated = complex(0,0)
            for k in range(0,widthof1stArray):
                complexInA = inlistofListofComplexNumbersArrayA[i][k]
                complexInB = inlistofListofComplexNumbersArrayB[k][j]
                #print("Gonna multiply")
                #print(complexInA)
                #print(complexInB)
                complexFound =   complexInA * complexInB
                complexValCalculated = complexValCalculated + complexFound
            #print("result" + str(complexValCalculated))
            resultrow = resultrow + " " + str(complexValCalculated)
        #print("result row " + resultrow)
        outF.write(resultrow)
        outF.write("\n")

def main():
    """This main method 
     - Will load a list of compelx number for the first array - into a list of lists
     - Will load a list of compelx number for the 2nd array - into a list of lists
     - Call a method to do the multiplication 

    Parameters
    ----------
    None
  
    No strict multi dimensional arrays in basic python

    Returns
    -------
    list of list of complex numbers
    """
    listofListofComplexNumbersArrayA = loadFileToMultiDimensionalArray("inputValuesArrayA.txt")
    listofListofComplexNumbersArrayB = loadFileToMultiDimensionalArray("inputValuesArrayB.txt")
    calculateOutputArrayandWriteToFile(listofListofComplexNumbersArrayA,listofListofComplexNumbersArrayB)

if __name__ == "__main__":
    main()