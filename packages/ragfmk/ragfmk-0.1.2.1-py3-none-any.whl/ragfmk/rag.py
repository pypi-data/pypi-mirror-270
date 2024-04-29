__author__ = "Benoit CAYLA"
__email__ = "benoit@datacorner.fr"
__license__ = "MIT"

from ragfmk.elements.wrappers.document import document
from ragfmk.elements.llms.ollama import ollama
from ragfmk.elements.wrappers.prompt import prompt
from ragfmk.utils.milestone import milestone
from ragfmk.elements.embeddings.stEmbeddings import stEmbeddings
from ragfmk.elements.wrappers.chunks import chunks
import ragfmk.utils.CONST as C
from ragfmk.utils.log import log
import os

class rag():
    def __init__(self):
        self.__milestones = milestone()
        try:
            ragLogFileName = os.environ[C.RAGCLI_LOGFILE_ENV]
        except:
            ragLogFileName = C.TRACE_FILENAME
        self.__myLog = log(C.TRACE_LOGGER, ragLogFileName)
        self.__milestones.start()
        self.log.info("** START **")
        
    def setCLIArgs(self, args):
        self.__milestones.initialize(args)

    @property
    def milestones(self):
        return self.__milestones
    @property
    def log(self):
        return self.__myLog

    def addMilestone(self, name, description, *others):
        self.__milestones.add(name, description, others)
        self.log.info("Step {} -> {}".format(name, self.__CLI_fmtMsgForLog(description)))

    def __CLI_fmtMsgForLog(self, message, limit = C.TRACE_MSG_LENGTH):
        """ Format a message for logging
        Args:
            message (str): log message
            limit (int, optional): message max length. Defaults to C.TRACE_MSG_LENGTH.
        Returns:
            formatted message: _description_
        """
        logMsg = message.replace("\n", " ")
        dots = ""
        if (len(message) > limit):
            dots = " ..."
        logMsg = logMsg[:limit] + dots
        return logMsg
    
    def __CLI_buildOutput(self, response, error = False, errorMsg = C.NULLSTRING):
        """ Build the final output display of the process
        Args:
            response (str): final response
            error (bool, optional): has error ? Defaults to False.
            errorMsg (str, optional): error message. Defaults to C.NULLSTRING.
        Returns:
            str: JSON output with main milestones
            str: status
            str: final LLM response
        """
        try:
            outJson, outStatus, outResponse = "", "", ""
            self.__milestones.stop()
            outJson = self.milestones.getFullJSON()
            if (error):
                self.log.error("Output: Response> {} | Error> {}".format(self.__CLI_fmtMsgForLog(response), errorMsg))
                outStatus = C.OUT_ERROR
                outResponse = errorMsg
            else:
                self.log.info("Output: Response> {}".format(self.__CLI_fmtMsgForLog(response)))
                outStatus = C.OUT_SUCCESS
                outResponse = response
            self.log.info("** STOP **")
            return outJson, outStatus, outResponse
        except Exception as e:
            self.log.error(str(e))
            return outJson, outStatus, outResponse
            
    def CLI_output(self, response, error = False, errorMsg = C.NULLSTRING):
        """ Build the final output of the process for the CLI (Standard Output (CLI) printing via XML tags)
        Args:
            response (str): final response
            error (bool, optional): has error ? Defaults to False.
            errorMsg (str, optional): error message. Defaults to C.NULLSTRING.
        Returns:
            str: JSON output with main milestones
            str: status
            str: final LLM response
        """
        outJson, outStatus, outResponse = self.__CLI_buildOutput(response, error, errorMsg)
        print(C.TAG_O_LOG + outJson + C.TAG_C_LOG)
        print(C.TAG_O_STATUS + outStatus + C.TAG_C_STATUS)
        print(C.TAG_O_RESPONSE + outResponse + C.TAG_C_RESPONSE)

    def readTXT(self, txtfile) -> str:
        """ Reads a txt file
        Args:
            txtfile (str): text file path
        Returns:
            str: text read
        """
        try:
            # Read and parse a pdf file
            self.log.info("Read TXT file {} by using mode ...".format(txtfile))
            doc = document()
            doc.load(txtfile)
            if (len(doc.content) <= 0):
                raise Exception("Error while reading the TXT document")
            self.addMilestone("PDF2TXT", "TXT file successfully loaded. Text length : {}".format(len(doc.content)))
            self.log.info("TXT file loaded successfully")
            return doc
        except Exception as e:
            self.log.error("Error while reading the TXT file: {}".format(str(e)))
            return ""

    def readPDF(self, pdffile, method = C.ARG_READER_VALPYPDF) -> str:
        """ Reads a pdf file and converts it to Text
        Args:
            pdffile (str): pdf file path
            method (str, optional): Type of conversion. Defaults to C.ARG_READER_VALPYPDF.
        Returns:
            str: text converted
        """
        try:
            # Read and parse a pdf file
            self.log.info("Read PDF file {} by using mode {}...".format(pdffile, method))
            pdf = document()
            if (method == C.ARG_READER_VALPYPDF):
                pdf.pyMuPDFParseDocument(pdffile)
            else:
                pdf.llamaParseDocument(pdffile)
            if (len(pdf.content) <= 0):
                raise Exception("Error while converting the PDF document to text")
            self.addMilestone("PDF2TXT", "PDF converted to TEXT successfully. Text length : {}".format(len(pdf.content)))
            self.log.info("PDF file opened successfully")
            return pdf
        except Exception as e:
            self.log.error("Error while reading the PDF file: {}".format(str(e)))
            return ""
            
    def charChunk(self, doc, separator, chunk_size, chunk_overlap) -> chunks:
        """ Document character chunking process
        Args:
            doc (elements.document): Text / document to chunk
            separator (str): Chunks separator
            chunk_size (str): chunk size
            chunk_overlap (str): chunk overlap
        Returns:
            chunks: chunks object
        """
        try:
            self.log.info("Character Chunking document processing ...")
            cks =  doc.characterChunk(separator, chunk_size, chunk_overlap)
            if (cks == None):
                raise Exception("Error while chunking the document")
            self.addMilestone("CHUNKING","Document (character) chunked successfully, Number of chunks : {}".format(cks.size), cks.size)
            self.log.info("Document chunked successfully with {} chunks".format(cks.size))
            return cks
        except Exception as e:
            self.log.error("Error while chunking the document: {}".format(str(e)))
            return None

    def semChunk(self, doc) -> chunks:
        """ Document semantic chunking process
        Args:
            doc (elements.document): Text / document to chunk
        Returns:
            int: number of chunks
            list: List of chunks / JSON format -> {'chunks': ['Transcript of ...', ...] }
        """
        try:
            self.log.info("Semantic Chunking document processing ...")
            cks =  doc.semanticChunk()
            if (cks == None):
                raise Exception("Error while chunking the document")
            self.addMilestone("CHUNKING","Document (character) chunked successfully, Number of chunks : {}".format(cks.size), cks.size)
            self.log.info("Document chunked successfully with {} chunks".format(cks.size))
            return cks
        except Exception as e:
            self.log.error("Error while chunking the document: {}".format(str(e)))
            return None
        
    def buildPrompt(self, question, nr) -> str:
        """ Build smart prompt (for RAG)
        Args:
            question (str): initial question
            nr (nearest object): list of the nearest / most similar chunks
        Returns:
            str: new prompt
        """
        try:
            self.log.info("Building RAG prompt ...")
            myPrompt = prompt(question, nr)
            customPrompt = myPrompt.build()
            if (len(customPrompt) == 0):
                raise Exception("Error while creating the prompt")
            self.addMilestone("PROMPT", "Prompt built successfully", customPrompt)
            self.log.info("RAG Prompt created successfully")
            return customPrompt
        except Exception as e:
            self.log.error("Error while building the LLM prompt {}".format(str(e)))
            return ""

    def promptLLM(self, question, urlOllama, model, temperature):
        """ send a prompt to the LLM
        Args:
            question (str): prompt
            urlOllama (str): Ollama URL
            model (str): Ollama Model
            temperature (str): Ollama Model LLM Temperature
        Returns:
            str: LLM response
        """
        try:
            self.log.info("Send the prompt to the LLM ...")
            myllm = ollama(urlOllama, model, temperature)
            resp = myllm.prompt(question)
            self.addMilestone("LLMPT", "LLM Reponse\n {}\n".format(resp))
            self.log.info("Prompt managed successfully by the LLM.")
            return resp
        except Exception as e:
            self.log.error("Error while prompting the LLM {}".format(str(e)))
            return ""
    
    def createEmbeddings(self, cks) -> stEmbeddings:
        """ create embeddings for a list of chunks
        Args:
            cks (chunks): Chunks object
        Returns:
            json: data and embeddings
        """
        try:
            self.log.info("Create embeddings for list of texts/chunks ...")
            embds = stEmbeddings()
            if (not embds.create(cks)):
                raise Exception("Error while creating the chunks embeddings")
            self.addMilestone("DOCEMBEDDGS", "Embeddings created from chunks successfully")
            self.log.info("Chunks Embeddings created successfully")
            return embds
        except Exception as e:
            self.log.error("Error while creating the list of texts/chunks embeddings {}".format(str(e)))
            return None