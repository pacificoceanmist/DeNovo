import sys
import os

baseCommand = "java -jar /home/sj-won/sra_data/Trimmomatic-0.39/trimmomatic-0.39.jar PE -phred33"
baseParamter = "ILLUMINACLIP:/home/sj-won/sra_data/Trimmomatic-0.39/adapters/TruSeq3-PE.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36"
fileBaseName = "SRR"
extName = ".fastq"



for i in range(1,len(sys.argv)):
    accessionName = sys.argv[i]

    inputFile1 = fileBaseName + accessionName + "_1" + extName
    inputFile2 = fileBaseName + accessionName + "_2" + extName

    outputPFile1 = fileBaseName + accessionName + "_1_P" + extName
    outputUPFile1 = fileBaseName + accessionName + "_1_UP" + extName
    outputPFile2 = fileBaseName + accessionName + "_2_P" + extName
    outputUPFile2 = fileBaseName + accessionName + "_2_UP" + extName


    fetchCommand = baseCommand + " " + inputFile1 + " " + inputFile2 + " " + outputPFile1 + " " + outputUPFile1 + " " + outputPFile2 + " " + outputUPFile2 + " "  + baseParamter

    os.system(fetchCommand)
