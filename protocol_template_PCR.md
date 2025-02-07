---
# MIOP terms
methodology_category: Omics Analysis
project: # can be general
purpose: PCR [OBI:0000415]
analyses: PCR [OBI:0000415]
geographic_location: Atlantic Ocean [GAZ:00000344], Gulf of Mexico [GAZ:00002853]
broad_scale_environmental_context: marine biome [ENVO:00000447], marine photic zone [ENVO:00000209]
local_environmental_context: marine biome [ENVO:00000447], marine photic zone [ENVO:00000209]
environmental_medium: sea water [ENVO:00002149], polymerase chain reaction [OBI:0000415]
target: 16S [NCIT:C105370]
creator: # names separated by commas
materials_required: vortexer [OBI:0400118], PCR instrument [OBI:0000989], agarose gel electrophoresis system [OBI:0001134]
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
pcr_0_1: # 1
thermocycler: # name of thermocycler
amplificationReactionVolume: # 25
assay_name: # ssu16sv4v5_emp
assay_validation: # not provided
targetTaxonomicAssay: # 16S rRNA gene sequencing targeting the V4-V5 region using primers 515F and 926R
targetTaxonomicScope: # Prokaryotes, including Bacteria and Archaea
target_gene: # 16S rRNA
target_subfragment: # V4-V5
ampliconSize: # 411
pcr_primer_forward: # GTGYCAGCMGCCGCGGTAA
pcr_primer_reverse: # CCGYCAATTYMTTTRAGTTT
pcr_primer_name_forward: # 515F-Y
pcr_primer_name_reverse: # 926R
pcr_primer_reference_forward: # 10.1111/1462-2920.13023
pcr_primer_reference_reverse: # 10.1111/1462-2920.13023
pcr_primer_vol_forward: # 1.0
pcr_primer_vol_reverse: # 1.0
pcr_primer_conc_forward: # 10
pcr_primer_conc_reverse: # 10
probeReporter: # not applicable
probeQuencher: # not applicable
probe_seq: # not applicable
probe_ref: # not applicable
probe_conc: # not applicable
commercial_mm: # AmpliTaq Gold 360 Master Mix
custom_mm: # PCR reactions were run in 25 uL reaction volumes, with 1.0 uL of DNA, 12.5 uL of AmpliTaq Gold, 9.5 uL of water, and 1.0 uL of each primer (10 uM)
pcr_dna_vol: # 1.0
pcr_rep: # 1
nucl_acid_amp: # https://doi.org/10.1111/1462-2920.13023
pcr_cond: # initial denaturation:95_3;denaturation:95_0.75;annealing:50_0.75;elongation:72_1.5;final elongation:72_10;30
annealingTemp: # 50
pcr_cycles: # 30
pcr_analysis_software: # not provided
pcr_method_additional: # not provided
---

# Protocol Template

## PROTOCOL INFORMATION

### Quick Links:

- [MIOP](#Minimum-Information-about-an-Omics-Protocol-(MIOP))
- [Background](#BACKGROUND)
- [Equipment](#EQUIPMENT)
- [Standard Operating Procedure (main protocol)](#STANDARD-OPERATING-PROCEDURE)

## Minimum Information about an Omics Protocol (MIOP)

See [MIOP_definition.md](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/MIOP_definition.md) for list and definitions.

### Making eDNA FAIR (FAIRe)

- FAIRe terms are listed in the YAML frontmatter of this page.
- See <https://fair-edna.github.io/download.html> for the FAIRe checklist and more information.
- See <https://fair-edna.github.io/guidelines.html#missing-values> for guidelines on missing values that can be used for missing FAIRe or MIOP terms.

## Authors

| PREPARED BY All authors known to have contributed to the preparation of this protocol, including those who filled in the template.  | AFFILIATION | ORCID (visit https://orcid.org/ to register) | DATE |
| ------------- | ------------- | ------------- | ------------- |
| Content Cell  | Content Cell  | Content Cell | yyyy-mm-dd |
| Content Cell  | Content Cell  | Content Cell | yyyy-mm-dd |

## Related Internal Protocols

This is a list of protocols which should be known to users of this protocol. For example, if you create a derivative or altered protocol, you would link to the original protocol in the section below. Please include the link to each related protocol. Also include the version number of that protocol when you linked to it.

| PROTOCOL NAME | LINK  | VERSION The version of the protocol you linked to | RELEASE DATE This is the date corresponding to the version listed to the left |
| ------------- | ------------- | ------------- | ------------- |
| Content Cell  | Content Cell  | Content Cell  | yyyy-mm-dd  |
| Content Cell  | Content Cell  | Content Cell  | yyyy-mm-dd  |

## Related External Protocols

| PROTOCOL NAME | LINK | ISSUER / AUTHOR | ACCESS DATE |
| ------------ | ------------ | ------------ | ---------- |
| Content Cell  | Content Cell  | Content Cell  | yyyy-mm-dd  |
| Content Cell  | Content Cell  | Content Cell  | yyyy-mm-dd  |

### Protocol Revision Record

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

- Description: E.g., "filter".
- Product Name and Model: Provide the official name of the product.
- Manufacturer: Provide the name of the manufacturer of the product.
- Quantity: Provide quantities necessary for one application of the standard operating procedure (e.g., number of filters).
- Remark: For example, some of the consumable may need to be sterilized, some commercial solution may need to be diluted or shielded from light during the operating procedure.

# STANDARD OPERATING PROCEDURE

In the following SOP, please use the exact names of equipment as noted in the table above.

Provide a step-by-step description of the protocol. The identification of difficult steps in the protocol and the provision of recommendations for the execution of those steps are encouraged.

### Preparation

Please specify the preparatory actions you took before you collected the samples and note what equipment was needed to do so (e.g. disinfection of work surfaces, preparations to the equipment you intend to use later on).

1.  Step 1
2.  Step 2

### PCR

Please specify the actions you took to amplify the previously extracted DNA and the equipment and primers you used (ingredients for the PCR reaction, number of triplicates, PCR cycle parameter)

**Primers**: PCR primer sequences

| PCR Primer Name | Direction | Sequence (5’ -> 3’)|
| ----- | ----- | ----- |
| content | forward | content |
| content | reverse | content |

**Reaction Mixture**: PCR reagents, volumes, initial and final concentrations

| reagent | volume | intial concentration| final concentration|
| ----- | ----- | ----- |----- |
| content | content | content |content |
| content | content | content |content |

**PCR Cycling Program**: 

| PCR step | Temperature | Duration | Repetition |
| ----- | ----- | ----- | ----- |
| content | content | content | content |
| content | content | content | content |

1. Step 1

2. Step 2

3. Step 3


### Quality control, PCR clean-up

Please specify the actions you took to confirm the quality of the PCR output, to clean up the PCR output and the equipment you used (e.g. agarose gel to confirm quality, purification of PCR products).

1. Step 1

2. Step 2

## Quality control

Describe and explain criteria used to validate results of the standard operating procedure.

## Basic troubleshooting guide

Identify known issues associated with the procedure, if any.
Provide troubleshooting guidelines when available.

## REFERENCES

Insert all references cited in the document.
Please insert full DOI address when available, e.g. http://doi.dx.org/10.1007/s11258-014-0404-1

## APPENDIX A: DATASHEETS

Link templates (e.g. preformatted spreadsheets) used to record measurements and report on the quality of the data as well as any documents such as manufacturer specifications, images, etc that support this protocol. Please include a short note describing the document's relevance.
