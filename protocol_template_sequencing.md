---
# MIOP terms
methodology_category: Omics Analysis
project: # can be general
purpose: DNA sequencing assay [OBI:0000626]
analyses: DNA sequencing assay [OBI:0000626]
geographic_location: 
broad_scale_environmental_context: 
local_environmental_context:
environmental_medium: 
target: 
creator: # names separated by commas
materials_required: 
skills_required: 
time_required: # minutes (integer)
personnel_required: 1
language: en
issued: # YYYY-MM-DD
audience: scientists
publisher: # institution
hasVersion: 1
license: 
maturity level: 

# FAIRe terms
barcoding_pcr_appr: # PCR approach for metabarcoding one-step PCR | two-step PCR | ligation-based 
pcr2_thermocycler: # The manufacturer and model of a thermocycler used in the second step PCR
pcr2_amplificationReactionVolume: # The total PCR reaction volume in the second step PCR. Unit = µL
pcr2_commercial_mm: # Name, brand, and manufacture of commercial, pre-made master mix  in the second step PCR (if commercial master mix was used)
pcr2_dna_vol: # Volume of DNA added in each reaction in the second step PCR. Unit = µL
pcr2_annealingTemp: # The reaction temperature during the annealing phase of the second step PCR. Unit = degree Celsius
pcr2_cycles: # Number of PCR cycles in the second step PCR. Unit = cycles
pcr2_analysis_software: # The program used to analyse the PCR runs in the second step PCR
sequencing_location: # The location the sequencing run was performed. Indicate the name of the lab or core facility where samples were sequenced
platform: # General sequencing platform used.
instrument: # Sequencing instrument (manufacturer and model) used. Where possible the term should be taken from the OBI list of DNA sequencers (https://ontobee.org/ontology/OBI?iri=http://purl.obolibrary.org/obo/OBI_0002750)
seq_kit: # The name of sequencing kit
lib_layout: # Specify whether to expect single, paired, or other configuration of reads
adapter_forward: # Forward sequencing adapter. The sequence should be reported in uppercase letters
adapter_reverse: # Reverse sequencing adapter. The sequence should be reported in uppercase letters
lib_screen: # Specific enrichment or screening methods applied before and/or after creating libraries
lib_conc_meth: # Method to estimate lib_conc
phix_perc:  # % of PhiX added into a library, if applicable. Unit = %
---

# Protocol Template

### Quick Links:

