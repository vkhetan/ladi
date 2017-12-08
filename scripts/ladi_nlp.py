import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def language_analysis():
    """
    reads the .txt file from the provided path in command line
    uses google language api to extract and print  "person", "organization" and "location"  name  entity from provided text file
    """
    # must  have language api activated for this to work
    from google.cloud import language # importing google cloud natural language api
    try:
        file_path = sys.argv[1]
        text_file = open(file_path)
        text_content = text_file.read()
        language_client = language.Client() # calling client to make language api call
        client_text_content = language_client.document_from_text(text_content)

        recognized_entities = client_text_content.analyze_entities()

        #recognized_entities = processed_text.entities()
        extracted_entities = recognized_entities.entities
        for entity in extracted_entities:
            if entity.entity_type in ["PERSON", "ORGANIZATION", "LOCATION"]:
                print(entity.name)
    except KeyboardInterrupt:
        print("You cancelled the operation; Bbye.")
    except ImportError:
        print("No module found, make sure you have required modules installed")
    except IOError:
        print("An error orrured trying to read the file")
    except:
        print("something seems Strange; there is some error")



if __name__ =='__main__':
    if len(sys.argv) < 2:
        print("You need to provide more arguments" + "\n" + "give some text file path as second argument to the script")
    elif sys.argv[1] == '--help':
        print('Input:Path for text file' + '\n' + 'Output:extracts and prints the named entities in the provided text file using google-language api')
    elif sys.argv[1] == '-h':
        print("Input:Path for text file' + '\n' + 'Output:extracts and prints the named entities in the provided text file using google-language api")
    elif sys.argv[1] == '--version':
        print("ladi_nlp.py 0.1")
    else:
        language_analysis()


