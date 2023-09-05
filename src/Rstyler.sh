#!/bin/bash

# Script to run R Styler
# https://confluence.collab.test-and-trace.nhs.uk/display/JQA/How+to+run+Styler+inside+sagemaker

if [ "$1" == "install" ]; then
    echo
    echo "Install styler"
    echo
    Rscript -e 'install.packages("styler", repo="http://cran.rstudio.com/")'
    exit
fi

if [ "$1" == "" ]; then
    echo
    echo "Usage: Rstyler.sh FILE/DIRECTORY"
    echo
    exit
fi

if [ -f $1 ]; then
    ${HOME}/anaconda3/envs/R/bin/Rscript -e 'styler::style_file(commandArgs(trailingOnly = TRUE))' ${1}
    exit
fi

if [ -d $1 ]; then
    ${HOME}/anaconda3/envs/R/bin/Rscript -e 'styler::style_dir(commandArgs(trailingOnly = TRUE))' ${1}
    exit
fi

echo
echo "Invalid file/directory: $1"
echo