- [MIOP](#Minimum-Information-about-an-Omics-Protocol-(MIOP))
- [Background](#BACKGROUND)
- [Equipment](#EQUIPMENT)
- [Standard Operating Procedure (main protocol)](#STANDARD-OPERATING-PROCEDURE)

## Minimum Information about an Omics Protocol (MIOP)

See [MIOP_definition.md](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/MIOP_definition.md) for list and definitions.

| MIOP Term  | Value |
| ------------- | ------------- | 
| methodology category  |  |
| project  |  |
| purpose  |  |
| analyses  |  |
| geographic location  |  |
| broad-scale environmental context  |  |
| local environmental context  |  |
| environmental medium  |  |
| target  |  |
| creator  |  |
| materials required  |  |
| skills required  |  |
| time required  |  |
| personnel required  |  |
| language  |  |
| issued  |  |
| audience  |  |
| publisher  |  |
| hasVersion  |  |
| license  |  |
| maturity level  |  |

## AUTHORS

| PREPARED BY All authors known to have contributed to the preparation of this protocol, including those who filled in the template.  | AFFILIATION | ORCID (visit https://orcid.org/ to register) | DATE |
| ------------- | ------------- | ------------- | ------------- |
| Content Cell  | Content Cell  | Content Cell | yyyy-mm-dd |
| Content Cell  | Content Cell  | Content Cell | yyyy-mm-dd |

## RELATED PROTOCOLS

This is a list of protocols which should be known to users of this protocol. For example, if you create a derivative or altered protocol, you would link to the original protocol in the section below. Please include the link to each related protocol. Also include the version number of that protocol when you linked to it.

| PROTOCOL NAME | LINK  | VERSION The version of the protocol you linked to | RELEASE DATE This is the date corresponding to the version listed to the left |
| ------------- | ------------- | ------------- | ------------- |
| Content Cell  | Content Cell  | Content Cell  | yyyy-mm-dd  |
| Content Cell  | Content Cell  | Content Cell  | yyyy-mm-dd  |

# BACKGROUND

This document describes the required protocol to conduct insert name of the method/protocol.

## Summary

Insert a short description of the background for the method/protocol (e.g. why and for which purpose do you perform water sampling).
Please provide a brief summary of your method including, as appropriate, a brief description of what techniques your best practice is about, which ocean environments or regions it targets, the primary sensors covered, what type of data/measurements/observing platform it covers, limits to its applicability.

## Method description and rationale

Insert a short description of the functioning principal of the methodology used in the protocol (i.e. how does the method work?). Please note that this is different from the step-by-step description of the protocol procedure.
Insert a short statement explaining why the specific methodology used in the protocol has been selected (e.g. it is highly reproducible, highly accurate, procedures are easy to execute etc….).

## Spatial coverage and environment(s) of relevance

If applicable, please specify the region where the protocol is applied. For regional term guidance see here. If applicable, please indicate here the environment(s) of relevance for the protocol, e.g. Abyssal plain. Select from the ENVO terminology.

## Personnel Required

Insert the number of technicians, data managers, and scientists required for the good execution of the procedure

## Safety

Identify hazards associated with the procedure and specify protective equipment and safety training required to safely execute the procedure

## Training requirements

Specify technical training required for the good execution of the procedure.

## Time needed to execute the procedure

Specify how much time is necessary to execute the procedure.

# EQUIPMENT

| DESCRIPTION e.g. filter | PRODUCT NAME AND MODEL Provide the official name of the product | MANUFACTURER Provide the name of the manufacturer of the product. | QUANTITY Provide quantities necessary for one application of the standard operating procedure (e.g. number of filters). | REMARK For example, some of the consumable may need to be sterilized, some commercial solution may need to be diluted or shielded from light during the operating procedure. |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Durable equipment |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Consumable equipment |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Chemicals |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |

# STANDARD OPERATING PROCEDURE

In the following SOP, please use the exact names of equipment as noted in the table above.

Provide a step-by-step description of the protocol. The identification of difficult steps in the protocol and the provision of recommendations for the execution of those steps are encouraged.

### Preparation

Please specify the preparatory actions you took before you collected the samples and note what equipment was needed to do so (e.g. disinfection of work surfaces, preparations to the equipment you intend to use later on).

1.  Step 1
2.  Step 2

### Sequencing

Please specify the actions you took to sequence the DNA and note what equipment was needed to do so (loading of sequencing machine, details about the sequencing run, sequencing institution (if out of house), sequencing primers used).

1. Step 1

| Sequencing Primer Name | Direction | Sequence (5’ -> 3’)|
| ----- | ----- | ----- |
| content | forward | content |
| content | reverse | content |


2. Step 2

    a. Sub-step a

    b. Sub-step b

## Quality control

Describe and explain criteria used to validate results of the standard operating procedure.

## Basic troubleshooting guide

Identify known issues associated with the procedure, if any.
Provide troubleshooting guidelines when available.

## ACRONYMS AND ABBREVIATIONS

| ACRONYM / ABBREVIATION | DEFINITION |
| ------------- | ------------- |
| Content Cell  | Content Cell  |

## GLOSSARY

| SPECIALISED TERM | DEFINITION |
| ------------- | ------------- |
| Content Cell  | Content Cell  |
| Content Cell  | Content Cell  |

# REFERENCES

Insert all references cited in the document.
Please insert full DOI address when available, e.g. http://doi.dx.org/10.1007/s11258-014-0404-1

# APPENDIX A: DATASHEETS

Link templates (e.g. preformatted spreadsheets) used to record measurements and report on the quality of the data as well as any documents such as manufacturer specifications, images, etc that support this protocol. Please include a short note describing the document's relevance.
