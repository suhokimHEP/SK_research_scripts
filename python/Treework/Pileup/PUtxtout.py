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
#filename = '/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/QCD_HT100to200_try.root'
#filename = '/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/ControlRegionStudies/bin/DYJetsToLL_M-50_try.root'
filename = '/uscms/home/skim2/nobackup/SignalProduction/SK_research_scripts/python/Treework/Pileup/DYJetsToLL_M-50_try.root'
_file0 = TFile.Open(filename,'read')
hist = _file0.Get("tmp")
hist.Scale(1/hist.Integral())
for i in range(120):
	norm = hist.GetBinContent(i+1)
	print(norm)

#k=raw_input('Press ENTER to exit')
