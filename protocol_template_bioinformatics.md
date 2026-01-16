---
# MIOP terms
meth_cat: bioinformatics
project: # can be general
purpose: # taxonomic diversity assessment by targeted gene survey [OBI:0001960]
analyses: # "bioinformatics analysis [MIOP:0000004] | amplicon sequencing assay [OBI:0002767]"
geographic_location: not applicable
broad-scale_environmental_context: not applicable
local_environmental_context: not applicable
environmental_medium: not applicable
target: not applicable
creator: # names separated by commas
materials_required: # list of software tools and versions
skills_required: # proficiency with UNIX command line and amplicon/metabarcoding data analysis
time_required: # 120 minutes
personnel_required: # 1 person
language: en
issued: # 2025-09-30
audience: # metabarcoding data analysts
publisher: # institution
hasVersion: # 1.0.0
license: # CC0
maturity_level: # Pilot or Demonstrated

# FAIRe terms
checkls_ver: # 1.0.2
sop_bioinformatics: # "https://github.com/aomlomics/tourmaline/tree/develop"
assay_name: # Eukarya-18S-V9-Lane-Medlin
trim_method: # qiime2-amplicon-2024.10;Cutadapt 4.9
trim_param: # not applicable
demux_tool: # Illumina Bcl2fastq v2.20.0
demux_max_mismatch: # not applicable
merge_tool: # qiime2-amplicon-2024.10;DADA2 1.30.0
merge_min_overlap: # not applicable
min_len_cutoff:
  default: # 50
  source_file: # config_01_qaqc.yaml
  source_term: # minimum_length
min_len_tool: # qiime2-amplicon-2024.10;Cutadapt 4.9
error_rate_tool: # qiime2-amplicon-2024.10;DADA2 1.30.0
error_rate_cutoff:
  default: # 2
  source_file: # config_02_repseqs.yaml
  source_term: # dada2_max_ee_f
error_rate_type: # not applicable
chimera_check_method: # denovo;qiime2-amplicon-2024.10;DADA2 1.30.0
chimera_check_param: # not applicable
otu_clust_tool: # qiime2-amplicon-2024.10;DADA2 1.30.0
otu_clust_cutoff: # not applicable
min_reads_cutoff:
  default: # not applicable
  source_file: # config_02_repseqs.yaml
  source_term: # deblur_min_reads
min_reads_cutoff_unit: # not applicable
min_reads_tool: # qiime2-amplicon-2024.10;DADA2 1.30.0
otu_db: # not applicable
otu_db_custom:
  default: # rcrux_18Sv4_NA_removed_uniq-classifier
  options: # pr2_v5.0.0_18Sv4_uniq-classifier
  source_file: # config_03_taxonomy.yaml
  source_term: # database_name 
tax_assign_cat: # not applicable
otu_seq_comp_appr:
  default: # qiime2-amplicon-2024.10;naive-bayes classifier;scikit-learn 1.4.2
  source_file: # config_03_taxonomy.yaml
  source_term: # classify_method
tax_class_id_cutoff:
  default: # not applicable
  options: # [0-1]
  source_file: # config_03_taxonomy.yaml
  source_term: # perc_identity
tax_class_query_cutoff:
  default: # not applicable
  options: # [0-1]
  source_file: # config_03_taxonomy.yaml
  source_term: # query_cov
tax_class_other:
  options: # --verbose
  source_file: # config_03_taxonomy.yaml
  source_term: # classify_params
tax_class_collapse:
  default: # 0.7
  options: # [0-1]
  source_file: # config_03_taxonomy.yaml
  source_term: # skl_confidence
screen_contam_method: # not applicable
screen_geograph_method: # not applicable
screen_nontarget_method: # not applicable
screen_other: # not applicable
otu_raw_description: # not applicable
otu_final_description: # not applicable
bioinfo_method_additional: # not applicable
input_read_count: # not applicable
output_read_count: # not applicable
output_otu_num: # not applicable
otu_num_tax_assigned: # not applicable
---

# Protocol Template -- Bioinformatics

## PROTOCOL INFORMATION

### Minimum Information about an Omics Protocol (MIOP)

- MIOP terms are listed in the YAML frontmatter of this page.
- See [MIOP_definition.md](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/MIOP_definition.md) for list and definitions.

### Making eDNA FAIR (FAIRe)

- FAIRe terms are listed in the YAML frontmatter of this page.
- See <https://fair-edna.github.io/download.html> for the FAIRe checklist and more information.
- See <https://fair-edna.github.io/guidelines.html#missing-values> for guidelines on missing values that can be used for missing FAIRe or MIOP terms.

### Authors

- All authors known to have contributed to the preparation of this protocol, including those who filled in the template.
- Visit https://orcid.org/ to register for an ORCID.
- Date is the date the author first worked on the protocol.

| PREPARED BY  | AFFILIATION  | ORCID        | DATE       |
| ------------ | ------------ | ------------ | ---------- |
| Content Cell | Content Cell | Content Cell | yyyy-mm-dd |
| Content Cell | Content Cell | Content Cell | yyyy-mm-dd |

### Related Protocols

- This section contains protocols that should be known to users of this protocol.
- Include the link to each protocol.
- Include the version number and release date (if available).
- Internal/External: "Internal" are derivative or altered protocols, or other protocols in this workflow. "External" are protcols from manufacturers or other groups.

| PROTOCOL NAME | LINK         | VERSION      | RELEASE DATE | INTERNAL/EXTERNAL |
| ------------- | ------------ | ------------ | ------------ | ----------------- |
| Content Cell  | Content Cell | Content Cell | yyyy-mm-dd   | Content Cell      |
| Content Cell  | Content Cell | Content Cell | yyyy-mm-dd   | Content Cell      |

