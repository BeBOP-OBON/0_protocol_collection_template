---
# MIOP terms
methodology_category: sample extraction and purification
project: # can be general
purpose: biodiversity assessment objective [OBI:0001969]
analyses: DNA extraction [OBI:0000257]
geographic_location: # Atlantic Ocean [GAZ:00000344], Gulf of Mexico [GAZ:00002853]
broad_scale_environmental_context: # marine biome [ENVO:00000447], marine photic zone [ENVO:00000209]
local_environmental_context: # marine biome [ENVO:00000447], marine photic zone [ENVO:00000209]
environmental_medium: # sea water [ENVO:00002149]
target: deoxyribonucleic acid (DNA) [NCIT:C449]
creator: # names separated by commas
materials_required: # vortexer [OBI:0400118], centrifuge [OBI:0400106], DNA extraction/purification instrument [OBI:0001117], multichannel electronic pipette [OBI:0001083] (optional)
skills_required: sterile technique, pipetting skills, standard molecular technique
time_required: # minutes (integer)
personnel_required: 1
language: en
issued: # YYYY-MM-DD
audience: scientists
publisher: # institution
hasVersion: 1
license: CC0 1.0 Universal
maturity level: mature

# FAIRe terms
samp_vol_we_dna_ext: # 1
samp_vol_we_dna_ext_unit: # mL
nucl_acid_ext_lysis: # physical
nucl_acid_ext_sep: # centrifugation
nucl_acid_ext: # https://files.zymoresearch.com/protocols/_d4302_d4306_d4308_zymobiomics-96_magbead_dna_kit.pdf
nucl_acid_ext_kit: # ZymoBIOMICS 96 Magbead DNA Kit
nucl_acid_ext_modify: # Sterivex was lysed with 1000 uL of ZymoBIOMICS Lysis Solution, use of KingFisher Flex Purification System for bead cleanup and final elution
dna_cleanup_0_1: # 1.0
dna_cleanup_method: # ZymoBIOMICS 96 Magbead DNA Kit
concentration: # not applicable
concentration_method: # VarioSkan Microplate Reader, Quant-iT dsDNA Assay Kit High Sensitivity
ratioOfAbsorbance260_280: # not applicable
pool_dna_num: # not applicable
nucl_acid_ext_method_additional: # not applicable
---

# Protocol Template - DNA Extraction

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

## EQUIPMENT

- Opentrons Consumables: If using Opentrons OT-2 Robot for KF Plate Prep.
- Description: E.g., "filter".
- Product Name and Model: Provide the official name of the product.
- Manufacturer: Provide the name of the manufacturer of the product.
- Quantity: Provide quantities necessary for one application of the standard operating procedure (e.g., number of filters).
- Remark: For example, some of the consumable may need to be sterilized, some commercial solution may need to be diluted or shielded from light during the operating procedure.

| DESCRIPTION | PRODUCT NAME AND MODEL | MANUFACTURER | QUANTITY | REMARK |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| **Durable equipment** |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| **Consumable equipment** |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| **Chemicals** |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |
| Content Cell | Content Cell | Content Cell | Content Cell | Content Cell |

## STANDARD OPERATING PROCEDURE

In the following SOP, please use the exact names of equipment as noted in the table above.

Provide a step-by-step description of the protocol. The identification of difficult steps in the protocol and the provision of recommendations for the execution of those steps are encouraged.

### Preparation

Please specify the preparatory actions you took before you extracted the DNA from your samples and note what equipment was used to do so (e.g. disinfection of work surfaces, preparations to the equipment you intend to use later on).

1. [Step 1]
2. [Step 2]

### Extraction

Please specify the actions you took to extract the DNA from your samples and note what equipment was used to do so (e.g. incubation, vortexing, washing, elution, use of controls).

1. [Step 1]
2. [Step 2]
   a. [Sub-step a]
   b. [Sub-step b]

### Quality Control

Describe and explain criteria used to validate results of the standard operating procedure.

### Basic Troubleshooting Guide

- Identify known issues associated with the procedure, if any.
- Provide troubleshooting guidelines when available.

## REFERENCES

- Insert all references cited in the document.
- Please insert full DOI address when available, e.g. http://doi.dx.org/10.1007/s11258-014-0404-1

## APPENDIX A: DATASHEETS

Link templates (e.g. preformatted spreadsheets) used to record measurements and report on the quality of the data as well as any documents such as manufacturer specifications, images, etc that support this protocol. Please include a short note describing the document's relevance.
