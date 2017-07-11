
/* Grammar interface */

#ifndef Py_GRAMMAR_H
#define Py_GRAMMAR_H
#ifdef __cplusplus
extern "C" {
#endif

#include "bitset.h" /* Sigh... */

/* A label of an arc */

typedef struct {
    int		 lb_type;
    char	*lb_str;
***REMOVED*** label;

#define EMPTY 0		/* Label number 0 is by definition the empty label */

/* A list of labels */

typedef struct {
    int		 ll_nlabels;
    label	*ll_label;
***REMOVED*** labellist;

/* An arc from one state to another */

typedef struct {
    short	a_lbl;		/* Label of this arc */
    short	a_arrow;	/* State where this arc goes to */
***REMOVED*** arc;

/* A state in a DFA */

typedef struct {
    int		 s_narcs;
    arc		*s_arc;		/* Array of arcs */
	
    /* Optional accelerators */
    int		 s_lower;	/* Lowest label index */
    int		 s_upper;	/* Highest label index */
    int		*s_accel;	/* Accelerator */
    int		 s_accept;	/* Nonzero for accepting state */
***REMOVED*** state;

/* A DFA */

typedef struct {
    int		 d_type;	/* Non-terminal this represents */
    char	*d_name;	/* For printing */
    int		 d_initial;	/* Initial state */
    int		 d_nstates;
    state	*d_state;	/* Array of states */
    bitset	 d_first;
***REMOVED*** dfa;

/* A grammar */

typedef struct {
    int		 g_ndfas;
    dfa		*g_dfa;		/* Array of DFAs */
    labellist	 g_ll;
    int		 g_start;	/* Start symbol of the grammar */
    int		 g_accel;	/* Set if accelerators present */
***REMOVED*** grammar;

/* FUNCTIONS */

grammar *newgrammar(int start***REMOVED***;
dfa *adddfa(grammar *g, int type, char *name***REMOVED***;
int addstate(dfa *d***REMOVED***;
void addarc(dfa *d, int from, int to, int lbl***REMOVED***;
dfa *PyGrammar_FindDFA(grammar *g, int type***REMOVED***;

int addlabel(labellist *ll, int type, char *str***REMOVED***;
int findlabel(labellist *ll, int type, char *str***REMOVED***;
char *PyGrammar_LabelRepr(label *lb***REMOVED***;
void translatelabels(grammar *g***REMOVED***;

void addfirstsets(grammar *g***REMOVED***;

void PyGrammar_AddAccelerators(grammar *g***REMOVED***;
void PyGrammar_RemoveAccelerators(grammar ****REMOVED***;

void printgrammar(grammar *g, FILE *fp***REMOVED***;
void printnonterminals(grammar *g, FILE *fp***REMOVED***;

#ifdef __cplusplus
***REMOVED***
#endif
#endif /* !Py_GRAMMAR_H */
