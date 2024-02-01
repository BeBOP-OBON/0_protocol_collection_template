# Protocol collection templates

This repository contains protocol templates for biomolecular ocean observing. The templates were developed on the basis of the NEON and AWI protocol templates, and adapted for the purpose of capturing metagenomic ocean observing workflows. 

This repository is maintained by the Better Biomolecular Ocean Practices (BeBOP) UN Ocean Decade Project under the [Ocean Biomolecular Observing Network (OBON)](https://www.obon-ocean.org/) programme. This project developed out of the [Task Team 21-03: Omics/eDNA Protocol Management](https://www.oceanbestpractices.org/about/task-teams/obps-task-team-21-03-omics-edna-protocol-management/) under the Ocean Best Practices System.

## Aim and Scope
We aim to achieve increased comparability between Biomolecular Ocean Practices (BOPs). Currently, the wealth of ocean biomolecular practices is shared in diverse formats (e.g. text in publications, pdfs, ...). To allow the community to understand differences in practices and the potential for integrating the data generated using the BOPs, we intend to offer means of standardization via the development of the templates found in this repository. These will allow humans to more efficiently (or at all) log and compare protocols at scale.

## How to use the content of this repository

### Exploring the protocol templates
This repository currently contains protocol templates for the following steps of an omics observation:
- [Sampling](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_sampling.md)
- [DNA extraction](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_DNA_extraction.md)
- [PCR and clean up](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_PCR.md)
- [Sequencing](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_sequencing.md)
- [In-silico analysis](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_insilico_analysis.md)

All protocol templates follow a similar structure: General metadata on top, followed by sections on background, personnel required, and equipment required. Next, you will find a section on the Standard Operating Procedure (SOP), which should be used to report on the exact steps taken as part of executing a protocol. In the template for insilico analysis, in place of the SOP, there is a Guide to the archived methodology and a section on Archive content. The templates conclude with References and Appendices.

Note, that the protocol-level metadata is to be reported as part of the protocol in the section Minimum Information about an Omic Protocol (MIOP). For more information and guidance on MIOP, please refer to this document [MIOP_definition.md](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/MIOP_definition.md) or consult the [MIOP repository](https://github.com/BeBOP-OBON/miop) in this organisation.

### Create your own repository from this template

**To use the templates, and apply them to your own protocols, please create a repository from this template.**

This repository is a "template respository". For guidance on how to create your own repository from this template please see [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

On the main page of this repository:
1. Above the file list, click "Use this template".
2. Select "Create a new repository".
3. Choose repository ownership (select "BeBOP-OBON" to be featured on the BeBOP page) and name your repository after your project or institution
  - *You can always link your repository later to the BeBOP-OBON github space if you would like to work on protocols within your own github location first.*

### Editing the protocol templates
In your new repository, you may then freely edit the content sections of the protocol in markdown. If you are unfamiliar with markdown language, please see this list of resources and softwares to support your work:

Training resources
- [Markdown Cheatsheet by Adam Pritchard](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Markdown Crash Course by Traversy Media](https://youtu.be/HUBNt18RFbo) 
- [Writing on GitHub by GitHub docs](https://docs.github.com/en/get-started/writing-on-github)

Markdown Editors (not necessary, but may facilitate editing in markdown)
- [Visiual Studio Code](https://code.visualstudio.com/Docs/languages/markdown)
- [MacDown](https://macdown.uranusjr.com), open source Markdown editor for macOS

### Versioning
For the versioning of your protocol, please note the section on _version control_ in the [Towards a Best Practice for Developing Best Practices in Ocean Observation (BP4BP): Supporting Methodological Evolution through Actionable Documentation](http://dx.doi.org/10.25607/OBP-781) publication. 

As noted there, we recommend the use of [semantic versioning](https://semver.org). 
> Given a version number MAJOR.MINOR.PATCH, increment the:
> - MAJOR version when you make incompatible API changes
> - MINOR version when you add functionality in a backwards compatible manner
> - PATCH version when you make backwards compatible bug fixes
>
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

### Converting Markdown to PDF
For sharing the protocols, PDF versions of the protocols may be more convenient(xRef https://github.com/BeBOP-OBON/0_protocol_collection_template/issues/1). The PDF versions of the protocols can also be added to your repository alongside with their markdown versions. 

Please see below for some tools to convert your markdown file to PDF
- [Markdowntopdf](https://www.markdowntopdf.com)(online tool)
- [GitHub action to make pdfs from markdown files](https://github.com/BaileyJM02/markdown-to-pdf)

### Release your repository and get citable DOIs from Zenodo

For information on creating a release of your repository and getting DOIs from Zenodo, please see the guidance [here](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

Please also note the [GLOMICON community](https://zenodo.org/communities/glomicon/) on Zenodo. When archiving your repository with Zenodo, please do so in this community.

## See a problem or have a recommendation?
Please use this GitHub repository's [Issue tracker](https://github.com/BeBOP-OBON/0_protocol_collection_template/issues) to request changes/additions or report errors or specific concerns related to the protocol templates.

