from pysbolgraph.SBOL2Graph import SBOL2Graph

from pysbolgraph.terms import Biopax, SBOL2

uriPrefix = 'http://deadparrot/'

g = SBOL2Graph()

cas9_generic = g.create_component_definition(uriPrefix, "cas9_generic", Biopax.Protein)
gRNA_generic = g.create_component_definition(uriPrefix, "gRNA_generic", Biopax.RnaRegion)
cas9_gRNA_complex = g.create_component_definition(uriPrefix, "cas9_gRNA_complex", Biopax.Complex)
target_gene = g.create_component_definition(uriPrefix, "target_gene", Biopax.DnaRegion)
target = g.create_component_definition(uriPrefix, "target", Biopax.Protein)

crispr_template = g.create_module_definition(uriPrefix, "CRISPR_Template")

cas9_complex_formation = crispr_template.create_interaction("cas9_complex_formation",
                                                            "http://identifiers.org/biomodels.sbo/SBO:00000177")

cas9_complex_formation.create_participation("participant_cas9_generic", cas9_generic,
                                            "http://identifiers.org/biomodels.sbo/SBO:00000010")
cas9_complex_formation.create_participation("participant_gRNA_generic", gRNA_generic,
                                            "http://identifiers.org/biomodels.sbo/SBO:00000010")
cas9_complex_formation.create_participation("participant_cas9_gRNA_complex", cas9_gRNA_complex,
                                            "http://identifiers.org/biomodels.sbo/SBO:00000011")

# Production of target from target gene
eyfp_production = crispr_template.create_interaction("target_production",
                                                     "http://identifiers.org/biomodels.sbo/SBO:00000589")
eyfp_production.create_participation("participant_target_gene", target_gene,
                                     "http://identifiers.org/biomodels.sbo/SBO:00000598")
eyfp_production.create_participation("participant_target", target, "http://identifiers.org/biomodels.sbo/SBO:00000011")

# Inhibition of target by cas9m_BFP_gRNA
target_generic_gene_inhibition = crispr_template.create_interaction("target_gene_inhibition",
                                                                    "http://identifiers.org/biomodels.sbo/SBO:00000169")
target_generic_gene_inhibition.create_participation("participant_cas9_gRNA_complex", "cas9_gRNA_complex",
                                                    "http://identifiers.org/biomodels.sbo/SBO:00000020")
target_generic_gene_inhibition.create_participation("participant_target_gene", "target_gene",
                                                    "http://identifiers.org/biomodels.sbo/SBO:00000598")

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
g.create_sequence(uriPrefix, "CRa_U6_seq", CRa_U6_seq_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")

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
g.create_sequence(uriPrefix, "gRNA_b_seq", gRNA_b_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")

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
g.create_sequence(uriPrefix, "mKate_seq", mKate_seq_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")

# Create Sequence for CRP_b promoter
CRP_b_seq_elements = "GCTCCGAATTTCTCGACAGATCTCATGTGATTACGCCAAGCTACG" + \
                     "GGCGGAGTACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAG" + \
                     "TACTGTCCTCCGAGCGGAGTACTGTCCTCCGAGCGGAGTTCTGTC" + \
                     "CTCCGAGCGGAGACTCTAGATACCTCATCAGGAACATGTTGGAAT" + \
                     "TCTAGGCGTGTACGGTGGGAGGCCTATATAAGCAGAGCTCGTTTA" + \
                     "GTGAACCGTCAGATCGCCTCGAGTACCTCATCAGGAACATGTTGG" + \
                     "ATCCAATTCGACC"
g.create_sequence(uriPrefix, "CRP_b_seq", CRP_b_seq_elements, "http://www.chem.qmul.ac.uk/iubmb/misc/naseq.html")

CRP_b = g.create_component_definition(uriPrefix, "CRP_b", Biopax.DnaRegion)
CRP_b.add_role("http://identifiers.org/so/SO:00000167")  # fix me
CRP_b.add_sequence(CRP_b)

EYFP_cds = g.create_component_definition(uriPrefix, "EYFP_cds", Biopax.DnaRegion)
EYFP_cds.add_role("http://identifiers.org/so/SO:00000167")  # fix me

EYFP_gene = g.create_component_definition(uriPrefix, "EYFP_gene", Biopax.DnaRegion)
EYFP_gene.create_sequence_constraint("precedes_constraint", SBOL2.precedes, CRP_b, EYFP_cds)

CRPb_circuit = g.create_module_definition(uriPrefix, "CRPb_characterization_circuit")
CRPb_circuit.create_functional_component("EYFP", SBOL2.private, "EYFP", SBOL2.none)

Template_Module = CRPb_circuit.create_module("CRISPR_Template", crispr_template)
Template_Module.create_maps_to("cas9m_BFP_map", SBOL2.useLocal, "cas9m_BFP", "cas9_generic")
Template_Module.create_maps_to("gRNA_b_map", SBOL2.useLocal, "gRNA_b", "gRNA_generic")
Template_Module.create_maps_to("cas9m_BFP_gRNA_map", SBOL2.useLocal, "cas9m_BFP_gRNA_b", "cas9_gRNA_complex")
Template_Module.create_maps_to("EYFP_map", SBOL2.useLocal, "EYFP", "target")
Template_Module.create_maps_to("EYFP_gene_map", SBOL2.useLocal, "EYFP_gene", "target_gene")

xml_string = g.serialize_xml().decode("utf-8")

print(xml_string)
print("\n"*5)
print("Results from SBOL Validator service:")
print(g.validate_xml(xml_string))
