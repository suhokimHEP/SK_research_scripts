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
	
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 0, 10, 700, 600 )
c1.SetGrid()
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
gPad.SetLogy()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
Channel = Region[i]
Var = TV[j]
_file0 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/Aug20/ggH_HToSSTo4Tau_MH-125_MS-15_ctauS-100_tree.root','read')
_file1 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/Aug20/QCD_Pt-15to20_tree.root','read')
_file2 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/Aug20/QCD_Pt-20to30_tree.root','read')
_file3 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/Aug20/QCD_Pt-30to50_tree.root','read')
_file4 = TFile.Open('/uscms/home/skim2/nobackup/CMSSW_10_6_12/src/HiggsLongLived/WorkareaSA/bin/CuttedTree/Aug20/QCD_Pt-50to80_tree.root','read')

h0=_file0.Get('Oppsublead')
h1=_file1.Get('Oppsublead')
h2=_file2.Get('Oppsublead')
h3=_file3.Get('Oppsublead')
h4=_file4.Get('Oppsublead')
h0.GetXaxis().SetTitle('subleadROI score')
h0.GetYaxis().SetTitle('Unit Normalized')
h0.GetYaxis().SetTitleOffset(1.3)
h0.Scale(4.414)
h0.SetLineColor(1)

h1.Scale(2799000.0)
h2.Scale(2526000.0)
h3.Scale(1362000.0)
h4.Scale(376600.0)
h1.Add(h2)
h1.Add(h3)
h1.Add(h4)
h1.SetLineColor(2)
for i in range(70):
	h1.SetBinContent(i+1,2.5+math.sqrt(h1.GetBinContent(i+1)))
h0.Divide(h1)
h0.Draw('HIST')
h0.GetXaxis().SetRangeUser(0.3,1.0)
#h0.GetYaxis().SetRangeUser(0.001,1.0)

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
c1.SaveAs('Punzi_%s.pdf'%Var)
k=raw_input('Press ENTER to exit')
