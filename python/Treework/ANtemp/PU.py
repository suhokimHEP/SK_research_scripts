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
from ROOT import *
import math

gROOT.ForceStyle(kTRUE)
Var="PUWeight"	
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 0, 10, 700, 600 )
c1.SetGrid()
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/Extrafile/2018_puWeights_BPH_69200.root','read')

h0=_file0.Get('h_PUweight')
h0.Draw('hist')
h0.GetXaxis().SetTitle('subleadROI score')
h0.GetYaxis().SetTitle('Unit Normalized')
h0.GetYaxis().SetTitleOffset(1.3)
h0.SetLineColor(1)


legend = TLegend(0.65,0.75,0.85,0.87) 		
legend.SetBorderSize(0)
legend.SetTextSize(.0175)
#legend.SetNColumns(2)
legend.SetFillColor(kWhite)
legend.SetFillColor(kWhite)
legend.AddEntry(h0,"Punzi","l")
legend.Draw()
title = TText(1,1,"") 
title.SetTextSize(0.045)
title.SetTextColor(kBlack)
title.SetTextAlign(11)
title.SetTextFont(62)

extra = TText(1,1,"") 
extra.SetTextSize(0.03)
extra.SetTextColor(kBlack)
extra.SetTextAlign(11)
extra.SetTextFont(52)

extra2 = TLatex(1,1,"") 
extra2.SetTextSize(0.025)
extra2.SetTextColor(kBlack)
extra2.SetTextAlign(11)
extra2.SetTextFont(62)
title.DrawTextNDC(0.2,0.91,"CMS")
extra.DrawTextNDC(0.3,0.91,"Preliminary")
extra2.DrawLatexNDC(0.55,0.91,"Run2")
c1.Modified()
c1.Update()
#k=raw_input('Press ENTER to exit')
c1.SaveAs('PUWeight_%s.pdf'%Var)
k=raw_input('Press ENTER to exit')
