#======================
# Purpose: Import YAML metadata from BeBOP markdown protocol files
# Author: Kathleen Pitz
# Created: 2026-07-16
#======================

# Import libraries
library(here)
library(yaml)
library(rmarkdown)
library(tibble)
library(dplyr)
library(readr)

# Import BeBOP metadata terms
file_path <- here('examples', 'NOAA-PMEL-OME_eDNA_Collection_Protocol_Sterivex_PeristalticPump.md')

# Import the YAML front matter
metadata_list <- rmarkdown::yaml_front_matter(file_path)

# Create tibble of terms
df <- as_tibble(metadata_list) %>% mutate(file_path = file_path) %>%
  mutate(across(everything(), as.character))

# Import and compare with another sequencing protocol

# Import BeBOP metadata terms
file_path <- here('examples', 'AOML_eDNA_Sampling_Protocol_Sterivex_Beads.md')

# Import the YAML front matter
metadata_list <- rmarkdown::yaml_front_matter(file_path)

# Create tibble of terms
df2 <- as_tibble(metadata_list) %>% mutate(file_path = file_path) %>%
  mutate(across(everything(), as.character))

# Join two tibbles
df_comb <- df %>% full_join(df2)

# Export to compare values across protocols; or submit with datasets
write_csv(df_comb, here('examples', 'BeBOP_protocol_metadata_test.csv'))
