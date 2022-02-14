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


Region = [0,.001803,.0008667,.0008361]
NRegion = ["ctauS-1mm","10mm","100mm","1000mm"]
R2egion = [.001714,.001857,.001051,.0009831]
R3egion = [.00152,.0015,.0009167,.0006957]
R4egion = [.001283,.001298,.001266,.0008437]
gROOT.ForceStyle(kTRUE)
	
c1 = TCanvas( 'c1', 'Histogram Drawing Options', 0, 10, 700, 600 )
c1.SetGrid()
gPad.SetLeftMargin(0.13)
gPad.SetBottomMargin(0.12)
gPad.SetTickx()
gPad.SetTicky()
gStyle.SetOptStat(0)
gStyle.SetLineWidth(3)
gStyle.SetHistLineWidth(3)
h0 = TH1F("","",4,0,4);
h1 = TH1F("","",4,0,4);
h2 = TH1F("","",4,0,4);
h3 = TH1F("","",4,0,4);
for i in range(4):
	h0.SetBinContent(i+1,Region[i])
	h0.GetXaxis().SetBinLabel(i+1,NRegion[i])
	h1.SetBinContent(i+1,R2egion[i])
	h2.SetBinContent(i+1,R3egion[i])
	h3.SetBinContent(i+1,R4egion[i])

h0.SetTitle('BPH-Mu9IP6 Trig Eff')
h0.GetYaxis().SetTitleOffset(1.3)
h0.SetLineColor(1)
h0.Draw('hist')
h0.GetYaxis().SetRangeUser(0.0,0.004)

h1.SetLineColor(2)
h1.Draw('hist SAME')
h2.SetLineColor(3)
h2.Draw('hist SAME')

h3.SetLineColor(4)
h3.Draw('hist SAME')


legend = TLegend(0.15,0.65,0.35,0.87) 		
legend.SetBorderSize(0)
legend.SetTextSize(.0275)
#legend.SetNColumns(2)
legend.SetFillColor(kWhite)
legend.SetFillColor(kWhite)
legend.AddEntry(h0,"MS-07","l")
legend.AddEntry(h1,"MS-15","l")
legend.AddEntry(h2,"MS-40","l")
legend.AddEntry(h3,"MS-55","l")
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
c1.SaveAs('Discs.pdf')
k=raw_input('Press ENTER to exit')
