
from pysbolgraph.SBOL2Graph import SBOL2Graph

from pysbolgraph.terms import Biopax, SBOL2

uriPrefix = 'http://deadparrot/'


g = SBOL2Graph()

cas9_generic = g.createComponentDefinition(uriPrefix, "cas9_generic", Biopax.Protein)
gRNA_generic = g.createComponentDefinition(uriPrefix, "gRNA_generic", Biopax.RnaRegion)
cas9_gRNA_complex = g.createComponentDefinition(uriPrefix, "cas9_gRNA_complex", Biopax.Complex)
target_gene = g.createComponentDefinition(uriPrefix, "target_gene", Biopax.DnaRegion)
target = g.createComponentDefinition(uriPrefix, "target", Biopax.Protein)

crispr_template = g.createModuleDefinition(uriPrefix, "CRISPR_Template")


cas9_complex_formation = crispr_template.createInteraction("cas9_complex_formation", "http://identifiers.org/biomodels.sbo/SBO:00000177")

cas9_complex_formation.createParticipation("participant_cas9_generic", cas9_generic, "http://identifiers.org/biomodels.sbo/SBO:00000010")
cas9_complex_formation.createParticipation("participant_gRNA_generic", gRNA_generic, "http://identifiers.org/biomodels.sbo/SBO:00000010")
cas9_complex_formation.createParticipation("participant_cas9_gRNA_complex",cas9_gRNA_complex, "http://identifiers.org/biomodels.sbo/SBO:00000011")

# Production of target from target gene
eyfp_production = crispr_template.createInteraction("target_production", "http://identifiers.org/biomodels.sbo/SBO:00000589")
eyfp_production.createParticipation("participant_target_gene", target_gene, "http://identifiers.org/biomodels.sbo/SBO:00000598")
eyfp_production.createParticipation("participant_target", target, "http://identifiers.org/biomodels.sbo/SBO:00000011")


# Inhibition of target by cas9m_BFP_gRNA
target_generic_gene_inhibition = crispr_template.createInteraction("target_gene_inhibition", "http://identifiers.org/biomodels.sbo/SBO:00000169")
target_generic_gene_inhibition.createParticipation("participant_cas9_gRNA_complex", "cas9_gRNA_complex", "http://identifiers.org/biomodels.sbo/SBO:00000020")
target_generic_gene_inhibition.createParticipation("participant_target_gene", "target_gene", "http://identifiers.org/biomodels.sbo/SBO:00000598")