### Protocol Revision Record

- Version numbers start at 1.0.0 when the protocol is first completed and will increase when changes that impact the outcome of the procedure are made (patches: 1.0.1; minor changes: 1.1.0; major changes: 2.0.0).
- Release date is the date when a given protocol version was finalised.
- Description of revisions includes a brief description of what was changed relative to the previous version.

| VERSION | RELEASE DATE | DESCRIPTION OF REVISIONS |
| ------------- | ------------- | ------------- |
| 1.0.0 | yyyy-mm-dd | Initial release |

### Acronyms and Abbreviations

| ACRONYM / ABBREVIATION | DEFINITION |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

### Glossary

| SPECIALISED TERM | DEFINITION |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

## BACKGROUND

This document describes the required protocol to conduct [insert name of the method/protocol].

### Summary

Insert a short description of the background for the method/protocol (e.g. why and for which purpose do you perform water sampling).
Please provide a brief summary of your method including, as appropriate, a brief description of what techniques your best practice is about, which ocean environments or regions it targets, the primary sensors covered, what type of data/measurements/observing platform it covers, limits to its applicability.

### Method Description and Rationale

Insert a short description of the functioning principal of the methodology used in the protocol (i.e. how does the method work?). Please note that this is different from the step-by-step description of the protocol procedure.
Insert a short statement explaining why the specific methodology used in the protocol has been selected (e.g. it is highly reproducible, highly accurate, procedures are easy to execute etc….).

### Spatial Coverage and Environment(s) of Relevance

If applicable, please specify the region where the protocol is applied. For regional term guidance see the [GAZ ontology](https://www.ebi.ac.uk/ols4/ontologies/gaz). If applicable, please indicate here the environment(s) of relevance for the protocol, e.g. Abyssal plain. Select from the [ENVO ontology](https://www.ebi.ac.uk/ols4/ontologies/envo).

## PERSONNEL REQUIRED

Insert the number of technicians, data managers, and scientists required for the good execution of the procedure

### Safety

Identify hazards associated with the procedure and specify protective equipment and safety training required to safely execute the procedure

### Training Requirements

Specify technical training required for the good execution of the procedure.

### Time Needed to Execute the Procedure

Specify how much time is necessary to execute the procedure.

# EQUIPMENT, SOFTWARE & PACKAGES

| NAME | VERSION OR MODEL | MANUFACTURER OR CREATOR | REMARKS |
| ------------- | ------------- | ------------- | ------------- |
| Equipment |
| e.g. Laptop | Content Cell | Content Cell | e.g. needs at least 16 GB of RAM |
| Content Cell | Content Cell | Content Cell | Content Cell |
| Software |
| Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell |
| Code |
| Please include the links to the code you used for this analysis |
| e.g. link to the released version of a github repository  | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell |

## GUIDE TO ARCHIVED METHODOLOGY

The contents of this archive should allow your analysis to be reproduced exactly as you intended it.

This document provides guidance on the contents of each partner's compressed archive of in-silico methods. This document should be part of that same archive, serving as an extended README.

Below, please find guidance on what this archive should include. When describing the contents of the archive, please give precise file names and relative paths to the files.

### Archive content

To reproduce the in-silico analysis, please provide one of the following (in order of decreasing preference):

1. Jupyter, R notebook(s) or equivalents
2. Downloaded archive of (the released version of) your github repository
3. Individual scripts

In each of the above cases, guidance and documentation for all the steps you took to perform the in-silico analysis should be included. In case 1., code and documentation are integrated. In cases 2. and 3., in-line comments may be provided, however, these are not generally sufficient as documentation. In those cases, please provide a step-by-step protocol on how and when to run each script in the Execution Procedure section below.

Please include a script on **data acquisition** (e.g. documentation and code to pull sequences from INSDC, access sequences on an institutional FTP server, download metadata files, check file integrity via md5 checksum). Please add sufficient detail, so that the partners only have to install the software, run this script and will then have all the data needed to perform any analysis described below.

### Code

Here please describe each file containing code, including its purpose, its input, its output. Please provide the names and the relative paths to this documentation.

### Code documentation

Here, please indicate if your documentation is with the code (in a code notebook) or stored separately. In-line comments are not considered documentation. If the documentation is stored separately, please provide the names and the relative paths to this documentation.

### Metadata

Please provide link(s) to the files containing metadata about your sequence data (e.g. environmental data, procedural data). Please see the MIxS compliant metadata guidance.

Auxiliary files, e.g. mapping files, test/dummy files, colour palette.

### Execution Procedure

Please fill out this section if you have not already documented it as part of your R, Jupyter, or similar notebook. In this section, please provide a step-by-step guidance on how and when to run each component of your code.

### Quality control

In this section please include the names and paths that can be used to validate that operations were successful. If such checks were done during the execution procedures, please note this here. We recommend identifying such steps with in-line tags (e.g. “#QC”).

### Basic troubleshooting guide

Identify known issues associated with the procedure, if any. Provide troubleshooting guidelines when available.

## REFERENCES

- Insert all references cited in the document.
- Please insert full DOI address when available, e.g., https://doi.org/10.1007/s11258-014-0404-1.

## APPENDIX A: DATASHEETS

Link templates (e.g. preformatted spreadsheets) used to record measurements and report on the quality of the data as well as any documents such as manufacturer specifications, images, etc that support this protocol. Please include a short note describing the document's relevance.
