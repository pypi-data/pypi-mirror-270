__author__ = "Benoit CAYLA"
__email__ = "benoit@datacorner.fr"
__license__ = "MIT"

import argparse
from ragfmk.rag import rag
import ragfmk.utils.CONST as C
from ragfmk.elements.wrappers.document import document
import ragfmk.utils.FUNCTIONS as F 
from ragfmk.elements.wrappers.chunks import chunks

"""
    Chunks a text into several parts.
    output Format is JSON -> {'chunks': ['Transcript of ...', ...] }
    2 techniques can be used (option chunktype):
        1) Semantic chunking
        2) character chunking
    usage: RagChunkText [-h] 
                        [-chunktype {character,semantic}] 
                        -txt TXT 
                        -chunks {Chunks JSON file output} 
                        [-chunk_size {Chunk size for char chunking, def 500}]
                        [-chunk_overlap {Chunk overlap for char chunking, def 50}] 
                        [-sep {Chunk separator for char chunking, def .}]
"""

def main():
    parser = argparse.ArgumentParser()
    myRag = rag()
    try:
        parser.add_argument("-" + C.ARG_CHUNKTYPE[0], help=C.ARG_CHUNKTYPE[1], required=False, default=C.ARG_CHUNKTYPE_VALCHAR,
                            choices = [C.ARG_CHUNKTYPE_VALCHAR, C.ARG_CHUNKTYPE_VALSEM])
        parser.add_argument("-" + C.ARG_TXTFILE[0], help=C.ARG_TXTFILE[1], required=True)
        parser.add_argument("-" + C.ARG_CHUNKS[0], help=C.ARG_CHUNKS[1], required=True)
        parser.add_argument("-" + C.ARG_CHUNKSIZE[0], help=C.ARG_CHUNKSIZE[1], required=False, type=int, default=C.CHKS_DEFAULT_SIZE)
        parser.add_argument("-" + C.ARG_CHUNKOVAP[0], help=C.ARG_CHUNKOVAP[1], required=False, type=int, default=C.CHKS_DEFAULT_OVERLAP)
        parser.add_argument("-" + C.ARG_SEP[0], help=C.ARG_SEP[1], required=False, default=C.CHKS_DEFAULT_SEP)
        args = vars(parser.parse_args())
        myRag.setCLIArgs(args)

        # Read the Text file first
        doc = document()
        if not(doc.load(args[C.ARG_TXTFILE[0]])):
            raise Exception("Impossible to read the document content")

        # Document chunking
        if (args[C.ARG_CHUNKTYPE[0]] == C.ARG_CHUNKTYPE_VALCHAR):
            cks = myRag.charChunk(doc, args[C.ARG_SEP[0]], args[C.ARG_CHUNKSIZE[0]], args[C.ARG_CHUNKOVAP[0]])
        elif (args[C.ARG_CHUNKTYPE[0]] == C.ARG_CHUNKTYPE_VALSEM):
            cks = myRag.semChunk(doc)

        # Write the json in a file 
        cks.save(args[C.ARG_CHUNKS[0]])

        myRag.CLI_output(str(cks.size))

    except Exception as e:
        parser.print_help()
        myRag.CLI_output(C.OUT_ERROR, True, str(e))
        
if __name__ == "__main__":
    main()