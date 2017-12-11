# !/usr/bin/env python3
#  -*- coding: utf-8 -*-
# title           :mods.py
# description     :reading ladi_ocr.txt and ladi_nlp.txt output and writes it to mods compliant .xml file
# author          :Vivek Khetan
# date            :12112017
# version         :0.1
# usage           :python mods.py <path_to_ladi_ocr_result_text_file> <path_to_ladi_nlp_result_text>
# python_version  :3.6.3
# ==============================================================================


# Import the modules needed to run the script.
import sys

def mods_output():
	""" reads the ladi_ocr_result_text_file and ladi_nlp_result_text_file
		write the content in mods compliance format in a .xml file
	"""
	output_file_name = sys.argv[1].split('/')[1]
	ocr_output = open(sys.argv[1]).read()
	output_file = open("./results/"+ output_file_name + "/" +output_file_name + "_mods_output.xml", "wb")

	try:
		output_file.write('<note type="content" displayLabel="Transcription" lang="spa">\n')
		output_file.write(ocr_output.strip('\n'))
		output_file.write('</note>\n\n')
		nlp_output = open(sys.argv[2])
		for line in nlp_output:
			output_file.write('<subject lang="spa">\n')
			output_file.write('<topic>'+ line.strip('\n') + '</topic>\n\n')

	except KeyboardInterrupt:
		print('You cancelled the operation; bbye.')
	except ImportError:
		print("No module found, make sure you have required modules installed")
	except IOError:
		print("An error occurred trying to read the file.")
	except:
		print("something seems Strange; there is some error")
	
	output_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('You need to provide more arguments' + '\n' + " give path to ocr text result file and extracted ner result file" + "\n" " or --help for more help")
    elif sys.argv[1] == '--help':
        print('Input: Path for ocr and ner .txt file'+ '\n' + "output: .xml file in mods compliance format")
    elif sys.argv[1] =="--h":
        print('Input: Path for ocr and ner .txt file'+ '\n' + "output: .xml file in mods compliance format")
    elif sys.argv[1] == '--version':
        print(" mods_vision.py 0.1")

    else:
        mods_output()











