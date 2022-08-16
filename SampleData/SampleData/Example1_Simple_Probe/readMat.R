library(R.matlab)

sampleData <- R.matlab::readMat("Simple_Probe.mat")


reticulate::py_install("scipy")
reticulate::py_install("https://github.com/HanBnrd/NIRSimple/archive/master.zip
")
library(reticulate)
use_condaenv("r-reticulate")
py_install("mne", pip = TRUE)

py_install("https://github.com/HanBnrd/NIRSimple/archive/master.zip
", pip = TRUE)
py_module_available("NIRSimple")
fh <- import("fhirclient")