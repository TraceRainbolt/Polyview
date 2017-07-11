/* Stuff to export relevant 'expat' entry points from pyexpat to other
 * parser modules, such as cElementTree. */

/* note: you must import expat.h before importing this module! */

#define PyExpat_CAPI_MAGIC  "pyexpat.expat_CAPI 1.0"
#define PyExpat_CAPSULE_NAME "pyexpat.expat_CAPI"

struct PyExpat_CAPI 
{
    char* magic; /* set to PyExpat_CAPI_MAGIC */
    int size; /* set to sizeof(struct PyExpat_CAPI***REMOVED*** */
    int MAJOR_VERSION;
    int MINOR_VERSION;
    int MICRO_VERSION;
    /* pointers to selected expat functions.  add new functions at
       the end, if needed */
    const XML_LChar * (*ErrorString***REMOVED***(enum XML_Error code***REMOVED***;
    enum XML_Error (*GetErrorCode***REMOVED***(XML_Parser parser***REMOVED***;
    XML_Size (*GetErrorColumnNumber***REMOVED***(XML_Parser parser***REMOVED***;
    XML_Size (*GetErrorLineNumber***REMOVED***(XML_Parser parser***REMOVED***;
    enum XML_Status (*Parse***REMOVED***(
        XML_Parser parser, const char *s, int len, int isFinal***REMOVED***;
    XML_Parser (*ParserCreate_MM***REMOVED***(
        const XML_Char *encoding, const XML_Memory_Handling_Suite *memsuite,
        const XML_Char *namespaceSeparator***REMOVED***;
    void (*ParserFree***REMOVED***(XML_Parser parser***REMOVED***;
    void (*SetCharacterDataHandler***REMOVED***(
        XML_Parser parser, XML_CharacterDataHandler handler***REMOVED***;
    void (*SetCommentHandler***REMOVED***(
        XML_Parser parser, XML_CommentHandler handler***REMOVED***;
    void (*SetDefaultHandlerExpand***REMOVED***(
        XML_Parser parser, XML_DefaultHandler handler***REMOVED***;
    void (*SetElementHandler***REMOVED***(
        XML_Parser parser, XML_StartElementHandler start,
        XML_EndElementHandler end***REMOVED***;
    void (*SetNamespaceDeclHandler***REMOVED***(
        XML_Parser parser, XML_StartNamespaceDeclHandler start,
        XML_EndNamespaceDeclHandler end***REMOVED***;
    void (*SetProcessingInstructionHandler***REMOVED***(
        XML_Parser parser, XML_ProcessingInstructionHandler handler***REMOVED***;
    void (*SetUnknownEncodingHandler***REMOVED***(
        XML_Parser parser, XML_UnknownEncodingHandler handler,
        void *encodingHandlerData***REMOVED***;
    void (*SetUserData***REMOVED***(XML_Parser parser, void *userData***REMOVED***;
    /* always add new stuff to the end! */
***REMOVED***;

