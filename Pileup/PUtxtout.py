## \file
## \ingroup tutorial_pyroot
## \notebook -js
## A Simple histogram drawing example
##
## \macro_image
## \macro_output
## \macro_code
##
## \author Wim Lavrijsen
from __future__ import division
import glob
from ROOT import *
filename = 'new.root'
_file0 = TFile.Open(filename,'read')
hist = _file0.Get("hPU18")
hist.Scale(1/hist.Integral())
for i in range(80):
	norm = hist.GetBinContent(i+1)
	print(norm)

k=raw_input('Press ENTER to exit')
