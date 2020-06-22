
class Person:

    def __init__(self):
        #Configurable parameters
        self.dnaLetters=('A','T','C','G')
        self.dnaMaxSeq=4
        self.dnaMaxRepetionsToBeMutant=2
        #General errors dictionary
        self.errors = (
            'No se recibió array de DNA',
            'Los elementos recibidos del array no construyen una matrix NxN',
            'Matriz vacía',
            'Error no controlado',
            'La matriz enviada no tiene los caracteres obligatorios'
        )

    #Functions section

    def checkMatrixFormat(self,dna):
        #not null
        if(dna is None):
            print(self.errors[0])
            return "0"
        #Has elements
        if(len(dna)==0):
            print(self.errors[2])
            return "2"
        #all elements same len
        firstElementLen=len(dna[0])
        if(any(len(e) != firstElementLen for e in dna) or firstElementLen!=len(dna)):
            print(self.errors[1])
            return "1"    
        return None

    def getNextPositionInX(self,typePath,posX):
        if(typePath=='V'):
            return posX+1
        elif(typePath=='H'):
            return posX
        elif(typePath=='OF'):
            return posX+1
        elif(typePath=='OB'):
            return posX+1

    def getNextPositionInY(self,typePath,posY):
        if(typePath=='V'):
            return posY
        elif(typePath=='H'):
            return posY+1
        elif(typePath=='OF'):
            return posY+1
        elif(typePath=='OB'):
            return posY-1

    def checkPositions(self,posX,posY,letter,dna,recursive,typePath):
        #Get next position
        nextX=self.getNextPositionInX(typePath,posX)
        nextY=self.getNextPositionInY(typePath,posY)
        #check limits matrix
        if(nextX<len(dna) and nextY<len(dna[posX]) and nextY>=0):
            #get row
            row=dna[nextX]
            #check letter
            if(row[nextY]==letter):
                recursive+=1
                if(recursive==self.dnaMaxSeq):
                    return True
                else:
                    return self.checkPositions(nextX,nextY,letter,dna,recursive,typePath)
            else:
                return False
        else:
            return False

    #Detect mutant function
    def isMutant(self,dna):
        try:
            #check correct matrix format
            checkResult=self.checkMatrixFormat(dna)
            if(checkResult is not None):
                return False
            #Search dna mutant
            firstElementLen=len(dna[0])
            contx=0
            contRepeats=0
            for elementX in dna:
                conty=0
                for elementY in elementX:
                    #check correct letter
                    if(all(e != elementY for e in self.dnaLetters)):
                        print(self.errors[4])
                        return False
                    #Check path in all directios
                    if(self.checkPositions(contx,conty,elementY,dna,1,'V')):
                        contRepeats+=1
                    if(self.checkPositions(contx,conty,elementY,dna,1,'H')):
                        contRepeats+=1
                    if(self.checkPositions(contx,conty,elementY,dna,1,'OF')):
                        contRepeats+=1
                    if(self.checkPositions(contx,conty,elementY,dna,1,'OB')):
                        contRepeats+=1
                    conty+=1
                contx+=1
            print(contRepeats)
            if(contRepeats>=self.dnaMaxRepetionsToBeMutant):
                return True
            else:
                return False
        except:
            #AGREGADO DE LOGS CORRESPONDIENTE, NO LO AGREGUÉ PARA SIMPLIFICAR
            print(self.errors[3])
            return False