# Create Sequence for CRa_U6 promoter
CRa_U6_seq_elements = "GGTTTACCGAGCTCTTATTGGTTTTCAAACTTCATTGACTGTGCC" + \
"AAGGTCGGGCAGGAAGAGGGCCTATTTCCCATGATTCCTTCATAT" + \
"TTGCATATACGATACAAGGCTGTTAGAGAGATAATTAGAATTAAT" + \
"TTGACTGTAAACACAAAGATATTAGTACAAAATACGTGACGTAGA" + \
"AAGTAATAATTTCTTGGGTAGTTTGCAGTTTTAAAATTATGTTTT" + \
"AAAATGGACTATCATATGCTTACCGTAACTTGAAATATAGAACCG" + \
"ATCCTCCCATTGGTATATATTATAGAACCGATCCTCCCATTGGCT" + \
"TGTGGAAAGGACGAAACACCGTACCTCATCAGGAACATGTGTTTA" + \
"AGAGCTATGCTGGAAACAGCAGAAATAGCAAGTTTAAATAAGGCT" + \
"AGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTT" + \
"TTGGTGCGTTTTTATGCTTGTAGTATTGTATAATGTTTTT"
g.createSequence("CRa_U6_seq", CRa_U6_seq_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")
		
# Create Sequence for gRNA_b coding sequence
gRNA_b_elements = "AAGGTCGGGCAGGAAGAGGGCCTATTTCCCATGATTCCTTCATAT" + \
"TTGCATATACGATACAAGGCTGTTAGAGAGATAATTAGAATTAAT" + \
"TTGACTGTAAACACAAAGATATTAGTACAAAATACGTGACGTAGA" + \
"AAGTAATAATTTCTTGGGTAGTTTGCAGTTTTAAAATTATGTTTT" + \
"AAAATGGACTATCATATGCTTACCGTAACTTGAAAGTATTTCGAT" + \
"TTCTTGGCTTTATATATCTTGTGGAAAGGACGAAACACCGTACCT" + \
"CATCAGGAACATGTGTTTAAGAGCTATGCTGGAAACAGCAGAAAT" + \
"AGCAAGTTTAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGG" + \
"CACCGAGTCGGTGCTTTTTTT"
g.createSequence("gRNA_b_seq", gRNA_b_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")
		
# Create Sequence for mKate
mKate_seq_elements = "TCTAAGGGCGAAGAGCTGATTAAGGAGAACATGCACATGAAGCTG" + \
"TACATGGAGGGCACCGTGAACAACCACCACTTCAAGTGCACATCC" + \
"GAGGGCGAAGGCAAGCCCTACGAGGGCACCCAGACCATGAGAATC" + \
"AAGGTGGTCGAGGGCGGCCCTCTCCCCTTCGCCTTCGACATCCTG" + \
"GCTACCAGCTTCATGTACGGCAGCAAAACCTTCATCAACCACACC" + \
"CAGGGCATCCCCGACTTCTTTAAGCAGTCCTTCCCTGAGGTAAGT" + \
"GGTCCTACCTCATCAGGAACATGTGTTTTAGAGCTAGAAATAGCA" + \
"AGTTAAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACC" + \
"GAGTCGGTGCTACTAACTCTCGAGTCTTCTTTTTTTTTTTCACAG" + \
"GGCTTCACATGGGAGAGAGTCACCACATACGAAGACGGGGGCGTG" + \
"CTGACCGCTACCCAGGACACCAGCCTCCAGGACGGCTGCCTCATC" + \
"TACAACGTCAAGATCAGAGGGGTGAACTTCCCATCCAACGGCCCT" + \
"GTGATGCAGAAGAAAACACTCGGCTGGGAGGCCTCCACCGAGATG" + \
"CTGTACCCCGCTGACGGCGGCCTGGAAGGCAGAAGCGACATGGCC" + \
"CTGAAGCTCGTGGGCGGGGGCCACCTGATCTGCAACTTGAAGACC" + \
"ACATACAGATCCAAGAAACCCGCTAAGAACCTCAAGATGCCCGGC" + \
"GTCTACTATGTGGACAGAAGACTGGAAAGAATCAAGGAGGCCGAC" + \
"AAAGAGACCTACGTCGAGCAGCACGAGGTGGCTGTGGCCAGATAC" + \
"TGCG"
g.createSequence("mKate_seq", mKate_seq_elements,  "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")

# Create Sequence for CRP_b promoter
CRP_b_seq_elements =  "GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACG" + \
"GGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAG" + \
"TACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTTCTGTC" + \
"CTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAAT" + \
"TCTAGGCGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTA" + \
"GTGAACCGTCAGATCGCCTCGAGTACCTCATCAGGAACATGTTGG" + \
"ATCCAATTCGACC"
g.createSequence("CRP_b_seq", CRP_b_seq_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")


CRP_b = g.createComponentDefinition(uriPrefix, "CRP_b", Biopax.DnaRegion)
CRP_b.addRole("http://identifiers.org/so/SO:00000167") # fix me
CRP_b.addSequence(CRP_b)

EYFP_cds = g.createComponentDefinition(uriPrefix, "EYFP_cds", Biopax.DnaRegion)
EYFP_cds.addRole("http://identifiers.org/so/SO:00000167") # fix me

EYFP_gene = g.createComponentDefinition(uriPrefix, "EYFP_gene", Biopax.DnaRegion)
EYFP_gene.createSequenceConstraint("precedes_constraint", SBOL2.precedes, CRP_b, EYFP_cds)

CRPb_circuit = g.createModuleDefinition(uriPrefix, "CRPb_characterization_circuit")
CRPb_circuit.createFunctionalComponent("EYFP", SBOL2.private, "EYFP", SBOL2.directionNone)


Template_Module = CRPb_circuit.createModule("CRISPR_Template", crispr_template)
Template_Module.createMapsTo("cas9m_BFP_map", SBOL2.useLocal, "cas9m_BFP", "cas9_generic")
Template_Module.createMapsTo("gRNA_b_map", SBOL2.useLocal, "gRNA_b", "gRNA_generic")
Template_Module.createMapsTo("cas9m_BFP_gRNA_map", SBOL2.useLocal, "cas9m_BFP_gRNA_b", "cas9_gRNA_complex")
Template_Module.createMapsTo("EYFP_map", SBOL2.useLocal, "EYFP", "target")
Template_Module.createMapsTo("EYFP_gene_map", SBOL2.useLocal, "EYFP_gene", "target_gene")



for s,p,o in g.g.triples((None, None, None)):
    print s,p,o





