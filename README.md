# BeBOP Protocol Templates

This repository contains protocol templates for biomolecular ocean observing. The templates were developed on the basis of the NEON and AWI protocol templates, and adapted for the purpose of capturing metagenomic ocean observing workflows. 

This repository is maintained by the Better Biomolecular Ocean Practices (BeBOP) UN Ocean Decade Project under the [Ocean Biomolecular Observing Network (OBON)](https://www.obon-ocean.org/) programme. This project developed out of the [Task Team 21-03: Omics/eDNA Protocol Management](https://www.oceanbestpractices.org/about/task-teams/obps-task-team-21-03-omics-edna-protocol-management/) under the Ocean Best Practices System.

## Aim and scope

We aim to achieve increased comparability between Biomolecular Ocean Practices (BOPs). Currently, the wealth of ocean biomolecular practices is shared in diverse formats (e.g., text in publications, PDFs, ...). To allow the community to understand differences in practices and the potential for integrating the data generated using the BOPs, we intend to offer means of standardization via the development of the templates found in this repository. These will allow humans to more efficiently (or at all) log and compare protocols at scale.

## Example BeBOP protocols

Existing protocols in BeBOP format can be found using the GitHub topic [obon-bebop](https://github.com/topics/obon-bebop).

## How to use the content of this repository

### Exploring the protocol templates

This repository currently contains protocol templates for the following steps of an omics observation:

- [Sampling](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_sampling.md)
- [DNA extraction](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_DNA_extraction.md)
- [PCR and clean up](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_PCR.md)
- [Sequencing](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_sequencing.md)
- [Bioinformatics](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/protocol_template_bioinformatics.md)

All protocol templates follow a similar structure: General metadata on top, followed by sections on background, personnel required, and equipment required. Next, you will find a section on the Standard Operating Procedure (SOP), which should be used to report on the exact steps taken as part of executing a protocol. In the template for bioinformatics, in place of the SOP, there is a Guide to the archived methodology and a section on Archive content. The templates conclude with References and Appendices.

Note, that the protocol-level metadata is to be reported as part of the protocol in the section Minimum Information about an Omic Protocol (MIOP). For more information and guidance on MIOP, please refer to this document [MIOP_definition.md](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/MIOP_definition.md) or consult the [MIOP repository](https://github.com/BeBOP-OBON/miop) in this organisation.

### Create your own repository for each protocol

To create a new protocol, follow these instructions:

1. Create a new repository from your GitHub account or organization. Choose a descriptive name, e.g., "MyInstitution-PCR-Protocol-MyAssay".
2. Create a README.md file. It can be blank for now. You'll be able to add the Zenodo DOI later (see below).
3. Create a new markdown file for your protocol. You may want to use the same name as your repository name, e.g., "MyInstitution-PCR-Protocol-MyAssay.md".
4. Copy the appropriate template text from this repository to your new markdown file.

### Editing the protocol templates

In your new repository, you may then freely edit the content sections of the protocol in markdown. If you are unfamiliar with markdown language, please see this list of resources and softwares to support your work:

Training resources:

- [Markdown Cheatsheet by Adam Pritchard](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
- [Markdown Crash Course by Traversy Media](https://youtu.be/HUBNt18RFbo) 
- [Writing on GitHub from GitHub Docs](https://docs.github.com/en/get-started/writing-on-github)

Markdown editors (not necessary but may facilitate editing in markdown):

- [Visual Studio Code](https://code.visualstudio.com/Docs/languages/markdown) – widely used integrated development environment
- [Typora](https://typora.io/) – simple yet powerful Markdown editor for all operating systems
- [MacDown](https://macdown.uranusjr.com) – open-source Markdown editor for macOS
- [HackMD.io](https://hackmd.io/) – web-based Markdown editor for collaborative work

### Versioning

For the versioning of your protocol, please note the section on _version control_ in the [Towards a Best Practice for Developing Best Practices in Ocean Observation (BP4BP): Supporting Methodological Evolution through Actionable Documentation](http://dx.doi.org/10.25607/OBP-781) publication. 

As noted there, we recommend the use of [semantic versioning](https://semver.org):

> Given a version number MAJOR.MINOR.PATCH, increment the:
> - MAJOR version when you make incompatible API changes
> - MINOR version when you add functionality in a backwards compatible manner
> - PATCH version when you make backwards compatible bug fixes
>
> Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

### Converting Markdown to PDF

For sharing and working with protocols in the laboratory, PDF versions of the protocols may be more convenient.

To automatically generate PDF files from your protocol Markdown files:

- Create a file called `create_pdf.yml` (copy from [here](https://github.com/BeBOP-OBON/0_protocol_collection_template/blob/main/.github/workflows/create_pdf.yml)) and place it in your repository in the folder `.github/workflows`.
- Edit the settings of the repository to allow read/write permissions for the Action. Go to Settings > Actions > General > Workflow permissions. Select Read and write permissions.
- This GitHub Action automatically converts your Markdown files into formatted PDFs using a Pandoc/LaTeX container whenever you push changes, then commits those finished PDFs back into your repository for you. 

To manually generate PDF files from your protocol Markdown files, please see below for some alternate tools:

- [Markdowntopdf](https://www.markdowntopdf.com) (online tool)
- [Pandoc](https://pandoc.org/MANUAL.html) (command line tool)

### Getting citable DOIs from Zenodo

Create a release of your repository and get DOIs from Zenodo for each new release (version):

1. Enable the Zenodo-GitHub integration for your repository on your Zenodo profile page.
2. Make sure your repository is Public and has a License.
3. Create a new Release on GitHub using a semantic version tag (e.g., v1.0.0).
4. Zenodo will automatically detect the new release, archive the code associated with that tag, and mint a new specific-version DOI (while linking it to your existing Concept DOI).
5. Look up the GitHub Repository ID by going to https://api.github.com/repos/{user}/{repo}.
6. Add the below lines of code including your Repository ID ({id}) to your repository's README.md file:

```
[![DOI](https://zenodo.org/badge/{id}.svg)](https://zenodo.org/badge/latestdoi/{id})

Concept DOI: [10.5281/zenodo.{concept}](https://doi.org/10.5281/zenodo.{concept})
```

7. Get the Concept DOI by clicking on the badge (first link) and copying the DOI that appears on the right side of the page where it says "Cite all versions?", then add it to the README.md file.

For more information on creating a release of your repository and getting DOIs from Zenodo, please see the guidance [here](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content).

Please also note the [GLOMICON community](https://zenodo.org/communities/glomicon/) on Zenodo. When archiving your repository with Zenodo, please do so in this community.

## See a problem or have a recommendation?

Please use this GitHub repository's [Issue tracker](https://github.com/BeBOP-OBON/0_protocol_collection_template/issues) to request changes/additions or report errors or specific concerns related to the protocol templates.
